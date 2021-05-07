string = "??????"
string_l = list(string)
string_l[2] += "XY"
string_l[3] = "Z"
string_n = "".join(string_l)
print(string_n)