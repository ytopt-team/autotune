# Autotune

## Installation

From source:

```bash
git clone https://github.com/ytopt-team/autotune.git
cd autotune/
pip install -e .
```

From source with documentation and doctest requirements:

```bash
git clone https://github.com/ytopt-team/autotune.git
cd autotune/
pip install -e '.[docs]'
```

## Documentation

To build and view the documentation:

```bash
cd docs/
make html
open _build/html/index.html
```

## Tests

To run all tests:

```bash
./run_tests.sh
```

To run `doctest`:

```bash
cd docs/
make doctest
```
