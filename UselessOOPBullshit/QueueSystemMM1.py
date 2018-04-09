class QueueSystemMM1:
    # Число обслуживающих приборов в СМО.
    ##private Integer k;
    # Интенсивность входящего потока требований.
    ##private Double lambda;
    # Интенсивность обслуживания требований одним прибором.
    ##private Double mu;
    # Коэффициент использования обслуживающих приборов системы (коэффициент загрузки).
    ##private Double psi;


    # Функция задает параметр psi
    # @return Коэффициент использования обслуживающих приборов системы (коэффициент загрузки).
    @property
    def setPsi(self):
        self.psi = self.lambdaVar / self.mu

        return self.psi

        # Число требований в системе (с. в.).
        ##private Double n;
        # Математическое ожидание числа требований в системе.
        ##private Double Mn;
        # Число требований в очереди.
        ##private Double b;
        # Математическое ожидание числа требований в очереди.
        ##private Double Mb;
        # Математическое ожидание числа свободных приборов.
        ##private Double Mg;
        # Мат. ожидание числа занятых приборов.
        ##private Double Mh;
        # Мат. ожидание длительности пребывания требований в системе.
        # private Double Mu;
        # Мат. ожидание длительности обслуживания одним прибором.
        # private Double Mv;
        # Мат. ожидание длительности пребывания требования в очереди.
        # private Double Mw;

        # @param n Ровно n требований.
        # @return Стационарная вероятность пребывания в системе ровно n требований.

    def getP_n(self, n):
        return (1 - self.psi) * pow(self.psi, n)

        # @return Математическое ожидание числа требований в системе.

    def getMn(self):
        return self.psi / (1 - self.psi)

    # @return Математическое ожидание числа требований в очереди.
    def getMb(self):
        return (self.psi * self.psi) / (1 - self.psi)

        # @return Мат. ожидание длительности пребывания требований в системе.

    def getMu(self):
        return 1 / (self.mu * (1 - self.psi))

    def isSystemStable(self):
        if self.lambdaVar < self.mu:
            return True
        else:
            return False

            # def updateQueueSystem(self):

    def _init_(self, lambdaVar, mu):
        self.lambdaVar = lambdaVar
        self.mu = mu
        self.psi = self.setPsi()


    #ToDo - create new constructior with keyboard input
    #def __init__(self):
