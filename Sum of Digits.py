number=int(input("Enter the Number : "))
def sum_of_digits(number):
    s=0
    while(number!=0):
        s=s + (number%10)
        number=number//10
    return s

print(sum_of_digits(number))

