class Search:
    def __init__(self, problem, parameters):
        self.problem = problem
        self.parameters = parameters

    def run(self):
        if self.parameters['method'] == 'ambs':
            self.parameters.pop('method')
            from ytopt.search.ambs import AMBS
            search = AMBS(problem=self.problem, **self.parameters)
            search.main()
