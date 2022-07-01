# find the sum of even fibonacci numbers up to 4000000

def even_fib(num):
    fib_list = [0,1]
    sum = 0

    while fib_list[-1] <= num:
        fib_list.append(fib_list[-1] + fib_list[-2])
        if fib_list[-1] % 2 == 0:
            sum += fib_list[-1]

    return sum

print(even_fib(4000000))