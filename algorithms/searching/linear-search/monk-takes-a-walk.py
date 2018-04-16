vowels = ['a', 'e', 'i', 'o', 'u']

t = int(input())

for _ in range(t):
    trees = input().lower()
    count = 0

    for letter in trees:
        if letter in vowels:
            count += 1

    print(count)
