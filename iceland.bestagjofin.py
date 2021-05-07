ammount = int(input())

name = ""
score = 0

for i in range(ammount):
    temp_name, temp_score = input().split()
    if score < int(temp_score):
        score = int(temp_score)
        name = temp_name
print(name)