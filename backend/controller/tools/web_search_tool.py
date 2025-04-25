from duckduckgo_search import DDGS

class WebSearchTool:
    def web_search(query: str, max_results: int = 3) -> str:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=max_results)
            if not results:
                return "No results found."
            return results
