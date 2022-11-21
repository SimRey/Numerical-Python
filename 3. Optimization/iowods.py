import numpy as np
from pymoo.core.problem import Problem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_mutation, get_crossover
from pymoo.optimize import minimize
import matplotlib.pyplot as plt


class MyProblem(Problem):

    def __init__(self):
        super(MyProblem, self).__init__(n_var=2,
                                        n_obj=2,
                                        n_constr=2,
                                        xl=np.array([-2, -2]),
                                        xu=np.array([2, 2]))

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = x[:, 0] ** 2 + x[:, 1] ** 2
        f2 = (x[:, 0] - 1) ** 2 + x[:, 1] ** 2

        g1 = 2 * (x[:, 0] - 0.1) * (x[:, 0] - 0.9) / 0.18
        g2 = -20 * (x[:, 0] - 0.4) * (x[:, 0] - 0.6) / 4.8

        out["F"] = np.column_stack([f1, f2])
        out["G"] = np.column_stack([g1, g2])


algorithm = NSGA2(
    pop_size=40,
    n_offsprings=10,
    sampling=get_sampling("real_random"),
    crossover=get_crossover("real_sbx", prob=0.9),
    mutation=get_mutation("real_pm", eta=20),
    eliminate_duplicates=True
)

res = minimize(
    MyProblem(),
    algorithm,
    ('n_gen', 100),
    seed=1,
    verbose=True

)

print(res.X)
print(res.F)

plt.scatter(res.F[:, 0], res.F[:, 1])
plt.show()
