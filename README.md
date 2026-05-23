# Agentic Bootcamp

A hands-on workspace for building agentic AI applications using [Google ADK](https://google.github.io/adk-docs/) and the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

---

## What's inside

### `pilot_agent/` — ADK Agent with Custom MCP Server

Demonstrates a full ADK ↔ MCP integration loop:

```
User
 └─► ADK LlmAgent (Claude Sonnet via LiteLLM)
      └─► McpToolset (MCP client)
           └─► my_adk_mcp_server.py (custom MCP server)
                └─► ADK FunctionTool (create_file)
```

- The **agent** (`pilot_agent/agent.py`) is powered by `claude-sonnet-4-6` via LiteLLM and connects to a custom MCP server over stdio.
- The **MCP server** (`my_adk_mcp_server.py`) wraps an ADK `FunctionTool` and exposes it to any MCP-compatible client — demonstrating how to bridge ADK tools into the broader MCP ecosystem.

This pattern is useful when you want to reuse ADK tools across different agents or frameworks without rewriting them.

---

## Setup

**Prerequisites:** Python 3.14+, Docker Desktop

```bash
# Clone the repo
git clone <repo-url>
cd Agentic-Bootcamp

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Environment variables

Create `pilot_agent/.env`:

```env
GOOGLE_API_KEY=your_google_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GITHUB_TOKEN=your_github_pat        # needs public_repo scope
```

---

## Running the agent

```bash
adk run pilot_agent
```

The agent will start, launch the MCP server as a subprocess, and be ready to accept instructions such as:

```
> Create a file called notes.txt
> List the files in the current directory
```

---

## Tech stack

| Layer | Technology |
|---|---|
| Agent framework | [Google ADK](https://google.github.io/adk-docs/) |
| LLM | Claude Sonnet 4.6 via [LiteLLM](https://docs.litellm.ai/) |
| Tool protocol | [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) |
| MCP transport | stdio |
| Package manager | pip + venv |

---

## Project structure

```
.
├── pilot_agent/
│   ├── agent.py              # ADK agent definition (MCP client)
│   ├── .env                  # API keys (not committed)
│   └── __init__.py
├── my_adk_mcp_server.py      # Custom MCP server wrapping ADK tools
├── requirements.txt
└── CLAUDE.md                 # Claude Code project instructions
```
