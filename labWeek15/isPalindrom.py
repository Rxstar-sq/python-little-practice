#isPalindrome.py
#2024/4/26
#palindrome check script(did before, but copy and paste)

def isPalindromeIterative(str):
    str = str.replace(" ", "").lower()

    for i in range(len(str) // 2):
        if str[i] != str[-(i + 1)]:
            return False
    return True

def isPalindromeRecursive(str):
    if len(str) <= 1:
        return True
    if str[0] != str[-1]:
        return False
    return isPalindromeRecursive(str[1:-1])





def main():
    str = input("Enter a string: ")
    print("Iterative:", isPalindromeIterative(str))    
    print("Recursive:", isPalindromeRecursive(str))

if __name__ == "__main__":
    main()