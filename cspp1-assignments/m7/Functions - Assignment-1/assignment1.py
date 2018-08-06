'''
@author : saitejasedate
'''
# Functions | Assignment-1 - Paying Debt off in a Year

# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the
# credit card company each month.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135

# So your program only prints out one thing: the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0

# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


def pay_debt_in_year(blc_1, annual_interest_rate, monthly_payment_rate):

    """function debt off in a year"""
    i = 0
    for i in range(1, 13):
        m_int_rate = annual_interest_rate / 12.0
        min_month_pay = monthly_payment_rate * blc_1
        mnth_unpaid_bal = blc_1 - min_month_pay
        up_bal_each_month = mnth_unpaid_bal + m_int_rate * mnth_unpaid_bal
        blc_1 = up_bal_each_month
        i = i + 1
    return round(blc_1, 2)


def main():
    """main"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:", pay_debt_in_year(data[0], data[1], data[2]))

if __name__ == "__main__":
    main()

