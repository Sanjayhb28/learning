from langchain_tavily import TavilySearch


def get_profile_url_tavily(name: str) -> str:
    search = TavilySearch()
    result = search.run(name)
    return result
