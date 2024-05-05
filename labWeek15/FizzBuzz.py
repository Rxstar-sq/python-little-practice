#fissBuzz.py
#2024/4/26
#small script that show the fizzbuzz problem (seriously)

#this comes from https://www.enjoyalgorithms.com/blog/fizz-buzz-problem
def fizzBuzzModulus(num):
    mod = []
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            mod.append("FizzBuzz")
        elif i % 3 == 0:
            mod.append("Fizz")
        elif i % 5 == 0:
            mod.append("Buzz")
        elif i % 7 == 0:
            mod.append("FIZZYBUZZY")
        else:
            mod.append(str(i))
    return mod

def fizzBuzzDict(num):
    dict = []
    fizzBuzz_dict = {3: "Fizz", 5: "Buzz", 7: "FIZZYBUZZY"}
    for i in range(1, num+1):
        word = ""
        for key in fizzBuzz_dict:
            if i % key == 0:
                word += fizzBuzz_dict[key]
        if not word:
            word = str(i)
        dict.append(word)
    return dict



def main():
    num= int(input("Enter an integer: "))
    print("FizzBuzz by using modulus: ", fizzBuzzDict(num))
    
    print("FizzBuzz by using dictionary: " , fizzBuzzDict(num))

if __name__ == "__main__":
    main()