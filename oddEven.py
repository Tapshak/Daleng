def odd(*args):
    Even_num = [n for n in args if n%2 ==0]
    odd_num = [n for n in args if n%2 ==1]
    return f'Even_num: {Even_num}\nOdd_num: {odd_num}'
output = odd(1,2,3,4,5,6,7,8,9,10)
print(output)
    