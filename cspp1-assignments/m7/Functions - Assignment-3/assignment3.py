'''
@Author : Saiteja
This program uses bisection search
'''

def payingDebtOff_inAYear(balance_in, annual_interestrate):
    '''
    Bisection method
    '''
    init_balance = balance_in
    moninterest_rate = annual_interestrate/12
    low_i = init_balance/12
    up_i = (init_balance* (1+ moninterest_rate)**12)/12.0
    epsilon = 0.03
    while abs(balance_in) > epsilon:
        mon_payrate = (up_i+low_i)/2
        balance_in = init_balance
        for _ in range(12):
            ans_i = balance_in - mon_payrate
            balance_in = ans_i + (ans_i * moninterest_rate)
        if balance_in > epsilon:
            low_i = mon_payrate
        elif balance_in < -epsilon:
            up_i = mon_payrate
        else:
            break
    return str(round(mon_payrate, 2))


def main():
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", payingDebtOff_inAYear(data[0], data[1]))
    
if __name__ == "__main__":
    main()
