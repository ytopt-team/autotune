from autotune import Space, TuningProblem

task_space = Space(
    matrix=["boyd1.mtx"]
)

input_space = Space(
    m=(10, 100),
    n=(10, 100)
)

problem = TuningProblem(task_space, input_space)


print('problem.to_json: ', problem.to_json(), end='\n')

problem_copy = TuningProblem(json_repr=problem.to_json())
print(problem_copy)