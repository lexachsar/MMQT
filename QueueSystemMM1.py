public class QueueSystemMM1 {
        // Число обслуживающих приборов в СМО.
        private Integer k;
        // Интенсивность входящего потока требований.
        private Double lambda;
        // Интенсивность обслуживания требований одним прибором.
        private Double mu;
        // Коэффициент использования обслуживающих приборов системы (коэффициент загрузки).
        private Double psi;

        /**
         * Функция задает параметр psi
         * @return Коэффициент использования обслуживающих приборов системы (коэффициент загрузки).
         */
        private Double setPsi() {
            this.psi = lambda / mu;

            return this.psi;
        }

        // Число требований в системе (с. в.).
        private Double n;
        // Математическое ожидание числа требований в системе.
        private Double Mn;
        // Число требований в очереди.
        private Double b;
        // Математическое ожидание числа требований в очереди.
        private Double Mb;
        // Математическое ожидание числа свободных приборов.
        private Double Mg;
        // Мат. ожидание числа занятых приборов.
        private Double Mh;
        // Мат. ожидание длительности пребывания требований в системе.
        private Double Mu;
        // Мат. ожидание длительности обслуживания одним прибором.
        private Double Mv;
        // Мат. ожидание длительности пребывания требования в очереди.
        private Double Mw;

        /**
         * @param n Ровно n требований.
         * @return Стационарная вероятность пребывания в системе ровно n требований.
         */
        private Double getP_n(int n) {
            return ( (1 - psi) * Math.pow(psi, n) );
        }

        /**
         * @return Математическое ожидание числа требований в системе.
         */
        private Double getMn() {
            return ( psi / (1 - psi) );
        }

        /**
         * @return Математическое ожидание числа требований в очереди.
         */
        private Double getMb() {
            return ( ( psi * psi ) / (1 - psi) );
        }

        /**
         * @return Мат. ожидание длительности пребывания требований в системе.
         */
        private Double getMu() {
            return ( 1 / ( mu * (1 - psi) ) );
        }

        private boolean isSystemStable() {
            if(lambda < mu) {
                return true;
            }
            else {
                return false;
            }
        }

        private void updateQueueSystem(Double lambda, Double mu) {

        }

        QueueSystemMM1(Double lambda, Double mu) {
            this.lambda = lambda;
            this.mu = mu;
            this.setPsi();
        }
}
