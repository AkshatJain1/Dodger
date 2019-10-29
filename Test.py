def FirstFactorial(num):
    if num == 1:
        return 1
    else:
        return num * FirstFactorial(num - 1)


# keep this function call here
num = int(input('Enter a number: '))
ans = FirstFactorial(num)
print('The factorial of' + str(num) + 'is' + str(ans))