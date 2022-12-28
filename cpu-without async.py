import matplotlib.pyplot as plt
import psutil
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Temperature (°C)')

def get_cpu_temperature():
    temperatures = psutil.sensors_temperatures()
    return sum(temperatures['cpu-thermal'].values()) / len(temperatures['cpu-thermal'])

def update_graph(num):
    temperature = get_cpu_temperature()
    x_data.append(num)
    y_data.append(temperature)
    ax.plot(x_data, y_data, 'r')

x_data, y_data = [], []
ani = FuncAnimation(fig, update_graph, interval=1000)
plt.show()
