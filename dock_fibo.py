start_num = int(input('Enter starting number:'))
end_num = int(input('Enter ending number:'))

count = 0
first_fibo = 0
second_fibo = 1
third_fibo = 1

fibo_nums = []

while True:
    third_fibo = second_fibo
    second_fibo = first_fibo
    first_fibo = first_fibo + third_fibo
    if first_fibo >= start_num and first_fibo <= end_num:
        fibo_nums.append(first_fibo)

    if(first_fibo > end_num):
        break

print('\nThe {} Fibonacci numbers between {} and {} are:'.format(len(fibo_nums),start_num,end_num))
result = ''
for x in fibo_nums:
    result = '{} {}'.format(result,x)

print(result)
