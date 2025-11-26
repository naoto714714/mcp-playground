# mcp-playground

MCP (Model Context Protocol) サーバーのサンプル実装です。FastMCP を使用して、リソース、ツール、プロンプトを提供するシンプルなサーバーをデモンストレーションしています。

## 概要

このプロジェクトは MCP サーバーの基本的な実装例を提供します。以下の機能が含まれています：

- **リソース**: 今日のラッキーカラーを取得する静的リソース
- **ツール**: 指定された URL から HTML コンテンツを取得するツール
- **プロンプト**: エラーメッセージを解析するためのプロンプト

## 必要環境

- Python 3.13 以上
- [uv](https://github.com/astral-sh/uv) パッケージマネージャー

## セットアップ

### 1. 依存関係のインストール

```bash
uv sync
```

### 2. MCP サーバーの設定

`example_mcp.json` を参考に、使用している MCP クライアント（例：Claude Desktop）の設定ファイルに以下の設定を追加します：

```json
{
  "mcpServers": {
    "mcp-playground": {
      "command": "<uvのパス>",
      "args": [
        "--directory",
        "<このプロジェクトのディレクトリ>",
        "run",
        "mcp-tools.py"
      ]
    }
  }
}
```

### 3. uvのパスを確認

```bash
which uv
```

## 使用方法

### サーバーの起動

```bash
uv run mcp-tools.py
```

### 提供されるリソース・ツール・プロンプト

#### リソース
- **lucky-color://static** - 今日のラッキーカラーを返します

#### ツール
- **fetch_html(url)** - 指定された URL から HTML コンテンツを取得します

#### プロンプト
- **error_analysis_prompt(error)** - エラーメッセージを解析するためのプロンプトを生成します

## プロジェクト構成

```
mcp-playground/
├── README.md              # このファイル
├── mcp-tools.py           # MCP サーバーの実装
├── example_mcp.json       # MCP クライアント設定の例
├── pyproject.toml         # プロジェクト設定（依存関係定義）
└── uv.lock                # 依存関係ロックファイル
```

## 依存パッケージ

- **mcp** (>=1.6.0) - Model Context Protocol のサーバー実装フレームワーク
- **requests** (>=2.32.3) - HTTP リクエスト用ライブラリ

## ライセンス

このプロジェクトはサンプルコードです。自由に改変・利用できます。

## 参考資料

- [Model Context Protocol (MCP) ドキュメント](https://modelcontextprotocol.io/)
- [FastMCP](https://github.com/jlowin/fastmcp)
