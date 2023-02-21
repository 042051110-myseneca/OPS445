#!/usr/bin/env python3

#Author: Narenth Nimalan
#Author ID: nnimalan
#Date Created: 2022/09/23

import sys




timer = int(sys.argv[1]) if len(sys.argv) >= 2 else 3

while timer != 0:
    print(timer)
    timer -=  1
print('blast off!')
