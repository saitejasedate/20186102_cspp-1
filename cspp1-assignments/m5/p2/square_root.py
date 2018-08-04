'''
@author : saitejasedate
'''
# Write a python program to find the sq_uare root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''
    python program to find the sq_uare root of the given number
    using approximation method
    '''
    ep_silon = 0.01
    st_ep = 0.1
    sq_uare = int(input())
    gu_ess = 0.0
    while gu_ess <= sq_uare:
        if abs(gu_ess**2-sq_uare) < ep_silon:
            break
        else:
            gu_ess += st_ep
    print(str(gu_ess))

if __name__ == "__main__":
    main()
