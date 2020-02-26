# Download base image ubuntu
FROM ubuntu:16.04

# Update Ubuntu repo
RUN apt-get update

# Install htop
RUN apt-get install htop

# Start htop
ENTRYPOINT [ "htop" ]

ENV TERM xterm
