import json

from mcp.server.fastmcp import FastMCP

from generated_tools.issues import list_my_issues

mcp = FastMCP("github-rest")


@mcp.tool()
def github_list_my_issues(**kwargs):
    return list_my_issues(**kwargs)


def main():
    mcp.run_stdio()


if __name__ == "__main__":
    main()
