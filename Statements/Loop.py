num_int = 0

# In either kind of loop, the else clause is not executed if the loop was terminated by a break.
while num_int < 5:
    print(num_int, end=" ")
    num_int += 1
else:
    # Optional else statement
    # Execute if the while loop's condition is not satisfied
    print("too big")


for i in range(0, 5):
    print(i, end=" ")
else:
    # Optional else statement
    # Executed after the loop reaches its final iteration.
    print("too big")
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

#conprihension



