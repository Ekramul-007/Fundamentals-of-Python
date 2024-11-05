while True:

        print("Choose option number to find area")
        print("***********************************")
        print(""""
        1. Area of circle
        2. Area of rectangle
        3. Area of triangle
        4. Area of parallelogram
        5. Area of square
        0. To exit""")
        print("***********************************")
        user_input=int(input("Enter your choice: "))
        if user_input == 1:
            radius = float(input("Enter radius of circle: "))
            area = 3.1416*radius**2
            print("Area of circle is", area)

        elif user_input == 2:
            length = float(input("Enter length of rectangle: "))
            width = float(input("Enter width of rectangle: "))
            area = length*width
            print("Area of rectangle is", area)

        elif user_input == 3:
            base = float(input("Enter base of triangle: "))
            height = float(input("Enter height of triangle: "))
            area = base*height*.5
            print("Area of triangle is", area)
        elif user_input == 4:
            base = float(input("Enter base of parallelogram: "))
            height = float(input("Enter height of parallelogram: "))
            area = base*height
            print("Area of parallelogram is", area)
        elif user_input == 5:
            side = float(input("Enter side of square: "))
            area = side*side
            print("Area of square is", area)
        elif user_input == 0:
            break
        else:
            print("Invalid input")
