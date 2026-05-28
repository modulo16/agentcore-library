import warnings

warnings.filterwarnings(action="ignore", message=r"datetime.datetime.utcnow")

from strands import Agent, tool

# This is an example agent that demonstrates how to use the Agent class from the strands library.
# aws bedrock list-foundation-models if needed.


@tool
def weather():
    return "The weather is sunny and warm."


agent = Agent(
    model="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    tools=[weather],
    system_prompt="You are a helpful assistant that provides concise responses, you can also use the tools provided to answer questions. If you don't know the answer, say you don't know. Always use the tools when they are relevant to the question.",
)
response = agent("What is the weather like today?")
