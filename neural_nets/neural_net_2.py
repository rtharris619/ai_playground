

def weighted_sum(input, weights):
    assert(len(input) == len(weights))

    output = 0

    for i in range(len(input)):
        output += input[i] * weights[i]

    return output


def neural_network(input, weights):
    pred = weighted_sum(input, weights)
    return pred


def test_neural_network():

    weights = [0.1, 0.2, 0]

    toes = [8.5, 9.5, 9.9, 9.0]
    wlrec = [0.65, 0.8, 0.8, 0.9]
    nfans = [1.2, 1.3, 0.5, 1.0]

    input = [toes[0], wlrec[0], nfans[0]]

    pred = neural_network(input, weights)

    print(pred)
