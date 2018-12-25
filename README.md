# Hello Docker

Practice of "[Dockerfile](./Dockerfile)" with an `ENTRYPOINT` to the script "[hello-world.py](./src/hello-world.py)".

## Building docker image

Make sure you have `docker` installed, then run `build` command as below:

```shellsession
$ # Version check
$ docker --version
Docker version 18.09.0, build 4d60db4
$ 
$ # Change directory to this repo
$ cd /path/to/this/repo
$
$ # Build image with a name 'test-image'
$ docker build -t test-image ./
```

## Create a container from an image and run 

Each commands below creates a container from an image, runs the script "[hello-world.py](./src/hello-world.py)", shuts down the container and then removes the container.

```shellsession
$ docker run --rm test-image --say
Hello World
$ 
$ docker run --rm test-image --echo foo
foo
$ 
$ docker run --rm test-image --help
usage: This script prints "Hello World" or given string as an argument.
       [-h] [-e ECHO] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -e ECHO, --echo ECHO  Echoes the string followed.
  -s, --say             Returns 'Hello World'.
$ 
$ docker run --rm test-image
usage: This script prints "Hello World" or given string as an argument.
       [-h] [-e ECHO] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -e ECHO, --echo ECHO  Echoes the string followed.
  -s, --say             Returns 'Hello World'.
$ 
```

