# https://www.union.ai/docs/v2/flyte/user-guide/flyte-2/
# uv run --prerelease allow examples/hello_async.py
# flyte --config .flyte/config.yaml run examples/hello.py main
# flyte run --local examples/hello.py main

import asyncio
import flyte

env = flyte.TaskEnvironment("hello_world")

@env.task
async def hello_world(name: str) -> str:
    return f"Hello, {name}!"

@env.task(short_name="hello-async")
async def main(name: str) -> str:
    results = []
    for i in range(10):
        results.append(hello_world(name))
    await asyncio.gather(*results)
    return "Done"

if __name__ == "__main__":
    flyte.init_from_config(".flyte/config.yaml")
    run = flyte.run(main, name="World")
    print(f"Run name = {run.name}")
    print(f"Run URL = {run.url}")
