import sys
from LeftRotation import LeftRotation

if __name__ == "__main__":
    string = sys.argv[0]
    nb_rotation = sys.argv[1]
    left_rotation = LeftRotation()
    print(left_rotation.rotate(string, nb_rotation))
