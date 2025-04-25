from typing import Dict, Any, List
from .weather_tool import WeatherTool

class Tools:
    """
    A class that stores and manages tool definitions for the OpenAI API.
    Tool implementations will be defined in separate files and integrated later.
    """
    def __init__(self):
        self.tools = [
            {
                "type": "web_search_preview",
                "name": "web_search"
            },
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
        self.tools_map = {
            "get_weather": WeatherTool.get_weather
        }
    
    @staticmethod
    def get_all_tools_definitions() -> List[Dict[str, Any]]:
        return Tools().tools
        
    def call_tool(self, tool_name: str, tool_args) -> Dict[str, Any]:
        if tool_name in self.tools_map:
            return self.tools_map[tool_name](**tool_args)
        else:
            raise ValueError(f"Tool {tool_name} not found")

    @staticmethod
    def get_tools_by_names(tool_names: List[str]) -> List[Dict[str, Any]]:
        """Get tool definitions for the specified tool names"""
        return [tool for tool in Tools().get_all_tools_definitions() if tool.get("name") in tool_names]