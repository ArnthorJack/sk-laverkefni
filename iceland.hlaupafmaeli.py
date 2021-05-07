
#x = float(10.5 + 10.5)
#y = str(x)[::-1]
#print(y[0 : 2])
test = "0."
year = int(input())
div4_year = float(year / 4)
div100_year = float(year / 100)
div400_year = float(year / 400)
d4_year = str(div4_year)[::-1]
d100_year = str(div100_year)[::-1]
d400_year = str(div400_year)[::-1]
if d4_year[0 : 2] == "0.":
    if d100_year[0 : 2] == "0.":
        if d400_year[0 : 2] == "0.":
            print(int(div4_year) - 505)
        else:
            print("Neibb")
    else:
        print(int(div4_year) - 505)
else:
    print("Neibb")