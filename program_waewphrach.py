import math

while True:
    shape = input("\nChoose shape (rectangle, triangle, circle, exit): ").lower()

    if shape == "exit":
        break

    try:
        if shape == "rectangle":
            width = float(input("Width: "))
            length = float(input("Length: "))
            if width > 0 and length > 0:
                print("Area =", width * length)

        elif shape == "triangle":
            base = float(input("Base: "))
            height = float(input("Height: "))
            if base > 0 and height > 0:
                print("Area =", 0.5 * base * height)

        elif shape == "circle":
            radius = float(input("Radius: "))
            if radius > 0:
                print("Area =", math.pi * radius**2)

        else:
            print("Invalid shape")

    except ValueError:
        print("Please enter numbers only.")
