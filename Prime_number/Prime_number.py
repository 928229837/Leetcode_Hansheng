def check_prim(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num//i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

# check_prim(407)


def get_all_prim(min, max):
    print("Prime # between", min, "and", max, "are:")

    for num in range(min, max+1):
        if num > 1:
            for i in range(2,num):
                if num%i == 0:
                    break
            else:
                print(num, end=' ')

get_all_prim(9, 100)


