import os
import json
from typing import List, Dict, Any, Optional, Union
from openai import OpenAI
from dotenv import load_dotenv
from agents import Agent, Runner,function_tool
import asyncio
from controller.tools.tools import Tools

class OpenAIUtils:
    """Utility class for OpenAI API interactions"""
    
    def __init__(self, api_key: Optional[str] = None):
        if not api_key:
            load_dotenv()
            api_key = os.getenv('OPENAI_API_KEY')
            
        if not api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY environment variable or pass directly.")
            
        self.client = OpenAI(api_key=api_key)
        self.tools = Tools()
    def create_response(self, 
                       input_text: Union[str, List[Dict[str, str]]], 
                       model: str = "gpt-4o", 
                       stream: bool = False,
                       tools: Optional[List[Dict[str, Any]]] = None,
                       temperature: float = 0.7) -> Dict[str, Any]:
        """Create a response using the OpenAI Chat Completions API
        
        Args:
            input_text: Either a string message or a list of message objects with role and content
            model: The model to use (default: gpt-4o)
            tools: Optional list of tools to enable
            temperature: Sampling temperature, between 0 and 2
            
        Returns:
            The complete response from the OpenAI API
        """
        if tools is None:
            tools = []
        
        # Format the input correctly based on its type
        if isinstance(input_text, str):
            formatted_input = [{"role": "user", "content": input_text}]
        elif isinstance(input_text, list):
            formatted_input = input_text
        else:
            raise ValueError("input_text must be either a string or a list of message objects")
        
        try:
            params = {
                "model": model,
                "input": formatted_input,
                "temperature": temperature,
                "stream": stream,
            }
            
            # Only add tools if there are any
            if tools:
                params["tools"] = tools

            print('PARAMS', params)
            
            # Make the API request
            response = self.client.responses.create(**params)

            response_data = response.model_dump()

            call = response_data["output"][0]

            if call["type"] == "function_call":
                tool_name = call["name"]
                tool_args = json.loads(call["arguments"])
                tool_response = self.tools.call_tool(tool_name, tool_args)

                return tool_response
            else:
                return response_data
            
        except Exception as e:
            print(f"Error making OpenAI API request: {str(e)}")
            if hasattr(e, 'response') and hasattr(e.response, 'text'):
                print(f"Response details: {e.response.text}")
            raise

    async def create_single_agent_response(self, 
                             name: str,
                             instructions: str,
                             input_text: Union[str, List[Dict[str, str]]], 
                             model: str = "gpt-4o", 
                             stream: bool = False,
                             tools: Optional[List[Dict[str, Any]]] = None,
                             temperature: float = 0.7) -> Dict[str, Any]:
        """Create a response using the OpenAI Agent API
        
        Args:
            input_text: Either a string message or a list of message objects with role and content
            model: The model to use (default: gpt-4o)
            tools: Optional list of tools to enable
            temperature: Sampling temperature, between 0 and 2
            
        Returns:
            The complete response from the OpenAI API
        """
        if tools is None:
            tools = []
        
        # Format the input correctly based on its type
        if isinstance(input_text, str):
            formatted_input = [{"role": "user", "content": input_text}]
        elif isinstance(input_text, list):
            formatted_input = input_text
        else:
            raise ValueError("input_text must be either a string or a list of message objects")
        
        try:
            agent = Agent(name, instructions=instructions, tools=tools)
            
            response = await Runner.run(agent, input_text)
            
            return response
            
        except Exception as e:
            print(f"Error making OpenAI API request: {str(e)}")
            if hasattr(e, 'response') and hasattr(e.response, 'text'):
                print(f"Response details: {e.response.text}")
            raise
            