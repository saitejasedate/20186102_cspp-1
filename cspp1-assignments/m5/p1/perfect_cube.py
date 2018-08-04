'''
@author : saitejasedate
'''
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
    c_len = int(input())
    gu_ess = 1
    while (gu_ess**3) < c_len:
        gu_ess += 1
    if int(gu_ess**3) == c_len:
        print(c_len, "is a perfect cube")
    else:
        print(c_len, "is not a perfect cube")

if __name__ == "__main__":
    main()
