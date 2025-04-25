import os
from typing import List, Dict, Any, Optional
from openai import OpenAI
from dotenv import load_dotenv

class OpenAIUtils:
    """Utility class for OpenAI API interactions"""
    
    def __init__(self, api_key: Optional[str] = None):
        if not api_key:
            load_dotenv()
            api_key = os.getenv('OPENAI_API_KEY')
            
        if not api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass directly.")
            
        self.client = OpenAI(api_key=api_key)
    
    def create_response(self, 
                       input_text: str, 
                       model: str = "gpt-4o", 
                       tools: Optional[List[Dict[str, Any]]] = None,
                       temperature: float = 0.7) -> Dict[str, Any]:
        """Create a response using the OpenAI responses API
        
        Args:
            input_text: The user's input query
            model: The model to use (default: gpt-4o)
            tools: Optional list of tools to enable
            temperature: Sampling temperature, between 0 and 2
            
        Returns:
            The complete response from the OpenAI API
        """
        if tools is None:
            tools = []
        
        params = {
            "model": model,
            "input": input_text,
            "tools": tools,
            "temperature": temperature,
        }
        
        # Make the API request
        response = self.client.responses.create(**params)
        
        return response
