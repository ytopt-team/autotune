from collections import OrderedDict

class Space:
    """Create a new Space instance.

    Args:
        json (str, optional): Create a space from a JSON representation. Defaults to None.

    >>> from autotune import Space
    >>> TaskSpace = Space(
            matrix=[“boyd1.mtx”] # Example of Discrete non-ordinal OR Categorical
            )
    >>> InputSpace = Space(
            COLPERM=(1, 5), # Example of Discrete ordinal
            …,
            )
    """

    def __init__(self, json: str=None, **kwargs):
        self.space = OrderedDict()
        if not json is None:
            self.from_json(json)
        else:
            self._init_space(**kwargs)

    def _init_space(self, **kwargs):
        for dim_name in kwargs:
            self.add_dim(dim_name, dim_range=kwargs[dim_name])

    def add_dim(self, dim_name: str, dim_range):
        self.check_dim(dim_name, dim_range)
        self.space[dim_name] = dim_range

    @staticmethod
    def check_dim(dim_name, dim_range):
        assert type(dim_name) is str
        assert type(dim_range) is list or type(dim_range) is tuple

    def to_json(self):
        """Convert a Space instance to a JSON representation.

        Return:
            str: a JSON representation of the Space.
        """

    def from_json(self, json: str):
        """Initialize a Space from a JSON representation.
        """

