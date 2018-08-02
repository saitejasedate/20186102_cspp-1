'''
@author : saitejasedate
Program to check the number of vowels in a string.
'''
S = input()
VOWELS = "a, e, i, o, u"
B = len(VOWELS)
L = len(S)
C = 0
J = 0
for I in range(0, L, 1):
    for J in range(0, B, 1):
        if S[I] == VOWELS[J]:
            C = C+1
print(C)
