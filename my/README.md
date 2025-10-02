# flyte-poc
Testing Flyte

- Union.ai Docs: https://www.union.ai/docs/v2/byoc/user-guide/getting-started/running/
- Flyte Git: https://github.com/flyteorg
- Flyte Docs: https://docs-legacy.flyte.org/en/latest/index.html

## Local Setup
- https://www.union.ai/docs/v2/flyte/user-guide/getting-started/local-setup/
- https://docs.astral.sh/uv/getting-started/installation/

```
# install
uv python3 install 3.13
uv python3 pin 3.13 --global

uv venv --python 3.13
source .venv/bin/activate
uv pip install -e .
uv pip install --no-cache --prerelease=allow --upgrade flyte
uv pip show flyte

# run
uv run --prerelease allow my/hello_async.py
flyte --config .flyte/config.yaml run my/hello_async.py main
flyte run --local my/hello_async.py main

# build your image
make dist
Python maint_tools/build_default_image.py --registry docker.com/anandhi_murali --name my-flyte-image
```
