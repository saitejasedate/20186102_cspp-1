'''
@author : saitejasedate
This is third porgram.
'''
VARA = 8
VARB = 7
if VARA > VARB:
    print("Greater")
elif VARA < VARB:
    print("smaller")
elif VARA==VARB:
    print("equal")
elif (isinstance(VARA) == str) or (isinstance(VARB) == str):
    print("strings involved")
