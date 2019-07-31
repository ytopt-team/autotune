from .space import Space
from typing import Callable, List

# Custom types

class TuningProblem:
    """

    Args:
        task_space (Space): the task space represents the set of problems you want to solve.
        input_space (Space): the input space represents a space of parameters you want to optimize for a particular problem. Given a choice in the task space you want to find the optimal set of parameters in the input space.
        objective (Callable): a function wich returns a single scalar or a tuple of scalar values.
        constraints (str, Callable, optional): if str then it is ... if a Callable then it is .... Defaults to None.
        model (...): an analytical model. Defaults to None.
        name (str, optional): A name corresponding to the TuningProblem. Defaults to None.

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
    >>> problem = TuningProblem(task_space, input_space, output_space, myobj, cst, model)
    """

    def __init__(self,
        task_space: Space,
        input_space: Space,
        output_space: Space,
        objective: Callable,
        constraints=None,
        model=None,
        name=None,
        **kwargs):

        self.name = name
        self.task_space = task_space
        self.input_space = input_space
        self.output_space = output_space
        self.objective = objective
        self.constraints = constraints
        self.model = model