from .space import Space
from typing import Callable, List

# Custom types
Constraint = Callable[[dict], bool]
Constraints = List[Constraint]
Objective = Callable[[dict], bool]

class TuningProblem:
    """
    >>> from autotune import TuningProblem
    >>> from autotune.space import *
    >>> task_space = Space([
    ...     Categorical(["boyd1.mtx"], name="matrix")
    ... ])
    >>> input_space = Space([
    ...     Integer(10, 100, name="m"),
    ...     Integer(10, 100, name="n")
    ... ])
    >>> def myobj(point):
    ...     return point['m']
    >>> problem = TuningProblem(task_space, input_space, myobj)
    """

    def __init__(self, task_space: Space, input_space: Space, objective: Objective, constraints: Constraints=[], name=None,  **kwargs):
        self.name = name
        self.task_space = task_space
        self.input_space = input_space
        self.objective = objective
        self.constraints = constraints[:]