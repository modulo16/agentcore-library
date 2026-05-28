import threading
import time
from datetime import timedelta
from mcp import StdioServerParameters, stdio_client
from mcp.client.streamable_http import streamable_http_client
from mcp.server import FastMCP
from strands import Agent
from strands.tools.mcp import MCPClient


def create_streamable_http_transport():
    return streamable_http_client("http://localhost:8000/mcp")


streamable_http_mcp_client = MCPClient(create_streamable_http_transport)

with streamable_http_mcp_client:
    # Get the tools
    tools = streamable_http_mcp_client.list_tools_sync()

    # create an agent with the tools
    agent = Agent(model="us.anthropic.claude-sonnet-4-5-20250929-v1:0", tools=tools)

    response = agent("What is 1500 + 758473?")
