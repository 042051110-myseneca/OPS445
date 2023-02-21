#!/usr/bin/env python3
#Author ID: nnimalan

import subprocess

p = subprocess.Popen("df -h | egrep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

output = p.communicate()
def free_space():
    stdout = output[0].decode('utf-8').strip()
    return stdout



