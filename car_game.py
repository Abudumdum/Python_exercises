command = ""
started = False
stopped = False
while True:
    command = input("> ")
    if command == "start":
        if started:
            print("  The car has already started")
        else:
            started = True
            print("  The car has started...")
    elif command == "brake":
        if not started:
            print("please start the car")
        elif stopped:
            print("  The car has already been stopped and you can't stop a car twice")
        else:
            stopped = True
            print("  The car has come to a halt...")
    elif command == "help":
        print("""
start - to start the car
brake - to stop the car 
quit - to exit the game
        """)
    elif command == "quit":
        break
    else:
        print("  I do not understand this command")
