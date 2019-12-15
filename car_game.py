car_ctrl = ""
started = False
while True:
    car_ctrl = input("> ").lower()
    if car_ctrl == "start":
        if started:
            print("car is already started/..")
        else:
            started = True
            print("car started")
    elif car_ctrl == "stop":
        if not started:
            print("car is already stopped/..")
        else:
            started = False
            print("car is stopped/..")
    elif car_ctrl == "help":
        print("""start - car start
        stop --- stop car
        quit --- exit """)
    elif car_ctrl == "quit":
        print("Exiting..")
        break
    else:
        print("cant get you mams, for list of commands try 'help'")