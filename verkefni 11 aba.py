ö=True

while ö==True:

    mv=str(input("Villtu reikna margfeldi eða veldi? m/v: "))

    if mv=="m":

        table=int(input("Hvaða margföldunartöflu villtu sjá? "))

        for i in range (1,11):
            print (table,"X",i,"=",table*i)

    if mv=="v":

        table=int(input("Hvaða tölu villtu fá í veldi? "))

        for i in range (1,11):
            print (table,"^",i,"=",table**i)

    ans=str(input("Villtu fá aðra töflu? j/n: "))
    if ans=="n":
        ö=False

print ("Forritunu er lokið")
