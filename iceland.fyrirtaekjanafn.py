import re
#samhljodar = re.compile("[BCDFGJKLMNPQSTVXZHRWY]")
#serhljodar = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y"]

#n_name = ""
name = input()

print(re.sub("[BCDFGJKLMNPQSTVXZHRW]", "", name, flags=re.IGNORECASE))
#for n in name:
 #   if n in serhljodar:
  #      n_name += n

#print(n_name)
    #for i in range(len(serhljodar)):
        #stafur = serhljodar[i]
        #if name[n] == stafur:
            #n_name += stafurfeceboo



# time limit exceeded