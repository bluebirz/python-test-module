# python-test-module

## about

- This repo is for documenting testing modules in Python that are `unittest` and `pytest`.
- It is written aside blogs described below.

## blog related

- [EN] [Python testing - module pytest](https://www.bluebirz.net/en/python-testing-pytest/)
- [TH] [Python testing - มารู้จัก module pytest](https://www.bluebirz.net/th/python-testing-pytest-th/)
- [Medium] [Python testing — module unittest](https://medium.com/@bluebirz/python-testing-module-unittest-1fd6dae52ebf)

## How to run

### Prerequisites

- install `requirements.txt` via
  
  ```bash
  pip install -r requirements.txt
  ```

- run test script in `tests/my-unittest` using

    ```bash
    python3 tests/my-unittest/<file.py>
    ```

- run test script in `tests/my-pytest` using

    ```bash
    pytest <flag> tests/my-unittest/<file.py>
    ```
