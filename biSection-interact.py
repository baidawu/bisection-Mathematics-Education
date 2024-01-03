import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider

# Define the equation
def f(x):
    return x+np.log(x)-3

# Bisection method
def bisection_method(a, b, tol=1e-6, max_iter=100):
    iter_count = 0
    x_values = [a]
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        x_values.append(c)
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return x_values

# Plot the equation
x_values = np.linspace(0, 4, 100)
y_values = f(x_values)

def plot_bisection(iteration):
    roots = bisection_method(2, 3)
    
    plt.figure(figsize=(12, 8))
    plt.plot(x_values, y_values, label='f(x)')
    plt.scatter(roots[:iteration+1], [0]*(iteration+1), color='red', label='Roots')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title(f'Iteration {iteration+1}')
    plt.legend()
    plt.show()

# Use interact function to create an interactive interface
interact(plot_bisection, iteration=IntSlider(min=0, max=20, step=1, value=0))
