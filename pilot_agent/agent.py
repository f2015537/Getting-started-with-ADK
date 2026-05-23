import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from google.adk.models.lite_llm import LiteLlm

PATH_TO_YOUR_MCP_SERVER_SCRIPT = os.getenv("MCP_SERVER_PATH")

root_agent = LlmAgent(
    model=LiteLlm(model="anthropic/claude-sonnet-4-6"),
    name="file_management_agent",
    instruction="Use the 'create_file' tool to create a new file with the name provided by the user.",
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="python3",
                    args=[PATH_TO_YOUR_MCP_SERVER_SCRIPT],
                )
            )
        )
    ],
)
