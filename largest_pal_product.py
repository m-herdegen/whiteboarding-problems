# find the largest palindrom made from the product of two 3-digit numbers

# what kind of output? - number or expression - number
# don't worry about negative numbers
# lower bound: 100
# upper bound: 999

def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

def find_products():
    product = 1
    largest_product = 1
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product > largest_product:
                largest_product = product 

    return largest_product

print(find_products())