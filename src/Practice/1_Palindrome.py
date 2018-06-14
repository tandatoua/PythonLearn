'''回文数判断'''
def is_palindrome(n:int)->int:
    n = str(n)
    m = n[::-1]
    return m == n