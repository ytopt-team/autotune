from numpy import inf
import skopt.space
from skopt.space import *
from skopt.utils import use_named_args
from typing import List

class Space(skopt.space.Space):
    """Create a new Space instance.

    Args:
        space (list, optional): a list of Dimensions.

    >>> from autotune.space import Space, Integer
    >>> task_space = Space([Integer(1, 5, name='max_depth')])
    >>> task_space.to_dict([1])
    {'max_depth': 1}

    """

    def __init__(self, dimensions: List[Dimension] , **kwargs):

        super().__init__(dimensions)

    def to_dict(self, params_list: list) -> dict:

        @use_named_args(self.dimensions)
        def to_params_dict(**params):
            return params

        return to_params_dict(params_list)

    def __len__(self):

        return len(self.dimensions)

    def __getitem__(self, k):

        return self.dimensions[k]

