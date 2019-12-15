name = input("enter name")

if len(name) <= 3:
    print("name should be at least 3 characters")
elif len(name) >= 50:
    print("name should be max of 50 characters")
else:
    print("name looks to be good")
