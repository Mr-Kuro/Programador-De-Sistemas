# programa aleatório que o prof pediu

def fizzBuzz(parametro):
    for i in range(1, parametro):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizzBuzz(210)