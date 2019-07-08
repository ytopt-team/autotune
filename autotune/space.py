from collections import OrderedDict
import json

class Space:
    """Create a new Space instance.

    Args:
        json_repr (str, optional): Create a space from a JSON representation. Defaults to None.

    >>> from autotune import Space
    >>> task_space = Space(matrix=["boyd1.mtx"])
    >>> task_space
    Space:
      * matrix -> ['boyd1.mtx']
    >>> task_space.to_json()
    '{"matrix": ["boyd1.mtx"], "__space__": true}'
    >>> task_space_copy = Space(json_repr=task_space.to_json())
    >>> task_space_copy
    Space:
      * matrix -> ['boyd1.mtx']
    """

    def __init__(self, json_repr: str=None, **kwargs):
        self.space = OrderedDict()
        if json_repr is None:
            self._init_space(**kwargs)
        else:
            self.from_json(json_repr)

    def _init_space(self, **kwargs):
        for dim_name in kwargs:
            self.add_dim(dim_name, dim_range=kwargs[dim_name])

    def __repr__(self):
        dims = "\n".join([f"  * {name} -> {val}"for name, val in self.space.items()])
        return f"Space:\n{dims}"

    def __str__(self):
        return self.__repr__()

    def add_dim(self, dim_name: str, dim_range):
        self.check_dim(dim_name, dim_range)
        self.space[dim_name] = dim_range

    @staticmethod
    def check_dim(dim_name, dim_range):
        assert type(dim_name) is str
        assert type(dim_range) is list or type(dim_range) is tuple, f"type(dim_range) is {type(dim_range)}"

    def to_json(self):
        """Convert a Space instance to a JSON representation.

        Return:
            str: a JSON representation of the Space.
        """
        return json.dumps(self.to_dict())

    def to_dict(self):
        space_copy = self.space.copy()
        space_copy['__space__'] = True
        return space_copy

    def from_json(self, json_repr):
        """Initialize a Space from a JSON representation.

        Args:
            json_repr (str|dict): a JSON representation of the space.
        """
        if type(json_repr) is str:
            dict_space = json.loads(json_repr)
        else:
            dict_space = json_repr
        dict_space.pop('__space__')
        self._init_space(**dict_space)

