### Hackerrank - Array Left Rotation

Project struture
```
.
├── main.py             # Main entry
├── LeftRotation.py     # Solution for problem
├── Dockerfile  
├── LICENSE
└── README.md
```

#### How to use
##### Local style
Use this command line to run: __python -m main <first_arg> <second_arg>__<br />
**Note**: 
- <first_arg> must be a string
- <second_arg> must be an integer

For example, we'll get "deabc" as a result after performing 3 left rotations on "abcde":
```console
foo@bar:~$ python -m main abcde 3
deabc
```

##### Docker style
Firstly, we'll build the docker image (in this example below, we also create a tag for our docker image)
```console
foo@bar:~$ docker build -t array-left-rotation .
```
We can check our docker image
```console
foo@bar:~$ docker images
```
Next, we can run a container based on this docker image via the command line:<br />
__docker run --rm array-left-rotation <first_arg> <second_arg>__<br />
By default, the <first_arg> is "abcde" and <second_arg> is 3.<br />
For example:
```console
foo@bar:~$ docker run --rm array-left-rotation
deabc
```
Or
```console
foo@bar:~$ docker run --rm array-left-rotation nguyenxuanhuy 4
enxuanhuynguy
```

