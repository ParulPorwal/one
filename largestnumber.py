largest = None
while True :
    num = input('Enter number :')
    if largest is None :
        largest = num
    elif num == 'done' :
        break
    elif num > largest :
        largest = num
print('Maximum is ',largest)
