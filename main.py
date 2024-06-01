import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter, FuncAnimation

def compare_times():
    size = 1_000_000
    list1 = [np.random.random() for _ in range(size)]
    list2 = [np.random.random() for _ in range(size)]
    array1 = np.random.random(size)
    array2 = np.random.random(size)

    start_time = time.perf_counter()
    result_list = [list1[i] * list2[i] for i in range(size)]
    end_time = time.perf_counter()
    print(f"Время выполнения для стандартных списков: {end_time - start_time:.6f} секунд")

    start_time = time.perf_counter()
    result_array = np.multiply(array1, array2)
    end_time = time.perf_counter()
    print(f"Время выполнения для массивов NumPy: {end_time - start_time:.6f} секунд")

def process_data2():
    data = pd.read_csv("data2.csv")
    column_data = data.iloc[:, 1]

    plt.figure(figsize=(10, 6))
    plt.hist(column_data, bins=16, edgecolor='black')
    plt.title('Гистограмма данных из столбца 2')
    plt.xlabel('Значения')
    plt.ylabel('Частота')
    plt.show()

    std_deviation = np.std(column_data)
    print(f"Среднеквадратическое отклонение: {std_deviation:.6f}")

def plot_3d():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(x ** y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')

    ax.set_title('3D график z = sin(x^y)')
    ax.set_xlabel('X ось')
    ax.set_ylabel('Y ось')
    ax.set_zlabel('Z ось')
    plt.show()

def animate_sin():
    x = np.linspace(-10, 10, 1000)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(-10, 10)
    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Анимация функции y = sin(x)')

    line, = ax.plot([], [], lw=2)

    def animate(i):
        x_plot = x[:i]
        y_plot = np.sin(x_plot)
        line.set_data(x_plot, y_plot)
        return line,

    ani = FuncAnimation(fig, animate, frames=len(x), interval=10, blit=True)
    writer = PillowWriter(fps=30)
    ani.save('sin_animation.gif', writer=writer)

if __name__ == "__main__":
    compare_times()
    process_data2()
    plot_3d()
    animate_sin()
