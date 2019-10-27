class LeftRotation:
    def rotate(self, string, nb_rotation):
        n = len(string)
        if nb_rotation > n:
            nb_rotation = nb_rotation % n
        return string[nb_rotation:] + string[:nb_rotation]
