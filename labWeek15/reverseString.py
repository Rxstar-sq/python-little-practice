#isPalindrome.py
#2024/4/26
#palindrome check script(did before, but copy and paste)

def reverseIterative(s):
    s_list = list(s)
    left, right = 0, len(s_list) - 1
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1
    return ''.join(s_list)

def reverseRecursive(s):
    if len(s) <= 1:
        return s
    return reverseRecursive(s[1:]) + s[0]






def main():
    s = input("Enter a string: ")
    
    print("Iterative:", reverseIterative(s))
    print("Reversed string:", reverseIterative(s))
    
    print("Recursive:", reverseRecursive(s))

if __name__ == "__main__":
    main()