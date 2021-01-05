#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 05:23:09 2020

@author: mario_hevia
"""


import math
import matplotlib.pyplot as plt
import numpy as np

MARKER_SIZE = 8
x = [i for i in range(20,161,20)]
y1 = [373204.462, 6382355.462, 31838617.502, 102952880.498, 273182219.094, 
      534073262.09, 942125071.288, 1724752388.326]
y2 = [22166.946, 439029.896, 2233678.234, 7263028.946, 20943139.522, 
      38750424.592, 75439485.748, 121262733.296]
y3 = [76286.866, 1500572.348, 8194845.866, 27818828.412, 64861963.694, 
      144679697.16, 276386507.11, 408043245]
y4 = [754563.08, 12909381.256, 64926793.376, 233628008.492, 537667438.144, 
      1123831482.816, 2102245141.4, 3575748681.676]
y6 = [41833.7, 811332.412, 4614266.98, 15499276.528, 38071664.076, 
      76303459.272, 135442944.972, 235663887.012]
y7 = [119566.6, 1892519.716, 9419706.692, 27960873.04, 67251935.832, 
      133498511.156, 233612271.252, 362625152.08]
y8 = [28273.712, 77530.268, 125147.012, 276100.324, 470262.176, 625021.144, 
      1037498.008, 1402112.976]
y10 = [95518.764, 1133885.148, 5040926.96, 14067255.648, 34645578.356, 
       73524324.032, 122476875.472, 214309909.672]
y11 = [108964.48, 1840189.788, 8477145.38, 21360793.196, 50517752.088,
       93987943.788, 142863582.58, 260827663.236] #Change!!!!!!!
y12 = [98347.008, 1588493.644, 7333293.968, 18801213.644, 46487825.02, 
       83944136.252, 140103455.604, 224028530.188]

fig = plt.figure(figsize=(13, 10))
ax1 = fig.add_subplot(111)
ax1.set_xlabel('n')
ax1.set_ylabel('Fitness evaluations')
ax1.set_yscale('log')
plt.plot(x, y1, '-', label='(1+1) EA p=1/n', color = "black", marker = "o", markersize=MARKER_SIZE)
plt.plot(x, y2, '-.', label='(1+1) EA p=k/n', color = "black", marker = ".", markersize=MARKER_SIZE)
plt.plot(x, y3, '-', label='(1+1) fEA β=1.5', color = "purple", marker = "s", markersize=MARKER_SIZE)
plt.plot(x, y4, '-', label='Vanilla SA (1+(λ,λ)) GA', color = "green", marker = "^", markersize=MARKER_SIZE)
plt.plot(x, y6, '-.', label='SA (1+(λ,λ)) GA λ_max = k', color = "teal", marker = "+", markersize=MARKER_SIZE)
plt.plot(x, y7, '-', label='(1+(λ,λ)) fGA', color = "darkcyan", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y8, '-', label='Non-standard (1+(λ,λ)) GA', color = "mediumblue", marker = "*", markersize=MARKER_SIZE)
plt.plot(x, y10, '-', label='SA (1+(λ,λ)) GA λ_max = n/2', color = "teal", marker = "P", markersize=MARKER_SIZE)
plt.plot(x, y11, '-', label='SA (1+(λ,λ)) GA reset', color = "red", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y12, '-', label='SA (1+(λ,λ)) GA reset F = (1+1/n)^4', color = "mediumblue", marker = "D", markersize=MARKER_SIZE)

ax1.legend()
plt.show()


x = [i for i in range(2,8)]
y1 = [1048.726, 19785.506, 373204.462, 7042924.108, 130097518.428, 2365827720.934]
y2 = [728.876, 4550.182, 22166.946, 74413.822, 198838.812, 418003.75]
y3 = [1209.076, 11905.998, 76286.866, 364080.112, 1167105.044, 3051183.158]
y4 = [1432.24, 38475.332, 754563.08, 13422600.32, 265444327.308, 5145204312.076]
y6 = [1112.228, 7968.364, 41833.7, 150040.052, 394824.636, 868727.564]
y7 =[1041.812, 13895.636, 119566.6, 592232.984, 2078403.6, 5497445.96]
y8 =[866.628, 5316.204, 28273.712, 132258.84, 435676.032, 1327034.068]
y10 = [612.24, 7246.348, 95518.764, 1005765.54, 2054036.228, 2294589.336]
y11 = [817.436, 10594.036, 108964.48, 544529.548, 1647562.036, 3389188.764]
y12 = [770.828, 10692.168, 98347.008, 550308.304, 1722752.876, 3333343.844]


fig = plt.figure(figsize=(13, 10))
ax1 = fig.add_subplot(111)
ax1.set_xlabel('k')
ax1.set_ylabel('Fitness evaluations')
ax1.set_yscale('log')
#ax1.set_ylim(bottom=0.9, top=1.2)
#plt.plot(x, y, 'b-', label='en (log(n/2)')
plt.plot(x, y1, '-', label='(1+1) EA p=1/n', color = "black", marker = "o", markersize=MARKER_SIZE)
plt.plot(x, y2, '-.', label='(1+1) EA p=k/n', color = "black", marker = ".", markersize=MARKER_SIZE)
plt.plot(x, y3, '-', label='(1+1) fEA β=1.5', color = "purple", marker = "s", markersize=MARKER_SIZE)
plt.plot(x, y4, '-', label='Vanilla SA (1+(λ,λ)) GA', color = "green", marker = "^", markersize=MARKER_SIZE)
plt.plot(x, y6, '-.', label='SA (1+(λ,λ)) GA λ_max = k', color = "teal", marker = "+", markersize=MARKER_SIZE)
plt.plot(x, y7, '-', label='(1+(λ,λ)) fGA', color = "darkcyan", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y8, '-', label='Non-standard (1+(λ,λ)) GA', color = "mediumblue", marker = "*", markersize=MARKER_SIZE)
plt.plot(x, y10, '-', label='SA (1+(λ,λ)) GA λ_max = n/2', color = "teal", marker = "P", markersize=MARKER_SIZE)
plt.plot(x, y11, '-', label='SA (1+(λ,λ)) GA reset', color = "red", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y12, '-', label='SA (1+(λ,λ)) GA reset F = (1+1/n)^4', color = "mediumblue", marker = "D", markersize=MARKER_SIZE)

ax1.legend()
plt.show()


x = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
y1 = [1056.384, 7387.342, 16647.02, 27227.954, 37664.816, 48031.826, 59570.602, 70718.042, 81998.508, 92614.37, 106653.922]
y1 = [j/(x[i]*math.log(x[i],2)) for i,j in enumerate(y1)]
y2 = [3680.49, 27074.94, 64429.324]
y2 = [j/(x[i]*math.log(x[i],2)) for i,j in enumerate(y2)]
y3 = [1717.658, 12648.058, 29136.96, 46907.434, 64148.966, 85270.268, 103859.658, 122247.712, 145477.602, 164166.444, 186430.882]
y3 = [j/(x[i]*math.log(x[i],2)) for i,j in enumerate(y3)]
y4 = [902.756, 4795.032, 9754.056, 14764.832, 19724.056, 24657.196, 29703.02, 34765.912, 39652.652, 44769.64, 49754.14]
y4 = [j/(x[i]*math.log(x[i],2)) for i,j in enumerate(y4)]
y6 = [1009.18, 6133.92, 13415.496]
y6 = [j/(x[i]*math.log(x[i],2)) for i,j in enumerate(y6)]
y7 = [1283.648, 7924.38, 16620.416, 25640.604, 35014.452, 44219.156, 53513.304, 62839, 72002.796, 81316.908, 91084.944]
y7 = [j/(x[i]*math.log(x[i],2)) for i,j in enumerate(y7)]
y8 = [6295.564, 59405.88, 133185.212, 206033.236, 295626.236, 409708.768, 500921.588, 611473.64, 735974.072, 840627.488, 969319.216]
y8 = [j/(x[i]*math.log(x[i],2)) for i,j in enumerate(y8)]
y10 = [898.992, 4782.716, 9747.704, 14713.464, 19680.708, 24688.412, 29715.432, 34830.344, 39804.524, 44829.936, 49784.032]
y10 = [j/(x[i]*math.log(x[i],2)) for i,j in enumerate(y10)]
y11 = [895.264, 4812.912, 9742.18, 14699.828, 19776.284, 24713.38, 29726.836, 34695.088, 39710.844, 44670.848, 49710.312]
y11 = [j/(x[i]*math.log(x[i],2)) for i,j in enumerate(y11)]
y12 = [1145.768, 6962.924, 14843.768, 23005.736, 31171.92, 39883.912, 48367.336, 57138.284, 65756.964, 74436.104, 83379.9]
y12 = [j/(x[i]*math.log(x[i],2)) for i,j in enumerate(y12)]

fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(121)
ax1.set_xlabel('n')
ax1.set_ylabel('Fitness evaluations/ $n \log n$')
# ax1.set_yscale('log')
#ax1.set_ylim(bottom=0.9, top=1.2)
#plt.plot(x, y, 'b-', label='en (log(n/2)')
plt.plot(x, y1, '-', label='(1+1) EA p=1/n', color = "black", marker = "o", markersize=MARKER_SIZE)
plt.plot(x, y3, '-', label='(1+1) fEA β=1.5', color = "purple", marker = "s", markersize=MARKER_SIZE)
plt.plot(x, y4, '-', label='Vanilla SA (1+(λ,λ)) GA', color = "green", marker = "^", markersize=MARKER_SIZE)
plt.plot(x, y7, '-', label='(1+(λ,λ)) fGA', color = "darkcyan", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y8, '-', label='Non-standard (1+(λ,λ)) GA', color = "mediumblue", marker = "*", markersize=MARKER_SIZE)
plt.plot(x, y10, '-', label='SA (1+(λ,λ)) GA λ_max = n/2', color = "teal", marker = "P", markersize=MARKER_SIZE)
plt.plot(x, y11, '-', label='SA (1+(λ,λ)) GA reset', color = "red", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y12, '-', label='SA (1+(λ,λ)) GA reset F = (1+1/n)^4', color = "mediumblue", marker = "D", markersize=MARKER_SIZE)
ax1.legend()

ax2 = fig.add_subplot(122)
ax2.set_xlabel('n')
ax2.set_ylabel('Fitness evaluations/ $n \log n$')
plt.plot(x, y1, '-', label='(1+1) EA p=1/n', color = "black", marker = "o", markersize=MARKER_SIZE)
plt.plot(x, y3, '-', label='(1+1) fEA β=1.5', color = "purple", marker = "s", markersize=MARKER_SIZE)
plt.plot(x, y4, '-', label='Vanilla SA (1+(λ,λ)) GA', color = "green", marker = "^", markersize=MARKER_SIZE)
plt.plot(x, y7, '-', label='(1+(λ,λ)) fGA', color = "darkcyan", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y10, '-', label='SA (1+(λ,λ)) GA λ_max = n/2', color = "teal", marker = "P", markersize=MARKER_SIZE)
plt.plot(x, y11, '-', label='SA (1+(λ,λ)) GA reset', color = "red", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y12, '-', label='SA (1+(λ,λ)) GA reset F = (1+1/n)^4', color = "mediumblue", marker = "D", markersize=MARKER_SIZE)

plt.show()


x = [0, 1, 2, 3, 4, 5]
y1 = [88908.934, 716163.618, 160110.03, 1307253.192, 331334.896, 641133.162]
y2 = [18093.408, 13355.294, 2418.22, 29681.348, 669.002, 718.764]
y3 = [209390.276, 1337203.972, 368096.84, 2382378.744, 533.828, 501217.72]
y4 = [30051.468, 45624.088, 10661.888, 82301.716, 630.412, 949.66]
y5 = [47368.22, 1913.136, 1764.604, 2383.508, 1686.148, 1632.6]
y6 = [93250.46, 227396.448, 43089.5, 438579.332, 533.316, 13914.18]
y7 = [76345.364, 74364.276, 20846.144, 124732.316, 534.012, 834.028]
y8 = [28693.412, 66401.784, 16177.88, 128096.872, 738.42, 929.872]

fig = plt.figure(figsize=(13, 10))
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Problem')
ax1.set_ylabel('Fitness evaluations')
ax1.set_yscale('log')
plt.xticks(np.arange(6), labels = ["Partition $n=500$", "WNP 6p", "WNP 3p", "NP 6p", "NP 5p", "NP 4p"])
plt.plot(x, y1, ' ', label='(1+1) EA p=1/n', color = "black", marker = "o", markersize=MARKER_SIZE)
plt.plot(x, y2, ' ', label='(1+1) fEA β=1.5', color = "purple", marker = "s", markersize=MARKER_SIZE)
plt.plot(x, y3, ' ', label='Vanilla SA (1+(λ,λ)) GA', color = "green", marker = "^", markersize=MARKER_SIZE)
plt.plot(x, y4, ' ', label='(1+(λ,λ)) fGA', color = "darkcyan", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y5, ' ', label='Non-standard (1+(λ,λ)) GA', color = "mediumblue", marker = "*", markersize=MARKER_SIZE)
plt.plot(x, y6, ' ', label='SA (1+(λ,λ)) GA λ_max = n/2', color = "teal", marker = "P", markersize=MARKER_SIZE)
plt.plot(x, y7, ' ', label='SA (1+(λ,λ)) GA reset', color = "red", marker = "X", markersize=MARKER_SIZE)
plt.plot(x, y8, ' ', label='SA (1+(λ,λ)) GA reset F = (1+1/n)^4', color = "mediumblue", marker = "D", markersize=MARKER_SIZE)

ax1.legend(loc="upper right", bbox_to_anchor=(1, 0.7) )
plt.show()