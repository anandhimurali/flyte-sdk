import flyte.remote

env = flyte.TaskEnvironment(name="hello_world")

# get remote tasks that were previously deployed
task = flyte.remote.Task.get("hello_world.main", auto_version="latest")
print(task)

@env.task
async def main() -> flyte.File:
    value = await task(13)
    return value
