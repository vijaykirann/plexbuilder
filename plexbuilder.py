import os
import subprocess

repository_url = "https://github.com/plexinc/pms-docker.git"
destination_folder = 'repository'
docker_username = 'dockerhub username to publish'
docker_password = 'dockerhub Password'
docker_repository = 'vijaykirann/plex-armv7'
dockerfile = 'Dockerfile'
docker_tag = 'latest'

# clones the repository form GIT
subprocess.run(['git', 'clone', repository_url, destination_folder])
os.chdir(destination_folder)

# runs the docker build and creates the image
subprocess.run(['docker', 'build', '-t', docker_repository + ':' + docker_tag, '-f', dockerfile, '.'])

#login to docker hub
docker_login_cmd = 'docker login -u ' + docker_username + ' -p ' + docker_password
subprocess.run(docker_login_cmd, shell=True)

#Pushes the image to dockerhub and logs out
subprocess.run(['docker', 'push', docker_repository + ':' + docker_tag])
subprocess.run(['docker', 'logout'])
