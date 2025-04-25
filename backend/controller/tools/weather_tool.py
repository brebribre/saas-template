from agents import function_tool

class WeatherTool:
    @function_tool
    def get_weather(location: str) -> str:
        return "Weather data for " + location + " is sunny"
