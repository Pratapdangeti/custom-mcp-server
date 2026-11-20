import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client


async def main():
    url = "http://localhost:8080/mcp"

    async with streamable_http_client(url) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()

            for tool in tools.tools:
                print("Available tool:", tool.name)

            result = await session.call_tool(
                "average_values", arguments={"values": [10, 20, 30, 40]}
            )

            print("Result:", result.content)


if __name__ == "__main__":
    asyncio.run(main())
