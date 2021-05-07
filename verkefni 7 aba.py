

from random import randint
num1=(randint(1,10))
num2=int(input("Sláðu inn tölu frá 1 upp í 10: "))

print ("Tölvan velur: ", num1, "Þú valdir", num2)

if num1==num2:
    print ("Þú giskaðir á réttu töluna, talan er: ", num1)
elif num1<num2:
    print ("Þú giskaðir á of háa tölu, talan var: ", num1)
elif num1>num2:
    print ("Þú giskaðir á of lága tölu, talan var: ", num1)
