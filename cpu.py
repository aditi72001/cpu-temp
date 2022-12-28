import asyncio
import wmi
import matplotlib.pyplot as plt

async def get_cpu_temp():
    c = wmi.WMI(namespace="root\wmi")
    temperature_info = c.MSAcpi_ThermalZoneTemperature()[0]
    return temperature_info.CurrentTemperature

async def main():
    temperatures = []
    while True:
        temp = await get_cpu_temp()
        temperatures.append(temp)
        plt.plot(temperatures)
        plt.show(block=False)
        plt.pause(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())



