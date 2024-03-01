




import random

def generateInput():
    len2 = random.randint(200, 500)
    return[random.randint(1, 2000) for _ in range(len2)]


def findMean(num):
    sum1 = 0
    for i in num:
        sum1 += i
    mean = sum1 / len(num)
    return mean

def fineMedian(num):
    s_num = sorted(num)
    len1 = len(s_num)
    if len1 %2 == 1:
        median = s_num[len1 // 2]
    else:
        median = (s_num[len1 // 2 - 1] + s_num[len1 // 2])/2
    return median


def main():

    num = generateInput()
    print("the randon number list is : " , num)

    mean = findMean(num)
    median = fineMedian(num)

    print(" the mean of this number list is : " , mean )
    print(" the median of this number list is : " , median )



if __name__ == "__main__":
    main()
