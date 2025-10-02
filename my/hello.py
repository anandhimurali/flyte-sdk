# hello.py
# https://www.union.ai/docs/v2/byoc/user-guide/getting-started/#hello-world-example
# uv run --prerelease allow examples/hello.py
# flyte --config .flyte/config.yaml run examples/hello.py main
# flyte run --local examples/hello.py main

import flyte
import logging
import os

# Configure logging to include process ID
logging.basicConfig(level=logging.INFO, format="%(asctime)s - PID:%(process)d - %(levelname)s - %(message)s")

# A TaskEnvironment provides a way of grouping the configuration used by tasks.
env = flyte.TaskEnvironment(name="hello_world")


# Use a TaskEnvironment to define tasks, which are regular Python functions.
@env.task
def fn(x: int) -> int:  # Type annotations are recommended.
    slope, intercept = 2, 5
    logging.info(f"I am running fn with x={x}.")
    print(f"{os.getpid()}: I am running fn with x={x}.")
    return slope * x + intercept


# Tasks can call other tasks.
# Each task defined with a given TaskEnvironment will run in its own separate container,
# but the containers will all be configured identically.
@env.task
def main(x_list: list[int] = list(range(10))) -> float:
    logging.info(f"Running main function with x_list={x_list}.")
    print(f"{os.getpid()}: Running main function with x_list={x_list}.")
    x_len = len(x_list)
    if x_len < 10:
        raise ValueError(f"x_list doesn't have a larger enough sample size, found: {x_len}")

    # flyte.map is like Python map, but runs in parallel.
    y_list = list(flyte.map(fn, x_list))
    y_mean = sum(y_list) / len(y_list)
    return y_mean


# Running this script locally will perform a flyte.run,
# which will deploy your task code to your remote Union/Flyte instance.
if __name__ == "__main__":

    # Establish a remote connection from within your script.
    flyte.init_from_config(".flyte/config.yaml")

    # Run your tasks remotely inline and pass parameter data.
    run_fn = flyte.run(fn, x=11)
    run = flyte.run(main, x_list=list(range(20)))

    # Print various attributes of the run.
    print(f"Run name = {run.name}")
    print(f"Run URL = {run.url}")

    logging.info(run_fn.name)
    logging.info(run_fn.url)

    # Stream the logs from the remote run to the terminal.
    logging.info("Going to wait for run.")
    run.wait(run)
    run.wait(run_fn)
    logging.info("Run completed.")
