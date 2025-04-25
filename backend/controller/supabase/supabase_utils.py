import os
from supabase import create_client, Client
from dotenv import load_dotenv
from typing import Dict, List, Any, Optional, Union

# Load environment variables
load_dotenv()


class SupabaseController:
    def __init__(self):
        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_SERVICE_KEY")

        if not self.supabase_url or not self.supabase_key:
            raise ValueError(
                "Supabase URL and key must be provided in environment variables"
            )

        self.client: Client = create_client(self.supabase_url, self.supabase_key)

    def select(
        self,
        table_name: str,
        columns: str = "*",
        filters: Optional[Dict[str, Any]] = None,
        order_by: Optional[Dict[str, str]] = None,
        limit: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        """
        Select data from a table with optional filtering, ordering, and limiting.

        Args:
            table_name: Name of the table to query
            columns: Columns to select (default "*" for all columns)
            filters: Dictionary of column-value pairs for filtering
            order_by: Dictionary with column name as key and "asc" or "desc" as value
            limit: Maximum number of rows to return

        Returns:
            List of dictionaries representing the selected rows
        """
        query = self.client.table(table_name).select(columns)

        # Apply filters if provided
        if filters:
            for column, value in filters.items():
                query = query.eq(column, value)

        # Apply ordering if provided
        if order_by:
            for column, direction in order_by.items():
                if direction.lower() == "asc":
                    query = query.order(column)
                else:
                    query = query.order(column, desc=True)

        # Apply limit if provided
        if limit:
            query = query.limit(limit)

        # Execute the query
        response = query.execute()

        # Check for errors
        if hasattr(response, "error") and response.error:
            raise Exception(f"Supabase query error: {response.error.message}")

        return response.data

    def insert(
        self, table_name: str, data: Union[Dict[str, Any], List[Dict[str, Any]]]
    ) -> Dict[str, Any]:
        """
        Insert one or more rows into a table.

        Args:
            table_name: Name of the table to insert into
            data: Dictionary or list of dictionaries containing the data to insert

        Returns:
            Dictionary containing the inserted data
        """
        response = self.client.table(table_name).insert(data).execute()

        # Check for errors
        if hasattr(response, "error") and response.error:
            raise Exception(f"Supabase insert error: {response.error.message}")

        return response.data

    def update(
        self, table_name: str, data: Dict[str, Any], filters: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Update rows in a table that match the given filters.

        Args:
            table_name: Name of the table to update
            data: Dictionary containing the columns and values to update
            filters: Dictionary of column-value pairs for filtering which rows to update

        Returns:
            Dictionary containing the updated data
        """
        query = self.client.table(table_name).update(data)

        # Apply filters
        for column, value in filters.items():
            query = query.eq(column, value)

        response = query.execute()

        # Check for errors
        if hasattr(response, "error") and response.error:
            raise Exception(f"Supabase update error: {response.error.message}")

        return response.data

    def delete(self, table_name: str, filters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delete rows from a table that match the given filters.

        Args:
            table_name: Name of the table to delete from
            filters: Dictionary of column-value pairs for filtering which rows to delete

        Returns:
            Dictionary containing the deleted data
        """
        query = self.client.table(table_name).delete()

        # Apply filters
        for column, value in filters.items():
            query = query.eq(column, value)

        response = query.execute()

        # Check for errors
        if hasattr(response, "error") and response.error:
            raise Exception(f"Supabase delete error: {response.error.message}")

        return response.data

    def execute_rpc(
        self, function_name: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Execute a stored procedure (RPC function) in the Supabase database.

        Args:
            function_name: Name of the function to execute
            params: Dictionary of parameters to pass to the function

        Returns:
            Dictionary containing the result of the function call
        """
        response = self.client.rpc(function_name, params or {}).execute()

        # Check for errors
        if hasattr(response, "error") and response.error:
            raise Exception(f"Supabase RPC error: {response.error.message}")

        return response.data

    def raw_query(
        self, query: str, params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Execute a raw SQL query.
        Note: This requires the service role key and proper permissions.

        Args:
            query: SQL query string
            params: Dictionary of parameters to pass to the query

        Returns:
            Dictionary containing the query results
        """
        # This requires the service role key
        response = self.client.rpc(
            "exec_sql", {"query": query, "params": params or {}}
        ).execute()

        # Check for errors
        if hasattr(response, "error") and response.error:
            raise Exception(f"Supabase raw query error: {response.error.message}")

        return response.data

    def get_table_schema(self, table_name: str) -> Dict[str, Any]:
        """
        Get the schema information for a specific table.

        Args:
            table_name: Name of the table to get schema for

        Returns:
            Dictionary containing the table schema information
        """
        query = f"""
        SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name = '{table_name}'
        ORDER BY ordinal_position
        """

        return self.raw_query(query)

    def list_tables(self) -> List[str]:
        """
        Get a list of all tables in the database.

        Returns:
            List of table names
        """
        query = """
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name
        """

        result = self.raw_query(query)
        return [row["table_name"] for row in result]

    def get_storage_url(self, bucket: str, path: str) -> str:
        """
        Get a public URL for a file in Supabase Storage.

        Args:
            bucket: Storage bucket name
            path: Path to the file within the bucket

        Returns:
            Public URL for the file
        """
        return self.client.storage.from_(bucket).get_public_url(path)

    def upload_file(
        self,
        bucket: str,
        path: str,
        file_data: bytes,
        content_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Upload a file to Supabase Storage.

        Args:
            bucket: Storage bucket name
            path: Path where the file should be stored
            file_data: Binary data of the file
            content_type: MIME type of the file

        Returns:
            Dictionary containing the upload result
        """
        options = {}
        if content_type:
            options["content_type"] = content_type

        response = self.client.storage.from_(bucket).upload(path, file_data, options)

        # Check for errors
        if hasattr(response, "error") and response.error:
            raise Exception(f"Supabase storage upload error: {response.error.message}")

        return response

    def download_file(self, bucket: str, path: str) -> bytes:
        """
        Download a file from Supabase Storage.

        Args:
            bucket: Storage bucket name
            path: Path to the file within the bucket

        Returns:
            Binary data of the file
        """
        response = self.client.storage.from_(bucket).download(path)

        # Check for errors
        if hasattr(response, "error") and response.error:
            raise Exception(
                f"Supabase storage download error: {response.error.message}"
            )

        return response

    def get_signed_url(
        self, bucket: str, path: str, expires_in: int = 3600
    ) -> Dict[str, Any]:
        """
        Generate a signed URL for temporary access to a file in Supabase Storage.

        Args:
            bucket: Storage bucket name
            path: Path to the file within the bucket
            expires_in: Expiration time in seconds (default: 1 hour)

        Returns:
            Dictionary containing the signed URL information
        """
        response = self.client.storage.from_(bucket).create_signed_url(path, expires_in)

        # Check for errors
        if hasattr(response, "error") and response.error:
            raise Exception(
                f"Supabase signed URL generation error: {response.error.message}"
            )

        return response

    def delete_file(self, bucket: str, path: str) -> Dict[str, Any]:
        """
        Delete a file from Supabase Storage.

        Args:
            bucket: Storage bucket name
            path: Path to the file within the bucket

        Returns:
            Dictionary containing the deletion result
        """
        response = self.client.storage.from_(bucket).remove([path])

        # Check for errors
        if hasattr(response, "error") and response.error:
            raise Exception(f"Supabase storage delete error: {response.error.message}")

        return response
