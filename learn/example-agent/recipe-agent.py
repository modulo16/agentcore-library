from strands import Agent, tool
from ddgs import DDGS
from ddgs.exceptions import RatelimitException, DDGSException
import logging

logging.getLogger("strands").setLevel(logging.INFO)


@tool
def websearch(
    keywords: str, region: str = "us-en", max_results: int | None = None
) -> str:
    """Search duckduckgo for the updated information.
    Args:
        keywords: The search query.
        region: The region to search in, default is "us-en".
        max_results: The maximum number of results to return, default is None (no limit).
    Returns:
        A list of dictionaries containing the search results.
    """
    try:
        results = DDGS().text(keywords, region - region, max_results=max_results)
        return results if results else "No results found."
    except RatelimitException:
        return "DuckDuckGo rate limit exceeded. Please try again later."
    except DDGSException as d:
        return f"An error occurred while searching DuckDuckGo: {str(d)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


recipe_agent = Agent(
    model="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    tools=[websearch],
    system_prompt="""
You are a helpful recipe assistant that provides users with recipes based on ingredients. You also answer general questionsa bout cooking. Utilize the websearch tool to find recipes when users mention ingredients.
""",
)
response = recipe_agent(
    "I have chicken, tomatoes, and basil. What can I cook for dinner?"
)
print(response)
