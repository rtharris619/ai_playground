

def neural_network(input, weight):
    prediction = input * weight
    return prediction


def test_neural_network():
    weight = 0.1
    number_of_toes = [8.5, 9.5, 10, 9]
    input = number_of_toes[0]
    pred = neural_network(input, weight)
    print(pred)
