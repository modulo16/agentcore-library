import threading
import time
from datetime import timedelta
from mcp import StdioServerParameters, stdio_client
from mcp.client.streamable_http import streamable_http_client
from mcp.server import FastMCP
from strands import Agent
from strands.tools.mcp import MCPClient

# Connect to an MCP Server using stdio
stdio_mcp_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", args=["awslabs.aws-documentation-mcp-server@latest"]
        )
    )
)

with stdio_mcp_client:
    # Get the tools
    tools = stdio_mcp_client.list_tools_sync()

    # create an agent with the tools
    agent = Agent(model="us.anthropic.claude-sonnet-4-5-20250929-v1:0", tools=tools)

    response = agent("What is the pricing on AWS Transform?")
