#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 14:32:07 2023

@author: iremguvercin
"""
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20, 6))
area = [48, 30, 20, 15]
priority = ['Low', 'Medium', 'High', 'Critical']
status = ['Resolved', 'Cancelled', 'Pending', 'Assigned']
company = ['IBM', 'Microsoft', 'Tesla', 'Apple']
colors = ['#8BC34A', '#D4E157', '#FFB300', '#FF7043']

# Alt grafiğin düzenini ayarla
plt.subplots_adjust(wspace=0.5, hspace=0.5)

# Alt grafiğin numarasını belirle
subplot_numbers = [1, 2, 3, 4, 5, 6]

# Alt grafiği oluştur ve düzenle
for i, subplot_number in enumerate(subplot_numbers, 1):
    plt.subplot(2, 3, i)
    plt.pie(area, labels=priority if i in [1, 4] else (status if i in [2, 5] else company), colors=colors, startangle=45)
    my_circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)

# Grafiği göster
plt.show()




