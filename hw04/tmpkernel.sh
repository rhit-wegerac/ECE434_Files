#!/bin/bash
i2cdetect -y -r 2


cd /sys/class/i2c-adapter/i2c-2
echo tmp101 0x48 > new_device
dmesg -H | tail -3
ls
cd 2-0048/hwmon/hwmon0
while true
do
cat temp1_input
sleep 0.5
done
    

