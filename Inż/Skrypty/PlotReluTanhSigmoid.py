import numpy as np
import matplotlib.pyplot as plt

# Definicje funkcji
def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

# Zakres dla wykresów
x = np.linspace(-5, 5, 100)

# Rysowanie funkcji ReLU
plt.figure()
plt.plot(x, relu(x), label='ReLU')
# plt.title('ReLU Function')
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.grid(True)
plt.savefig('relu.png')  # Zapisanie wykresu jako obraz PNG

# Rysowanie funkcji Sigmoid
plt.figure()
plt.plot(x, sigmoid(x), label='Sigmoid')
# plt.title('Sigmoid Function')
plt.xlabel('x')
plt.ylabel('Sigmoid(x)')
plt.grid(True)
plt.savefig('sigmoid.png')  # Zapisanie wykresu jako obraz PNG

# Rysowanie funkcji Tanh
plt.figure()
plt.plot(x, tanh(x), label='Tanh')
# plt.title('Tanh Function')§
plt.xlabel('x')
plt.ylabel('Tanh(x)')
plt.grid(True)
plt.savefig('tanh.png')  # Zapisanie wykresu jako obraz PNG

# Informacja zwrotna o zapisanych obrazach
print('Wykresy funkcji zostały zapisane jako obrazy PNG.')
