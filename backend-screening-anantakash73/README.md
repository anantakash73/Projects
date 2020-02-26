<div class="center">
<p align="center"><img src="https://user-images.githubusercontent.com/523933/49741959-91a1da00-fc65-11e8-911f-521331f87174.png" align="center" width="20%" height="20%"></p>
  <h1 align="center">Clear Street</h1>
  <p align="center">
  	<h2 align="center">
    	ReadMe
  	</h2>
	</p>
</div>

#

This repository contains parts of your interview. Your repository is private; only you and Clear Street team members can view it. 

Please create a new branch of `master` to complete your work. Once you are satisified, create a pull-request to merge your work into `master`. The pull-request will let us know you are finished.

## Q&A:

Please answer the following questions inline in this README.md file. Below each question, insert your response using tasteful Markdown choices.

### Tooling:

Provide your perference for each of the categories below.

1. operating system?

    MacOS
1. terminal type?

    iTerm

1. scripting languauge?

    Python3

### Pros & Cons:

Provide some salient pros and cons for each of the scenarios described below.

1. windows vs. linux

   Windows is better for large enterprise softwares that require a GUI for operation and/or use by non technical personnel

   Linux is better for quick setup and custom work that can be done by those with more technical knowledge

1. mono-repository vs. multi-repository

    mono-repository is better if everyone in the organization is trusted to access to all the code
    multi-repository is better when it known that the different repos will not interact with each other and different personnel will work on them

1. strongly typed vs. loosely typed languages

    strongly typed languages such as Swift,C++ are better when errors need to be caught at compile time and not at run time. They are also better for readability purposes

    loosely typed languages like JavaScript offer more flexibility and easier interchangability between types

1. monolith vs. microservice architecture

    monolith architecture is better for smaller teams where the codebase is not too large and more developer time will be required for feature building rather than DevOps

    Microservice architecture scales better and is more resilient as even if a service fails, the larger infrastructure is intact. However, this requires a lot more investment and personnel into DevOps

1. do you prefer git command-line or a git UI client?

    I have always preferred using the git command line before I recently switched to using Visual Studio Code, which has a built in GUI for git. I have been using that since. 


## Implementations:

The following sections asks you to implement mini-projects. You should add your project files directly to this repository.

### Docker:

Create a directory called `docker`. Now implement the following within this directory:

1. Create a `Dockerfile` so that an image can be built that runs `htop`. Your image should work against the following docker commands:

    `$ docker run -it --rm <YOUR_IMAGE>`

    Should run `htop`.

    `$ docker run -it --rm <YOUR_IMAGE> --version`

    Should echo the version of `htop` installed.

2. Create a `docker-compose.yml` so that you can bring up two services at once that run `htop`. In other words, running the following should create two `htop` instances:

    `$ cd ./docker && docker-compose up`

### Web Server:

For this portion of your project, please use GoLang, Java, or Python. Using GoLang is preferred.

Build out a web server that follows the swagger spec provided in `src/`.  Please reach out if you have any questions regarding the spec and/or what is expected.

This portion of the test will be autograded. Your app MUST listen on localhost:8080 AND return the proper status code for the tests to be successful. You will also need to create a Dockerfile inside `src/` directory that can be built and run your server with the following commands (run from the go/src directory):

  `$ docker build -t <IMAGE_NAME> ./`

  `$ docker run -d -p 8080:8080 <IMAGE_NAME>`

A sample Dockerfile:

```
FROM golang:alpine
RUN apk --no-cache add git
RUN mkdir /app
COPY ./ $GOPATH/app
WORKDIR $GOPATH/app
RUN go get
RUN go build cmd/trades-server/main.go
CMD ["./main", "--host", "0.0.0.0", "--port", "8080"]
```
