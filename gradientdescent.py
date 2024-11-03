import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return (x + 3) ** 2

def derivative(x):
    return 2 * (x + 3)

def gradient_descent(starting_x, learning_rate, num_iterations):
    x = starting_x
    history = []  # To store x values for visualization

    for i in range(num_iterations):
        grad = derivative(x)  # Compute the gradient
        x = x - learning_rate * grad  # Update x
        history.append(x)  # Store x for plotting

    return x, history

starting_x = 2  # Starting point
learning_rate = 0.1  # Learning rate
num_iterations = 50  # Number of iterations

final_x, history = gradient_descent(starting_x, learning_rate, num_iterations)
print(f"Local minima found at x = {final_x}")

x_values = np.linspace(-10, 5, 100)
y_values = function(x_values)

plt.plot(x_values, y_values, label='y = (x + 3)^2')
plt.scatter(history, [function(x) for x in history], color='red', label='Gradient Descent Path', zorder=5)
plt.title('Gradient Descent Optimization')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
