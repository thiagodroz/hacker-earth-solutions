def is_int(input):
  try:
    num = int(input)
  except ValueError:
    return False
  return True

n = int(input())
days = {}

for _ in range(n):
    message = input().split(' ')
    numbers = [int(d) for d in message if is_int(d)]

    weight = 2 if message[0] == 'G:' else 1

    for number in numbers:
        if number in days.keys():
            days[number] += weight
        else:
            days[number] = weight

if len(days.keys()) == 0:
    print('No Date')
elif len(days.keys()) == 1:
    if days[days.keys()[0]] == 19 or days[days.keys()[0]] == 20:
        print('Date')
    else:
        print('No Date')
else:
    sorted_days = sorted(days.items(), reverse=True, key=lambda x: x[1])

    if sorted_days[0][1] == sorted_days[1][1]:
        print('No Date')
    elif sorted_days[0][0] == 19 or sorted_days[0][0] == 20:
        print('Date')
    else:
        print('No Date')
