import math

from vector_input import VectorInput


class Vector:
    """Holds all functions related to vectors"""

    def magnitude(self):
        """Finds the magnitude of a vector whose coordinates are gathered through user input"""

        # Prints an intro statement and then prompts the user for the x,y, and z coordinates of the vector
        print("You will be prompted to input the x, y, and z coordinates in order for the magnitude of the vector"
              "to be calculated. Please enter a number. Leave the third prompt blank if there is no z coordinate")
        x_coordinate = input("Please enter the x coordinate of the vector: ")
        y_coordinate = input("Please enter the y coordinate of the vector: ")
        z_coordinate = input("Please enter the z coordinate of the vector (leave blank if it's a 2d vector): ")

        vector_obj = VectorInput(x_coordinate, y_coordinate, z_coordinate)
        vector = vector_obj.get_vector()

        if vector_obj.check_int():
            # Prints the answer based on the formula for magnitude of a vector depending on if a z coordinate was passed
            if z_coordinate:
                print(
                    math.sqrt(math.pow(int(vector[0]), 2) + math.pow(int(vector[1]), 2) + math.pow(int(vector[2]), 2)))
            else:
                print(math.sqrt(math.pow(int(vector[0]), 2) + math.pow(int(vector[1]), 2)))
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")

    def dot_product(self):
        """Finds the dot product of two vectors"""

        # Prints an intro statement and then prompts the user for the x,y, and z coordinates of the two vectors
        print("You will be prompted to input the x, y, and z coordinates for two vectors in order for the dot product "
              "to be calculated. Please enter a number. Leave the the prompt for the z coordinate blank if not "
              "applicable")
        x_coordinate1 = input("Please enter the x coordinate of the first vector: ")
        y_coordinate1 = input("Please enter the y coordinate of the first vector: ")
        z_coordinate1 = input("Please enter the z coordinate of the first vector (leave blank if it's a 2d vector): ")

        x_coordinate2 = input("Please enter the x coordinate of the second vector: ")
        y_coordinate2 = input("Please enter the y coordinate of the second vector: ")
        z_coordinate2 = input("Please enter the z coordinate of the second vector (leave blank if it's a 2d vector): ")

        vector_obj1 = VectorInput(x_coordinate1, y_coordinate1, z_coordinate1)
        vector1 = vector_obj1.get_vector()

        vector_obj2 = VectorInput(x_coordinate2, y_coordinate2, z_coordinate2)
        vector2 = vector_obj2.get_vector()

        if vector_obj1.check_int() and vector_obj2.check_int():
            # Prints the answer based on the formula for magnitude of a vector depending on if a z coordinate was passed
            if z_coordinate1 and z_coordinate2:
                result = \
                    int(vector1[0])*int(vector2[0]) + int(vector1[1])*int(vector2[1]) + int(vector1[2])*int(vector2[2])
                print("Result: " + str(result))
            else:
                print("Result: " + str(int(vector1[0])*int(vector2[0]) + int(vector1[1])*int(vector2[1])))
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")

    def vector_product(self):
        """Finds the vector product of two vectors"""

        # Prints an intro statement and then prompts the user for the x,y, and z coordinates of the two vectors
        print("You will be prompted to input the x, y, and z coordinates for two vectors in order for the vector "
              "product to be calculated. Please enter a number.")
        x_coordinate1 = input("Please enter the x coordinate of the first vector: ")
        y_coordinate1 = input("Please enter the y coordinate of the first vector: ")
        z_coordinate1 = input("Please enter the z coordinate of the first vector: ")

        x_coordinate2 = input("Please enter the x coordinate of the second vector: ")
        y_coordinate2 = input("Please enter the y coordinate of the second vector: ")
        z_coordinate2 = input("Please enter the z coordinate of the second vector: ")

        vector_obj1 = VectorInput(x_coordinate1, y_coordinate1, z_coordinate1)
        vector1 = vector_obj1.get_vector()

        vector_obj2 = VectorInput(x_coordinate2, y_coordinate2, z_coordinate2)
        vector2 = vector_obj2.get_vector()

        if vector_obj1.check_int() and vector_obj2.check_int():
            # Prints the answer based on the formula for vector product
            result = dict(x_coordinate=0, y_coordinate=0, z_coordinate=0)
            result[0] = int(vector1[1]) * int(vector2[2]) - int(vector1[2]) * int(vector2[1])
            result[1] = int(vector1[2]) * int(vector2[0]) - int(vector1[0]) * int(vector2[2])
            result[2] = int(vector1[0]) * int(vector2[1]) - int(vector1[1]) * int(vector2[0])

            print(f"Result: ({result[0]}, {result[1]}, {result[2]})")
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")

    def add_vectors(self):
        """Adds two vectors"""

        # Prints an intro statement and then prompts the user for the x,y, and z coordinates of the two vectors
        print("You will be prompted to input the x, y, and z coordinates for two vectors in order for the addition of "
              "two vectors to be calculated. Please enter a number. Leave the the prompt for the z coordinate blank if "
              "not applicable")
        x_coordinate1 = input("Please enter the x coordinate of the first vector: ")
        y_coordinate1 = input("Please enter the y coordinate of the first vector: ")
        z_coordinate1 = input("Please enter the z coordinate of the first vector (leave blank if it's a 2d vector): ")

        x_coordinate2 = input("Please enter the x coordinate of the second vector: ")
        y_coordinate2 = input("Please enter the y coordinate of the second vector: ")
        z_coordinate2 = input("Please enter the z coordinate of the second vector (leave blank if it's a 2d vector): ")

        vector_obj1 = VectorInput(x_coordinate1, y_coordinate1, z_coordinate1)
        vector1 = vector_obj1.get_vector()

        vector_obj2 = VectorInput(x_coordinate2, y_coordinate2, z_coordinate2)
        vector2 = vector_obj2.get_vector()

        if len(vector1) != len(vector2):
            print("Cannot find the addition of a 2D and a 3D vector")
            exit

        if vector_obj1.check_int() and vector_obj2.check_int():
            if len(vector1) == 2:
                result_x = int(vector1[0]) + int(vector2[0])
                result_y = int(vector1[1]) + int(vector2[1])
                print(f"({result_x}, {result_y})")
            else:
                result_x = int(vector1[0]) + int(vector2[0])
                result_y = int(vector1[1]) + int(vector2[1])
                result_z = int(vector1[2]) + int(vector2[2])
                print(f"Result: ({result_x}, {result_y}, {result_z})")
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")

    def subtract_vectors(self):
        """Adds two vectors"""

        # Prints an intro statement and then prompts the user for the x,y, and z coordinates of the two vectors
        print("You will be prompted to input the x, y, and z coordinates for two vectors in order for the addition of "
              "two vectors to be calculated. Please enter a number. Leave the the prompt for the z coordinate blank if "
              "not applicable")
        x_coordinate1 = input("Please enter the x coordinate of the first vector: ")
        y_coordinate1 = input("Please enter the y coordinate of the first vector: ")
        z_coordinate1 = input("Please enter the z coordinate of the first vector (leave blank if it's a 2d vector): ")

        x_coordinate2 = input("Please enter the x coordinate of the second vector: ")
        y_coordinate2 = input("Please enter the y coordinate of the second vector: ")
        z_coordinate2 = input("Please enter the z coordinate of the second vector (leave blank if it's a 2d vector): ")

        vector_obj1 = VectorInput(x_coordinate1, y_coordinate1, z_coordinate1)
        vector1 = vector_obj1.get_vector()

        vector_obj2 = VectorInput(x_coordinate2, y_coordinate2, z_coordinate2)
        vector2 = vector_obj2.get_vector()

        if len(vector1) != len(vector2):
            print("Cannot find the addition of a 2D and a 3D vector")
            exit

        if vector_obj1.check_int() and vector_obj2.check_int():
            if len(vector1) == 2:
                result_x = int(vector1[0]) - int(vector2[0])
                result_y = int(vector1[1]) - int(vector2[1])
                print(f"({result_x}, {result_y})")
            else:
                result_x = int(vector1[0]) - int(vector2[0])
                result_y = int(vector1[1]) - int(vector2[1])
                result_z = int(vector1[2]) - int(vector2[2])
                print(f"Result: ({result_x}, {result_y}, {result_z})")
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")

    def multiply_vectors(self):
        """Adds two vectors"""

        # Prints an intro statement and then prompts the user for the x,y, and z coordinates of the two vectors
        print(
            "You will be prompted to input the x, y, and z coordinates for two vectors in order for the addition of two"
            " vectors to be calculated. Please enter a number. Leave the the prompt for the z coordinate blank if not "
            "applicable")
        x_coordinate1 = input("Please enter the x coordinate of the first vector: ")
        y_coordinate1 = input("Please enter the y coordinate of the first vector: ")
        z_coordinate1 = input("Please enter the z coordinate of the first vector (leave blank if it's a 2d vector): ")

        x_coordinate2 = input("Please enter the x coordinate of the second vector: ")
        y_coordinate2 = input("Please enter the y coordinate of the second vector: ")
        z_coordinate2 = input("Please enter the z coordinate of the second vector (leave blank if it's a 2d vector): ")

        vector_obj1 = VectorInput(x_coordinate1, y_coordinate1, z_coordinate1)
        vector1 = vector_obj1.get_vector()

        vector_obj2 = VectorInput(x_coordinate2, y_coordinate2, z_coordinate2)
        vector2 = vector_obj2.get_vector()

        if len(vector1) != len(vector2):
            print("Cannot find the addition of a 2D and a 3D vector")
            exit

        if vector_obj1.check_int() and vector_obj2.check_int():
            if len(vector1) == 2:
                result_x = int(vector1[0]) * int(vector2[0])
                result_y = int(vector1[1]) * int(vector2[1])
                print(f"({result_x}, {result_y})")
            else:
                result_x = int(vector1[0]) * int(vector2[0])
                result_y = int(vector1[1]) * int(vector2[1])
                result_z = int(vector1[2]) * int(vector2[2])
                print(f"Result: ({result_x}, {result_y}, {result_z})")
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")
