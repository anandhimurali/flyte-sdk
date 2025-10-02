# flyte-poc
Testing Flyte

- Union.ai Docs: https://www.union.ai/docs/v2/byoc/user-guide/getting-started/running/
- Flyte Git: https://github.com/flyteorg
- Flyte Docs: https://docs-legacy.flyte.org/en/latest/index.html

## Local Setup
- https://www.union.ai/docs/v2/flyte/user-guide/getting-started/local-setup/
- https://docs.astral.sh/uv/getting-started/installation/

```
uv python3 install 3.13
uv python3 pin 3.13 --global

uv venv
source .venv/bin/activate
uv pip install --no-cache --prerelease=allow --upgrade flyte
uv pip show flyte
```
