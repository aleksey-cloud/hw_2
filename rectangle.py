import turtle


def rectangle(l):
    turtle.shape('turtle')
    for i in range(5):
        turtle.forward(l)
        turtle.left(90)

    pass


if __name__ == "__main__":
    rectangle(40)
