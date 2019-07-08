import json
from autotune import Space

class TuningProblem:
    """
    >>> from autotune import Space, TuningProblem
    >>> task_space = Space(
    ...     matrix=["boyd1.mtx"]
    ... )
    >>> input_space = Space(
    ...     m=(10, 100),
    ...     n=(10, 100)
    ... )
    >>> problem = TuningProblem(task_space, input_space)
    >>> problem.to_json()
    '{"task_space": {"matrix": ["boyd1.mtx"], "__space__": true}, "input_space": {"m": [10, 100], "n": [10, 100], "__space__": true}, "constraints": null}'
    >>> problem
    Tuning Problem:
     Task Space:
      * matrix -> ['boyd1.mtx']
     Input Space:
      * m -> (10, 100)
      * n -> (10, 100)
     Constraints: None
    >>> problem_copy = TuningProblem(json_repr=problem.to_json())
    >>> problem_copy
    Tuning Problem:
     Task Space:
      * matrix -> ['boyd1.mtx']
     Input Space:
      * m -> [10, 100]
      * n -> [10, 100]
     Constraints: None
    """

    def __init__(self, task_space=None, input_space=None, constraints=None, json_repr=None, **kwargs):
        if json_repr is None:
            self.problem = dict(
                task_space=task_space,
                input_space=input_space,
                constraints=constraints
            )
        else:
            self.problem = dict()
            self.from_json(json_repr)

    def __repr__(self):
        return f"Tuning Problem:\n Task {self.problem['task_space']}\n Input {self.problem['input_space']}\n Constraints: {self.problem['constraints']}"

    def __str__(self):
        return self.__repr__()

    def from_json(self, json_repr: str):
        self.problem.update(json.loads(json_repr, object_hook=decode_problem))

    def to_json(self):
        return json.dumps(self.problem, cls=ProblemEncoder)


class ProblemEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Space):
            return obj.to_dict()
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

def decode_problem(obj):
    if '__space__' in obj:
        return Space(json_repr=obj)
    return obj