import numpy as np
from LinearRegression import LinearRegression


# Creamos el DataSet
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 6, 9, 12, 15])

# Creamos la instancia de LinearRegression
model = LinearRegression(X, y)

# Obtenemos la ecuación de regresión y la imprimimos
equation = model.get_equation()
print(equation)

# Predecimos el valor de Y para un valor X de entrada y lo imprimimos
x_input = np.array([[6]])
y_pred = model.predict(x_input)
print(f"El valor predicho de Y para X={x_input[0][0]} es {y_pred}")

# Obtenemos el R-squared y lo imprimimos
r_squared = model.get_r_squared()
print(r_squared)