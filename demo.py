# server.py
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add_num(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://static")
def get_greeting() -> str:
    """Get a personalized greeting"""
    return "Hello, こんにちは!"


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("以下のエラーメッセージが出ました:"),
        base.UserMessage(error),
        base.AssistantMessage("私はエラーメッセージを読み解き、適切な対処を教えます"),
    ]


if __name__ == "__main__":
    mcp.run()
