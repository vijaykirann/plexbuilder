import os
import subprocess

repository_url = "https://github.com/plexinc/pms-docker.git"
destination_folder = 'repository'
docker_username = 'dockerhub username to publish'
docker_password = 'dockerhub Password'
docker_repository = 'vijaykirann/plex-armv7'
dockerfile = 'Dockerfile.armv7'
docker_tag = 'latest'

subprocess.run(['git', 'clone', repository_url, destination_folder])
os.chdir(destination_folder)
subprocess.run(['docker', 'build', '-t', docker_repository + ':' + docker_tag, '-f', dockerfile, '.'])

docker_login_cmd = 'docker login -u ' + docker_username + ' -p ' + docker_password
subprocess.run(docker_login_cmd, shell=True)

subprocess.run(['docker', 'push', docker_repository + ':' + docker_tag])
subprocess.run(['docker', 'logout'])