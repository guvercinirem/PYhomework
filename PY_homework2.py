#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:22:31 2023

@author: iremguvercin
"""

import matplotlib.pyplot as plt

np1 = range(10)
np2 = range(5, 15)
np3 = range(10, 20)
np4 = range(15, 25)
np5 = range(20, 30)
np6 = range(25, 35)
np7 = range(30, 40)
np8 = range(35, 45)
np9 = range(40, 50)


fig, axs = plt.subplots(3, 3)

axs[0, 0].plot(np1, np2, "r")
axs[0, 1].plot(np1, np3, "b")
axs[0, 2].plot(np1, np4, "g")
axs[1, 0].plot(np5, np2, "y")
axs[1, 1].plot(np6, np2, "rv")
axs[1, 2].plot(np7, np2, "b*")
axs[2, 0].plot(np3, np8, "g-")
axs[2, 1].plot(np3, np9, "yv")
axs[2, 2].plot(np3, np1, "yv")


plt.show()