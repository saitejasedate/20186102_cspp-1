# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    # input is captured in s
    # watch out for the data type of value stored in s
    # your code starts here
    CU_BE = int(input())
    GU_ESS = 1
    while (GU_ESS**3) < CU_BE:
        GU_ESS += 1
    if int(GU_ESS**3) == CU_BE:
        print(CU_BE, "is a perfect cube")
    else:
        print(CU_BE, "is not a perfect cube")

if __name__== "__main__":
    main()
