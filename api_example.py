def test():
    msg = "hi"
    def inner():
        print(msg)
    return inner

test()()