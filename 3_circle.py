def circle():
import turtle


turtle.shape('turtle')
n = 36
a = (n-2) * 180/n
turtle.left(90+1)
for i in range (n):
    turtle.forward(30)
    turtle.left(n)
    pass

if __name__ == "__main__":
    circle()