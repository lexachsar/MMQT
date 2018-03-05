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
    def __init__(self, L, lambda0, k, mu, Teta):
        self.L = L;
        self.lambda0 = lambda0;
        self.k = k;
        self.
