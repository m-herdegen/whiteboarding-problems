# find the largest prime factor of a number

def largest_prime(num):
    div = 2
    while div < num:
        while num % div == 0:
            num = int(num / div)
        
        if num == 1:
            return div

        div += 1

    return div

print(largest_prime(4))