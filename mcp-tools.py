import random

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp-playground")  # 適当なサーバー名


@mcp.resource("lucky-color://static")  # 適当なパス
def get_lucky_color() -> str:
    """今日のラッキーカラーを取得する"""
    return random.choice(["赤", "青", "緑", "黄"])


@mcp.tool()
def fetch_html(url: str) -> str:
    """
    指定されたURLからHTMLを取得して返します。

    Args:
        url (str):  取得対象のウェブページのURL

    Returns:
        str: 取得したHTML
    """
    response = requests.get(url)
    return response.text


from mcp.server.fastmcp.prompts import base


@mcp.prompt()
def error_analysis_prompt(error: str) -> list[base.Message]:
    """エラーメッセージを解析するときのプロンプト"""
    return [
        base.UserMessage("以下のエラーメッセージが出ました:"),
        base.UserMessage(error),
        base.AssistantMessage("エラーメッセージを読み対処方法を教えます"),
    ]


if __name__ == "__main__":
    mcp.run()
