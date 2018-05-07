#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy

import matplotlib as mpl
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
mu = numpy.array( [4, 1, 2, 5, 3, 2, 3] )

Mn = []
Mu = []
lambdas0 = []

# Шаг смены lambda_0
step = 0.1
# Интенсивность потока из источника
for lambda0 in numpy.arange(0, 1, step):

    lambdas0.append(lambda0)

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
        lambdai[i] = ( omega[i] / omega[0] ) * lambdai[0]

    # Вывод интенсивностей потоков
    #print(lambdai)

    # Коэффициент использования обслуживающих приборов системы (коэффициент загрузки).
    psi = lambdai / mu

    # Рассчет м.о. числа требований в системе
    Mn.append( psi / ( 1 - psi ) )

    #  Рассчет м.о. длительности пребывания требований в системе
    Mu.append( 1 / ( mu - lambdai ) )

print(Mn)

print(Mu)

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
plt.plot(lambdas0, Mn)
fig.savefig('Mn_lambda0_graph.png')

fig.clear()
plt.plot(lambdas0, Mu)
fig.savefig('Mu_lambda0_graph.png')