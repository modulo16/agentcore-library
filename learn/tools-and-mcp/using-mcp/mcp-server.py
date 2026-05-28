import threading
import time
from datetime import timedelta
from mcp import StdioServerParameters, stdio_client
from mcp.client.streamable_http import streamable_http_client
from mcp.server import FastMCP
from strands import Agent
from strands.tools.mcp import MCPClient

mcp = FastMCP("Calculator Server")


@mcp.tool(description="Calculator tool for calculating.")
def calculator(x: int, y: int) -> int:
    return x + y


@mcp.tool(description="This tool is design to run for a long time.")
def long_running_tool(name: str) -> str:
    time.sleep(25)
    return f"Hello, {name}!"


def main():
    mcp.run(transport="streamable-http", mount_path="mcp")


thread = threading.Thread(target=main)
thread.start()
