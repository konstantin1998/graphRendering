from scipy.optimize import linprog


c = [-2, 0, -1, 1, 1, 1]
a = [
    [1, 0, -1, 0, 0, 0],
    [1, -1, 0, 0, 0, 0],
    [0, 1, 0, -1, 0, 0],
    [0, 0, 1, 0, -1, 0],
    [0, 0, 1, 0, 0, -1]
]
b = [-1 for i in range(len(a))]
bounds = [(1, len(c)) for j in range(len(c))]
bounds[0] = (1, 1)
res = linprog(c=c, A_ub=a, b_ub=b, bounds=bounds)
print(res.x)