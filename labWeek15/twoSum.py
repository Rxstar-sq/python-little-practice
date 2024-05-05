#twoSum.py
#2024/4/25
#small script that about two sum peoblem



def twoSumLoops(num1, num2):
    n = len(num1)
    
    for i in range(n):
        for j in range(i + 1, n):
            if num1[i] + num1[j] == num2:
                return [i, j]
    return None


def twoSumDict(num1, num2):
    num_dict = {}
    for i, num in enumerate(num1):
        complement = num2 - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None


def twoSumLoopsAll(num1, num2):
    comb = []
    n = len(num1)
    for i in range(n):
        for j in range(i + 1, n):
            if num1[i] + num1[j] == num2:
                comb.append([i, j])
    return comb

def twoSumDictAll(num1, num2):

    num_dict = {}
    comb = []

    for i, num in enumerate(num1):
        complement = num2 - num
        if complement in num_dict:
            comb.append([num_dict[complement], i])
        num_dict[num] = i
    return comb




def main():
    num1 = [1, 2, 3, 1, 5, 6, 7, 8, 9]
    num2 = 9
    print("Index of numbers:", twoSumLoops(num1, num2))
    print("number pair:", twoSumLoopsAll(num1, num2))
    
    print("Indices of two numbers:", twoSumDict(num1, num2))
    print("All possible index comb:", twoSumDictAll(num1, num2))

if __name__ == "__main__":
    main()
