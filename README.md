# replace_me
Template that would allow you run python scripts.  
This includes:
- Dockerfile
- Makefile
- src folder
- Base logging config
- Base lint config
- Base secrets configuration


## How to use this
1. Run `make build` to have a base image
2. Replace all the "replace_me" with the correct values.
3. Add dependencies to the `pyproject.toml`
4. Run `make lock-dependencies` to re build the image
5. Yoy can use the `make terinal` to use a terminal inside the container


## Testing and lint
- `make test` would run all the test on the tests folder
- `make debug test_dir=tests/{file_name}::{test_name}` would allow you to run specific test or files with test
- `make lint` would run `pylint` to find improvements on your code
- `make black` to run `black` and formate your code
