import numpy as np

from QueueSystemMM1 import QueueSystemMM1


class QueueNetwork:
    # Количество систем обслуживания.
    #private Integer L
    # Входящий поток требований(из источника S0).
    #private Double lambda0;
    # Маршруная матрица.
    #private Matrix Teta;
    # Коллекция из Систем Массового Обслуживания.
    #private ArrayList < QueueSystemMM1 > Systems;


    # param L Количество систем обслуживания.
    # param lambda0 Интенсивность входящего потока требований.
    # param k Вектор числа приборов в системах.
    # param mu Вектор интенсивностей обслуживания.
    # param Teta Маршрутная матрица.
    def __init__(self, L, lambda0, k, Mu, Teta):

            self.L = L;
            self.lambda0 = lambda0;
            self.k = k;
            # ToDo - добавить проверку на k
            #if()

            I = np.eye(self.L, dtype=int)

            A = Teta.transpose() - I

            A[L - 1, :] = np.ones(L, dtype=int)

            B = np.zeros(L)
            B[L - 1] = 1

            Omega = np.linalg.solve(A, B)

            self.Lambda = np.zeros(L)
            self.Lambda[0] = lambda0

            print(A)
            print(B)
            print(Omega)

            self.systemCollection = np.zeros(L)
            self.systemCollection[0] = QueueSystemMM1(self.Lambda[0], Mu[0])
            for i in range(1, L):
                self.Lambda[i] = Omega[i] / Omega[0] * self.Lambda[0]
                # Коллекция из Систем Массового обслуживания
                self.systemCollection[i] = QueueSystemMM1(self.Lambda[i], Mu[i])
            print(self.Lambda)





    #ToDo - create new constructior with keyboard input
