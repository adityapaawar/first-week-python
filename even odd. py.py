#checking even/Odd using Bitwise Operators

def isEven(n):
 
    if (n | 1 > n):
        return True
    else:
        return False
 

if __name__ == "__main__":
    n = 100
    print("Even") if isEven(n) else print("Odd")
