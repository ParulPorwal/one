def isPalindrome(num):
    x =num
    rev = 0
    if x < 0 :
        return False
    while x :
        r = x % 10
        rev = rev *10 +r
        x = x // 10
    return num == rev

if isPalindrome(int(input())):
    print(True)
else:
    print(False)
