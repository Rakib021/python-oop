def timer():
    def inner():
        print("Time started")

        print("time ended")
    return inner