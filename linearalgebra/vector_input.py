class VectorInput:
    """Has various functions like those that check if input is of the correct type to reduce code redundancy in the
    main file"""

    def __init__(self, x_coordinate, y_coordinate, z_coordinate=None):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.vector = [self.x_coordinate, self.y_coordinate]

        if z_coordinate:
            self.z_coordinate = z_coordinate
            self.vector = [self.x_coordinate, self.y_coordinate, self.z_coordinate]

    def check_int(self):
        """Checks if the coordinates passed are numbers"""

        # Loops through every element in vector list and checks if its a number
        for i in range(len(self.vector)):
            try:
                int(self.vector[i]) + 1
            except TypeError:
                return False
            else:
                return True

    def get_vector(self):
        return self.vector