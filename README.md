# Plexbuilder

This is a Python file designed to automate the build and publishing of the Plex container to Docker Hub.

## Background

This tool was specifically created to build the Docker image for older Raspberry Pi devices running on ARM V7 architecture with Linux. Since it is directly sourced from the official Plex repository, there are no limitations.

## Usage

The file is self-explanatory. It requires Docker Hub credentials to push the changes and logs out the session.

To initiate the magic, run:

```
python plexbuilder.py
```

If you happen to have a Raspberry Pi lying around and want to host a media server while feeling lazy, you can easily pull the latest image by executing:

```
docker pull vijaykirann/plex-armv7:latest
```
