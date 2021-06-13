
#wartości
x_input = [1,0.5,0.2]
#Wagi dla każdej z ocen powyżej od 1 do 3
w_weights = [0.4, 0.3, 0.6]
#Wartość graniczna do przejścia przez granicę
threshold = 0.5

def step(weighted_sum):
    if weighted_sum > threshold:
        return 1
    else:
        return 0

def perceptron():
    weighted_sum = 0
    #Każdą wartość z dwóch array mnoży przez siebie drukuje i dodaje do smumy po kolei. jeśli suma wyjdzie > niż threshold to 1
    for x,w in zip(x_input, w_weights):
        weighted_sum +=x*w
        print(weighted_sum)
    return step(weighted_sum)

output = perceptron()
print("output: " + str(output))