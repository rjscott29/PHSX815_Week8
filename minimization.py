import numpy as np
from scipy.optimize import minimize

def function(x):
    F = (x-1)**2+1
    return F

x0 = np.array([.5])
result = minimize(function, x0)

print(result)