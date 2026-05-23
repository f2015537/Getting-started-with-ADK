# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment

Python 3.14 virtual environment is pre-configured at `.venv/`.

```bash
source .venv/bin/activate
pip install <package>
```

Always install dependencies into `.venv` rather than globally.

## Project context

This is an **Agentic Bootcamp** workspace — a learning environment for building agentic AI applications. As exercises and projects are added, update this file with relevant build/run/test commands.

## Dependencies

Install all dependencies into `.venv`:

```bash
pip install -r requirements.txt
```

Key packages: `google-adk`, `litellm`, `mcp`, `black`.

## Agents

### pilot_agent

A GitHub assistant agent that uses the [GitHub MCP server](https://github.com/github/github-mcp-server) via Docker to interact with GitHub repositories.

- **Model:** `gemini-2.5-flash`
- **Tools:** GitHub MCP server (runs via Docker)
- **Requires:** Docker Desktop running, `GITHUB_TOKEN` set in `pilot_agent/.env`

**Run:**

```bash
adk run pilot_agent
```

**Environment (`pilot_agent/.env`):**

```
GOOGLE_API_KEY=your_google_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GITHUB_TOKEN=your_github_pat
```

The GitHub PAT needs at least the `public_repo` scope for public repositories.
