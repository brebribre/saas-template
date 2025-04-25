from agents import function_tool

class WeatherTool:
    #@function_tool # remove this depending on whether we want to use Agents SDK or Responses API
    def get_weather(location: str) -> str:
        return "Weather data for " + location + " is sunny"
