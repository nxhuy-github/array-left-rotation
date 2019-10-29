class LeftRotation:
    """
    A class used to solve the problem at https://www.hackerrank.com/challenges/array-left-rotation/problem

    Methods
    -------
    rotate(string, nb_rotation)
        Shifts nb_rotation element of string to the left
    """


    def rotate(self, string, nb_rotation):
        """
        Rotates the string
        Time complexity: O(N)

        Parameters
        ----------
        string: str, required
            The original string
        nb_rotation: int, required
            The number of left rotations

        Returns
        -------
        str
            a new string after performing nb_rotation left rotations
        """

        n = len(string)
        # When the nb_rotation is bigger than the string's length
        if nb_rotation > n:
            nb_rotation = nb_rotation % n
        return string[nb_rotation:] + string[:nb_rotation]
