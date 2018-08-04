#Guess My Number Exercise

def main():
    #your code here
    mid_n = 50
    high_n = 100
    low_n = 0
    in_p = 'l'
    while (in_p!='c'):
        print(mid_n)
        in_p = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if in_p == 'h':
            high_n = mid_n
            mid_n = (high_n+low_n)//2
        elif in_p == 'l':
            low_n = mid_n
            mid_n = (high_n + low_n)//2
    print("your number is:",mid_n)
if __name__ == "__main__":
    main()