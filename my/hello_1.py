# hello.py
# /// script
# requires-python = ">=3.10"
# dependencies = ["flyte>=2.0.0b0"]
# ///
# uv run --prerelease=allow my/hello_1.py
# flyte --config .flyte/config.yaml run my/hello_1.py main

import flyte
import asyncio

env = flyte.TaskEnvironment(name="hello_world", resources=flyte.Resources(memory="250Mi"))


@env.task
def calculate(x: int) -> int:
    return x * 2 + 5


@env.task
async def main(numbers: list[int] = [1, 2, 3]) -> float:
    # Parallel execution across distributed containers
    results = await asyncio.gather(*[calculate.aio(num) for num in numbers])
    return sum(results) / len(results)


if __name__ == "__main__":
    flyte.init_from_config(".flyte/config.yaml")
    run = flyte.run(main, numbers=list(range(10)))
    print(f"Result: {run.result}")
    print(f"View at: {run.url}")
