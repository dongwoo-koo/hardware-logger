# Hardware logger

## Introduction
: Detect hardware information(**Temperature** and **Utilization** of **CPU** and **GPU**) and save them.   

* Example
```csv
# log_20210922-142054.csv
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Boot time:,2021/09/22/ 14:20:54
GPU count:,2
 - GPU-0 model:, GeForce RTX 2080 Ti
 - GPU-1 model:, GeForce GTX 1080 Ti
Time,CPU temp[°C],CPU utilization[%],GPU-0 temp[°C],GPU-0 utilization[%],GPU-0 utilization.memory[%],GPU-1 temp[°C],GPU-1 utilization[%],GPU-1 utilization.memory[%]
2021/09/22/ 14:20:54,34.75,13.8, 36, 8 %, 3 %, 29, 0 %, 0 %
2021/09/22/ 14:20:55,27.875,1.8, 36, 5 %, 3 %, 29, 0 %, 0 %
2021/09/22/ 14:20:57,27.875,0.9, 35, 2 %, 2 %, 29, 0 %, 0 %
2021/09/22/ 14:20:58,27.875,1.3, 35, 2 %, 2 %, 29, 0 %, 0 %
2021/09/22/ 14:20:59,37.0,12.7, 36, 22 %, 4 %, 29, 0 %, 0 %
2021/09/22/ 14:21:00,29.0,6.6, 36, 18 %, 3 %, 29, 0 %, 0 %
```

## Environments
* OS: Ubuntu 18.04
* Modules installation
  ```shell
  # $ pip install psutil
  $ pip install nvidia-smi
  $ pip install py-cpuinfo
  ```

## HOW-TO-USE
```shell
$ python3 hardware_logger.py
```

## Features
- [x] Check current time
- [x] Log cpu temperature, utilization
- [x] Log gpu temperature, utilization
- [x] Save as csv file
- [ ] Detect hardware information
- [ ] Send via email

## Reference
**Documents**
 - https://psutil.readthedocs.io/en/latest/index.html?highlight=temperature#psutil.sensors_temperatures
 - https://nvidia.custhelp.com/app/answers/detail/a_id/3751/~/useful-nvidia-smi-queries

**Blog**
 - https://www.thepythoncode.com/article/get-hardware-system-information-python

**GitHub**
 - https://github.com/nzkozar/sys-temp-logger/blob/master/temp-log.py
 - https://github.com/panch13114/gpumonitor/blob/master/gpumonitor