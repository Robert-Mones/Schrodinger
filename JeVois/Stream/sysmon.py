import psutil
import time

while True:
    cpu = psutil.cpu_percent(percpu=True)
    temp = psutil.sensors_temperatures()["cpu_thermal"][0].current
    mem = psutil.virtual_memory().percent
    print("CPU: {}%, Temp: {}*C, Mem: {}%".format(cpu,temp,mem))
    time.sleep(2)
