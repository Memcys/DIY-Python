# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py:light,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.0
#   kernelspec:
#     display_name: Python 3.8.3 64-bit
#     language: python
#     name: python38364bita14c50cabb94433e97ec307454e1294b
# ---

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.style.use(['seaborn-darkgrid', 'seaborn-talk'])

def logistic(a, x):
    '''
    Return ax(1-x)use   '''
    return np.multiply(np.multiply(a, x), (1 - x))


# Logistic
# Error tolerence
err_tol = 1e-4
# Parameters
a = float(input("请输入参数 a (0<a<4):"))
# Initial value of x0
initX = float(input("请输入参数 x0 (0<=x0<=1):"))

print("\n正在计算 Logistic 图……")
# The function lines
x = np.linspace(0, 1)
y1 = logistic(a, x)
y2 = x

# The step lines
stepX = [initX]
stepY = [logistic(a, initX)]

i = 0
while np.abs(stepX[i] - stepY[i]) >= err_tol:
    stepX.append(stepY[i])
    i += 1
    stepY.append(logistic(a, stepX[i]))
print("Logistic 图计算完成。")

# Feigenbaum
# # Error tolerence
err_tol = 1e-6
alist = np.linspace(2.6, 4, num=1000)
initX = 0.6

# The step lines
Xn = initX
Dict = {}

print("正在计算 Feigenbaum 图……")

for a in alist:
    # print("a = ", a)
    Yn = np.array([logistic(a, initX)])
    
    i = 0
    while np.abs(Xn - Yn[i]) >= err_tol:
        Xn = Yn[i]
        next = logistic(a, Xn)
        
        if (np.abs(next - Yn) < err_tol).any():
            i, = np.where(np.abs(next - Yn) < err_tol)
            i = np.array(i)[0]
            break
        else:
            Yn = np.append(Yn, next)
            i += 1
            # print("i = {}, Yn = {}".format(i, Yn))
    Dict[a] = Yn[i:]
    # print("\tX = ", Dict[a])
print("Feigenbaum 图计算完成。")

print("正在绘图……")

# The Logistic plot
fig, ax = plt.subplots(tight_layout=True)

ax.annotate("$a = {}, \qquad x_0 = {}$".format(a, initX), xy=(0.5, 0.8), xycoords='figure fraction', horizontalalignment='center', verticalalignment='top',)

ax.plot(x, y1)
ax.plot(x, y2)
ax.step(stepX, stepY, where='post', alpha=0.5,)
ax.plot(stepX, stepY, 'C2o', alpha=0.37, markersize=4)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
    #    title='About as simple as it gets, folks')
ax.grid()

# Save the plot
fig.savefig("../Images/Logistic.pdf")


# The Feigenbaum plot
aPlot = [a for a, data in zip(Dict, Dict.values()) for j in data]
yPlot = [val for data in Dict.values() for val in data]

fig2, ax2 = plt.subplots(tight_layout=True)

# colors = cm.Set2(np.linspace(0, 1, len(aPlot)))
ax2.scatter(aPlot, yPlot, marker='.', s=1,# c=colors
            )
ax2.grid()

# Save and show the plot
fig2.savefig("../Images/Feigenbaum.pdf")

plt.show()
