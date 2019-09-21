numbersTaken = [2, 5, 12, 13, 17]

print("Here are the numbers that are still availible:")

for n in range(1,100):
    if n in numbersTaken:
        continue
    print(n)

