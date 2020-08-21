#take a numeric input from user

input = 99
start = 0
fizzorbuzz = []
def counter(start, input):
    while start < input:
        start +=1
    
        if start % 3 == 0 and start % 15 != 0:
            print('fizz')
        elif start % 5 == 0 and start % 15 != 0:
            print('buzz')
        elif start % 15 == 0:
            print('fizzbuzz')
        else:
            print(start)

    

counter(start, input)