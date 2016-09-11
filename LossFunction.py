import numpy as np
from operator import itemgetter


def lossFunction(creditLine, transactionAmount, pi, actualOutput):
    cutOffs = np.linspace(0.4, 1, num=100)

    losses = np.zeros(100)
    i = 0
    for cutOff in cutOffs:
        print(cutOff)
        j = 0
        for crdLine in creditLine:

            if pi[j] >= cutOff:
                if actualOutput[j] == 0:
                    if crdLine < 2000:
                        losses[i] += 0.02 * 75 + transactionAmount[j] * 0.0075
                    else:
                        losses[i] += 0.05 * 275 + 4 * transactionAmount[j] * 0.005
            else:
                if actualOutput[j] == 1:
                    losses[i] += transactionAmount[j]
            j += 1
        i += 1

    index = min(enumerate(losses), key=itemgetter(1))[0]
    loss = losses[index]
    indices = [i for i, x in enumerate(losses) if abs(x - loss) < 0.001]

    return cutOffs[indices[len(indices) // 2]]

print(lossFunction([1500.0, 3000.0, 2000.0], [50.0, 20.0, 100.0], [.6, 0.7, .8], [0, 0, 1]))
