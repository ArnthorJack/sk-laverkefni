
past_hour, past_minute = map(int, input().split(":"))
current_hour, current_minute = map(int, input().split(":"))

current = int(current_hour) * 60 + int(current_minute)
past = int(past_hour) * 60 + int(past_minute)

if current < past:
    current += 24 * 60
    
x3 = int(current) - int(past)


print(x3)