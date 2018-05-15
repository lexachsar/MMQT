#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

import matplotlib.pyplot as plt

# Количество систем обслуживания
L = 6

# Число приборов в системе
kappa = 1

# Маршрутная матрица
TETA = numpy.array([[0, 0.2, 0, 0.8, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0.3, 0, 0.7, 0, 0],
                    [0, 0, 0.3, 0, 0, 0.2, 0.5],
                    [0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0]])

# Вектор интенсивностей обслуживания
mu = numpy.array([4, 1, 2, 5, 3, 2, 3])

Mn = []
Mu = []
mus1 = []

# Интенсивность потока из источника
lambda0 = 0.2

for mu[1] in range(1, 10):

    mus1.append(mu[1])

    # Создаем единичную матрицу, необходимую для решения системы
    I = numpy.eye(L + 1, dtype=float)

    A = TETA.transpose() - I

    # Заполняем последнюю строчку матрицы A нулями
    A[L, :] = numpy.ones(L + 1, dtype=float)

    # Создаем матрицу-столбец B системы, состоящую из нулей с единицей в нижней строке
    B = numpy.zeros(L + 1, dtype=float)
    B[L] = 1

    # Решаем систему, получаем распределение вероятностей поступления требований в системы
    omega = numpy.linalg.solve(A, B)

    # Создаем матрицу интенсивностей потоков
    lambdai = numpy.zeros(L + 1)
    lambdai[0] = lambda0

    # Рассчет интенсивностей потоков
    for i in range(1, L):
        lambdai[i] = (omega[i] / omega[0]) * lambdai[0]

    # Вывод интенсивностей потоков
    # print(lambdai)

    # Коэффициент использования обслуживающих приборов системы (коэффициент загрузки).
    psi = lambdai / mu

    # Рассчет м.о. числа требований в системе
    Mn.append(psi / (1 - psi))

    #  Рассчет м.о. длительности пребывания требований в системе
    Mu.append(1 / (mu - lambdai))

print(Mn)

print(Mu)

dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
plt.plot(mus1, Mn)
plt.xlabel('mu1')
plt.ylabel('Mn')
fig.savefig('Mn_mu1_graph.png')

fig.clear()
plt.plot(mus1, Mu)
plt.xlabel('mu1')
plt.ylabel('Mu')
fig.savefig('Mu_mu1_graph.png')