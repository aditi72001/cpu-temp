import wmi
import matplotlib.pyplot as plt
import asyncio

wmi_service = wmi.WMI()
cpu_temps = []

async def get_cpu_temp():
    while True:
        temp = wmi_service.Win32_TemperatureProbe()[0].CurrentReading
        cpu_temps.append(temp)
        await asyncio.sleep(1)

async def plot_temp():
    plt.ion()
    fig, ax = plt.subplots()
    while True:
        ax.clear()
        ax.plot(cpu_temps)
        fig.canvas.draw()
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(get_cpu_temp(), plot_temp())

asyncio.run(main())
plt.show()