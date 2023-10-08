def num_range(num):
    if num <= 10:
        print("less than 10")
    elif 10 < num <= 50:
        print("between 10 to 50")
    elif 50 < num <= 100:
        pass
    else:
        print("greater than 100")
    return


num_range(0)
num_range(20)
num_range(80)
num_range(200)
print()


# case matching
def http_status(status):
    match status:
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 401 | 403:  # match mutil cases
            print("Not allowed")
        case x if 500 <= x < 600:  # pattern matching, assign the value of status to x
            print("Server error")
        case _:
            print("Error")


http_status(400)
http_status(403)
http_status(550)
http_status(0)
print()


# structural pattern matching
def point(x, y):
    match (x, y):
        case (0, 0):
            print("origin")
        case (0, _):
            print("y axis")
        case (_, 0):
            print("x axis")
        case (x, y):
            print(x, y)
        case _:
            print("Error")


point(0, 0)
point(0, 1)
point(1, 0)
point(2, 2)
