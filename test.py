import asyncio

from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.core.program import FunctionCallingProgram

Settings.llm = Ollama(model="llama3.2:1b", request_timeout=360.0)

from llama_index.core.tools import FunctionTool

import nest_asyncio

nest_asyncio.apply()


def multiply(a: int | str, b: int | str) -> int:
    """Multiple two integers and returns the result integer"""
    if isinstance(a, str):
        a = int(a)
    if isinstance(b, str):
        b = int(b)
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)


def add(a: int | str, b: int | str) -> int:
    """Add two integers and returns the result integer"""
    if isinstance(a, str):
        a = int(a)
    if isinstance(b, str):
        b = int(b)
    return a + b


add_tool = FunctionTool.from_defaults(fn=add)

from llama_index.core.agent import FunctionCallingAgent

agent = FunctionCallingAgent.from_tools(
    [multiply_tool, add_tool],
    verbose=True,
    allow_parallel_tool_calls=False,
)

response = agent.chat("What is (121 + 2) * 5?")
print(response.sources)

# enable parallel function calling
agent = FunctionCallingAgent.from_tools(
    [multiply_tool, add_tool],
    verbose=True,
    allow_parallel_tool_calls=True,
)


async def get_response(agent) -> asyncio.coroutines:
    await agent.achat("What is (121 * 3) + (5 * 8)?")


# response = await agent.achat("What is (121 * 3) + (5 * 8)?")
response = asyncio.run(get_response(agent))
print(str(response))
