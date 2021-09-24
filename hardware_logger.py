# -*- coding:utf-8 -*-

import os
import csv
import time
import datetime

import psutil
import cpuinfo


def get_time(flatten=True):
    now = datetime.datetime.today()
    if flatten:
        return f'{now.year}{now.month:02d}{now.day:02d}-{now.hour:02d}{now.minute:02d}{now.second:02d}'
    else:
        return f'{now.year}/{now.month:02d}/{now.day:02d}/ {now.hour:02d}:{now.minute:02d}:{now.second:02d}'


def check_cpu_temp():
    temps = psutil.sensors_temperatures()

    core_temps = temps['coretemp'][1:]
    current_temps = []
    for core_temp in core_temps:
        current_temp = core_temp.current
        current_temps.append(current_temp)
    return sum(current_temps) / float(len(current_temps))


# Create log file
log_file_name = f'./log/log_{get_time()}.csv'
log_file = open(log_file_name, 'a', encoding='utf-8')
log_file_writer = csv.writer(log_file)

# Boot time check
log_file_writer.writerow(['Boot time:', get_time(flatten=False)])

# CPU check
cpu = cpuinfo.get_cpu_info()
cpu_model = cpu['brand_raw']
log_file_writer.writerow(['CPU model:', cpu_model])

# GPU check
p_result = os.popen(
    'nvidia-smi \
    --query-gpu=index,name \
    --format=csv,noheader'
)
gpus = p_result.readlines()
log_file_writer.writerow(['GPU count:', len(gpus)])
for gpu in gpus:
    gpu = gpu[:-1].split(',')
    gpu_index, gpu_name = gpu[0], gpu[1]
    log_file_writer.writerow([f' - GPU-{gpu_index} model:', gpu_name])

# Header
log = ['Time', 'CPU temp[°C]', 'CPU utilization[%]']
for index, gpu in enumerate(gpus):
    log.append(f'GPU-{index} temp[°C]')
    log.append(f'GPU-{index} utilization[%]')
    log.append(f'GPU-{index} utilization.memory[%]')
log_file_writer.writerow(log)
log_file.close()
time.sleep(1)

# Check state in loop
while True:
    log_file = open(log_file_name, 'a', encoding='utf-8')
    log_file_writer = csv.writer(log_file)

    now = get_time(flatten=False)
    cpu_temp = check_cpu_temp()
    cpu_utilization = psutil.cpu_percent()
    log = [now, cpu_temp, cpu_utilization]

    presult = os.popen(
        'nvidia-smi \
        --query-gpu=index,name,temperature.gpu,utilization.gpu,utilization.memory \
        --format=csv,noheader'
    )
    gpus = presult.readlines()
    for gpu in gpus:
        gpu = gpu[:-1].split(',')
        gpu_temp, gpu_utilization, gpu_utilization_memory = gpu[2], gpu[3], gpu[4]
        log.append(gpu_temp)
        log.append(gpu_utilization)
        log.append(gpu_utilization_memory)
    log_file_writer.writerow(log)
    log_file.close()
    time.sleep(1)
