import sys
from LeftRotation import LeftRotation

if __name__ == "__main__":
    string = sys.argv[1]
    try:
        nb_rotation = int(sys.argv[2])
        left_rotation = LeftRotation()
        print(left_rotation.rotate(string, nb_rotation))
    except ValueError:
        print('The second argument must be an integer...')
