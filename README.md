# Python starter

This is a modification of [Pamela fox's starter](https://github.com/pamelafox/python-project-template) which is awesome!

This is a template repository for any Python project that uses
[docopt](http://docopt.org/) to create a beautiful command-line
interface. It comes with the following dev tools:

  - `ruff` which identifies many errors and style issues (flake8, isort, pyupgrade)
  - `black` a code formatter
  - pytest for testing
  - pytest-cov to measure code coverage

`ruff` and `black` are run as pre-commit hooks using the pre-commit library. The checks and tests are all run using Github actions on every pull request and merge to main.

## Development instructions

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-dev.txt
pre-commit install # to setup git hook scripts
python3 -m pytest
```

## How to run

- Run program
  ```console
  python src/main.py -h
  ```


## Test
```console
python -m pytest     # regular run
python -m pytest -v  # run verbose
python -m pytest --cov-src tests # run tests with coverage report

```


### Filters

- **Skip** a particular test by decorating the test with `@pytest.mark.skip(reason="...")` and then run `python -m pytest [-v]`
  ```python
  # mytest.py

  @pytest.mark.skip(reason="Not implemented yet")
  def test_booboo:
    assert True
  ```

  ```console
  $ pytest -m pytest [-v]

  ```


- **Only** Run one test by decorating the test with `@pytest.mark.only` and then run `python -m pytest -[v]k only`
  ```python
  @pytest.mark.only
  def test_booboo:
    assert True
  ```

  ```console
  $ pytest -m pytest -k only
  ```
