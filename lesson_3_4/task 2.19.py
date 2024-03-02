import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot as plt
x0=float(input())
x = np.arrange(-4, 4, 0.001)
y=(x**2) * (x-4)**2 *np.exp (-1*x**2)
solution = minimize(x0)
