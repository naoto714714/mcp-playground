"""
Simple Echo MCP Server
This example demonstrates a basic MCP server that exposes a simple echo tool.
"""

from mcp.server.fastmcp import FastMCP

# MCPサーバを作成
mcp = FastMCP("Echo Server")


# テキストをエコーバックするツールを定義
@mcp.tool()
def echo(text: str) -> str:
    """Echo the input text back to the caller."""
    return f"Echo: {text}"


# サーバを実行（スクリプト直接実行時）
if __name__ == "__main__":
    # デフォルトでstdioトランスポートを使用してサーバを起動
    mcp.run()
