import os

from icecream import ic


def _load_mcp_from_dir(mcp_dir):
    return [
        x for x in os.listdir(mcp_dir) if x.startswith("mcp_") and x.endswith(".py")
    ]


def _create_json_mcp(mpc_name, mcp_file_name, mcp_dir):
    x = {
        mpc_name: {
            "command": "python",
            "args": [
                f"{mcp_dir}{mcp_file_name}",
            ],
            "transport": "stdio",
        },
    }
    return x


def get_mcp_config_from_dir(mcp_dir):
    # return {_create_json_mcp(x, x, mcp_dir) for x in _load_mcp_from_dir(mcp_dir)}
    # return {x: _create_json_mcp(x, x, mcp_dir) for x in _load_mcp_from_dir(mcp_dir)}
    return {
        k: v
        for x in _load_mcp_from_dir(mcp_dir)
        for k, v in _create_json_mcp(x, x, mcp_dir).items()
    }


if __name__ == "__main__":
    MCP_DIR = "/Users/dominik/2025/GPT/mcp/agents/src/agents/tools/"

    print(get_mcp_config_from_dir(MCP_DIR))
