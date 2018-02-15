## The largest palindrome from the product of two 2-digit number is 9009. 
## Write a function to find the largest palindrome from the product of two 3-digit numbers. 

def is_palindrome(x):
    return str(x) == str(x)[::-1]

def largestPalindrome():
    max_value = 0
    results = []
    for i in range(100,1000):
         for j in range(i,1000):
             product = i * j
             print (i,j,product)
             if product > max_value and is_palindrome(product):
                 max_value = product
                 
    print(max_value)

largestPalindrome()