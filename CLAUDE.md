# AIdventure Project Guidelines

## Build Commands
- Install dependencies: `uv install`
- Run project: `crewai run`
- Run single test: `python tests/test_crew.py`

## Test Commands
- Test crew: `python tests/test_crew.py`
- Test VLLMs: `python tests/test_v_llm.py`
- Test Azure: `python tests/test_azure.py`

## Scripts
- Latest AI development: `python -m src.latest_ai_development.main`
- Run crew: `python -m src.alg.crew`
- Test crew: `python -m src.alg.main --iterations=5 --model=gpt-4`

## Code Style
- Python >=3.10, <3.13
- Use type hints for all functions and classes
- PascalCase for classes, snake_case for functions/variables
- Imports: stdlib → third-party → local (grouped with blank lines)
- Error handling: use try/except with specific error messages
- Config in YAML format (see src/*/config/*.yaml)
- Environment variables for configuration and API keys