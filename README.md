# Autotuning problem definition interface

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

import collections
from autotune import TuningProblem
from autotune.space import *

from autotune import Search

task_space = Space([Categorical(["boyd1.mtx"], name="matrix")])

input_space = Space([Integer(10, 100, name="m"),
                     Integer(10, 100, name="n")
                     ])

output_space = Space([Real(0.0, inf, name="time")])

def objective(point):
    return point['m'] * point['n']

def analytical_model(point):
    from numpy import log
    return log(point['m']) + log(point['n'] + point['m']*point['n'])

analytical_models = collections.defaultdict(dict)
constraints["boyd1.mtx"]["model1"] = analytical_model

constraints = collections.defaultdict(dict)
constraints["boyd1.mtx"]["cst1"] = ["m > n & m-n > 10"]

starting_points = collections.defaultdict(dict)
starting_points["boyd1.mtx"]["pnt1"] = [15,20]

problem = TuningProblem(task_space, input_space, output_space, objective, constrains, analytical_models)

search_param_dict['method'] = 'surf'
search_param_dict['acq_func'] = 'gp_hedge'
search_param_dict['base_estimator'] = 'RF'
search_param_dict['kappa'] = 1.96
search_param_dict['patience_fac'] = 10 
search_param_dict'n_initial_points'] = 10

search = Search(search_param_dict)


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
