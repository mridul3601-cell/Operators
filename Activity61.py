def shutdown():
    a = input()

    if a == "Yes":
        print("Shutting down")
    elif a == "No":
        print("Abort shut down")
    else:
        print("Sorry")

shutdown()