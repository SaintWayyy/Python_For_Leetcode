num_int = 0

while num_int < 5:
    print(num_int, end=" ")
    num_int += 1
else:
    # Optional else statement
    # Execute if the while loop's condition is not satisfied
    print("too big")


for i in range(0, 5):
    print(i, end=" ")
print()


for i in range(0, 5):
    if i == 3:
        continue
    print(i, end=" ")
print()


for i in range(0, 5):
    if i == 3:
        break
    print(i, end=" ")
print()




