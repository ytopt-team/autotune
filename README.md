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

## Example

```
>>> from autotune import TuningProblem
>>> from autotune.space import *
>>> task_space = Space([
...     Categorical(["boyd1.mtx"], name="matrix")
... ])
>>> input_space = Space([
...     Integer(10, 100, name="m"),
...     Integer(10, 100, name="n")
... ])
>>> output_space = Space([
...     Real(0.0, inf, name="time")
... ])
>>> def myobj(point):
...     return point['m']
>>> def model(point):
...     from numpy import log
...     return log(point['m']) + log(point['n'] + point['m']*point['n'])
>>> cst = "m > n & m-n > 10"
>>> problem = TuningProblem(task_space, input_space, myobj, cst, model)
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
