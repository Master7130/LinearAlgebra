import math

from linearalgebra import vector_input


class Vector:
    """Holds all functions related to vectors"""

    def magnitude(self, x_param, y_param, z_param=None):
        """Finds the magnitude of a vector whose coordinates are gathered through user input"""

        vector_obj = vector_input.VectorInput(x_param, y_param, z_param)
        vector = vector_obj.get_vector()

        if vector_obj.check_int():
            # Prints the answer based on the formula for magnitude of a vector depending on if a z coordinate was passed
            if z_param:
                return \
                    math.sqrt(math.pow(int(vector[0]), 2) + math.pow(int(vector[1]), 2) + math.pow(int(vector[2]), 2))
            else:
                return math.sqrt(math.pow(int(vector[0]), 2) + math.pow(int(vector[1]), 2))
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")

    def dot_product(self, x_param1, y_param1, x_param2, y_param2, z_param1=None, z_param2=None):
        """Finds the dot product of two vectors"""

        vector_obj1 = vector_input.VectorInput(x_param1, y_param1, z_param1)
        vector1 = vector_obj1.get_vector()

        vector_obj2 = vector_input.VectorInput(x_param2, y_param2, z_param2)
        vector2 = vector_obj2.get_vector()

        if vector_obj1.check_int() and vector_obj2.check_int():
            # Prints the answer based on the formula for magnitude of a vector depending on if a z coordinate was passed
            if z_param1 and z_param2:
                return int(vector1[0]) * int(vector2[0]) + int(vector1[1]) * int(vector2[1]) + int(vector1[2]) * \
                       int(vector2[2])
            else:
                return "Result: " + int(vector1[0]) * int(vector2[0]) + int(vector1[1]) * int(vector2[1])
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")

    def vector_product(self, x_param1, y_param1, z_param1, x_param2, y_param2, z_param2):
        """Finds the vector product of two vectors"""

        vector_obj1 = vector_input.VectorInput(x_param1, y_param1, z_param1)
        vector1 = vector_obj1.get_vector()

        vector_obj2 = vector_input.VectorInput(x_param2, y_param2, z_param2)
        vector2 = vector_obj2.get_vector()

        if vector_obj1.check_int() and vector_obj2.check_int():
            # Prints the answer based on the formula for vector product
            result = dict(x_coordinate=0, y_coordinate=0, z_coordinate=0)
            result[0] = int(vector1[1]) * int(vector2[2]) - int(vector1[2]) * int(vector2[1])
            result[1] = int(vector1[2]) * int(vector2[0]) - int(vector1[0]) * int(vector2[2])
            result[2] = int(vector1[0]) * int(vector2[1]) - int(vector1[1]) * int(vector2[0])

            result = [result[0], result[1], result[2]]

            return result
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")

    def add_vectors(self, x_param1, y_param1, x_param2, y_param2, z_param1=None, z_param2=None):
        """Adds two vectors"""

        vector_obj1 = vector_input.VectorInput(x_param1, y_param1, z_param1)
        vector1 = vector_obj1.get_vector()

        vector_obj2 = vector_input.VectorInput(x_param2, y_param2, z_param2)
        vector2 = vector_obj2.get_vector()

        if len(vector1) != len(vector2):
            print("Cannot find the addition of a 2D and a 3D vector")
            exit

        if vector_obj1.check_int() and vector_obj2.check_int():
            if len(vector1) == 2:
                result_x = int(vector1[0]) + int(vector2[0])
                result_y = int(vector1[1]) + int(vector2[1])
                return [result_x, result_y]
            else:
                result_x = int(vector1[0]) + int(vector2[0])
                result_y = int(vector1[1]) + int(vector2[1])
                result_z = int(vector1[2]) + int(vector2[2])
                return [result_x, result_y, result_z]
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")

    def subtract_vectors(self, x_param1, y_param1, x_param2, y_param2, z_param1=None, z_param2=None):
        """Subtracts two vectors"""

        vector_obj1 = vector_input.VectorInput(x_param1, y_param1, z_param1)
        vector1 = vector_obj1.get_vector()

        vector_obj2 = vector_input.VectorInput(x_param2, y_param2, z_param2)
        vector2 = vector_obj2.get_vector()

        if len(vector1) != len(vector2):
            print("Cannot find the addition of a 2D and a 3D vector")
            exit

        if vector_obj1.check_int() and vector_obj2.check_int():
            if len(vector1) == 2:
                result_x = int(vector1[0]) - int(vector2[0])
                result_y = int(vector1[1]) - int(vector2[1])

                return [result_x, result_y]
            else:
                result_x = int(vector1[0]) - int(vector2[0])
                result_y = int(vector1[1]) - int(vector2[1])
                result_z = int(vector1[2]) - int(vector2[2])

                return [result_x, result_y, result_z]
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")

    def multiply_vectors(self, x_param1, y_param1, x_param2, y_param2, z_param1=None, z_param2=None):
        """Multiplies two vectors"""

        vector_obj1 = vector_input.VectorInput(x_param1, y_param1, z_param1)
        vector1 = vector_obj1.get_vector()

        vector_obj2 = vector_input.VectorInput(x_param2, y_param2, z_param2)
        vector2 = vector_obj2.get_vector()

        if len(vector1) != len(vector2):
            print("Cannot find the addition of a 2D and a 3D vector")
            exit

        if vector_obj1.check_int() and vector_obj2.check_int():
            if len(vector1) == 2:
                result_x = int(vector1[0]) * int(vector2[0])
                result_y = int(vector1[1]) * int(vector2[1])

                return [result_x, result_y]
            else:
                result_x = int(vector1[0]) * int(vector2[0])
                result_y = int(vector1[1]) * int(vector2[1])
                result_z = int(vector1[2]) * int(vector2[2])

                return [result_x, result_y, result_z]
        else:
            print("Invalid input(s)")
            print("Please enter numbers for the prompts")
