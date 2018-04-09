import numpy

from QueueNetwork import QueueNetwork

varTeta = numpy.array([[0, 0.2, 0, 0.8, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0.3, 0, 0.7, 0, 0],
                    [0, 0, 0.3, 0, 0, 0.2, 0.5],
                    [0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0]])

varMu = numpy.array( [4, 1, 2, 5, 3, 2, 3] )

vark = 1
varLambda0 = 0.8


queueNetwork = QueueNetwork(len(varTeta), varLambda0, vark, varMu, varTeta)