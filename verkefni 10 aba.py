ö=True

while ö==True:
    table=int(input("Hvaða margföldunartöflu villtu sjá? "))

    for i in range (1,11):
        print (table,"X",i,"=",table*i)

    ans=str(input("Villtu fá aðra töflu? j/n: "))
    if ans=="n":
        ö=False

print ("Forritunu er lokið")
