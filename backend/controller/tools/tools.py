from typing import Dict, Any, List
from .weather_tool import WeatherTool
from agents import WebSearchTool

class Tools:
    """
    A class that stores and manages tool definitions for the OpenAI API.
    Tool implementations will be defined in separate files and integrated later.
    """
    def __init__(self):
        # 1. add new tools here
        self.tools = [
            {
                "type": "function",
                "name": "get_weather",
                "description": "Get current temperature for a given location.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City and country e.g. Bogotá, Colombia"
                        }
                    },
                    "required": [
                        "location"
                    ],
                    "additionalProperties": False
                }
            } 
        ]
        # 2. map the tool definitions to the tool implementations here
        self.tools_map = {
            "get_weather": WeatherTool.get_weather,
        }
        # 3. make a new <tool_name>_tool.py file for each tool implementation. See weather_tool.py for example
    
    @staticmethod
    def get_all_tools_definitions() -> List[Dict[str, Any]]:
        return Tools().tools

    @staticmethod
    def get_all_function_tools() -> List[Dict[str, Any]]:
        """Get all function tools. This if for OpenAI Agent SDK"""
        return Tools().tools_map

    @staticmethod
    def get_tools_by_names(tool_names: List[str]) -> List[Dict[str, Any]]:
        """Get tool definitions for the specified tool names"""
        return [tool for tool in Tools().get_all_tools_definitions() if tool.get("name") in tool_names]

    @staticmethod
    def get_function_tools_by_names(tool_names: List[str]) -> List[Any]:
        """
        Get function tools for the specified tool names.
        """
        tools_map = Tools().tools_map
        return [tools_map[name] for name in tool_names if name in tools_map]
    
    # Only for Responses API. OpenAI SDK already has a tool calling mechanism built in.
    def call_tool(self, tool_name: str, tool_args) -> Dict[str, Any]:
        print('TOOL_NAME', tool_name)
        print('TOOL_ARGS', tool_args)
        if tool_name == "get_weather":
            return WeatherTool.get_weather(**tool_args)
        else:
            raise ValueError(f"Tool {tool_name} not found")

