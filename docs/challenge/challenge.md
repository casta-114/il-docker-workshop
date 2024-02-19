author: Joao Correia
summary: Docker introduction
id: dist
tags: il,workshop,docker,python
categories: docker,python

# Hello python app in docker

## Requirements

Duration: 0:10:00

* git: [https://desktop.github.com](https://desktop.github.com)
* docker: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

**Clone Repository:**

1. open a shell (for example: powershell)
2. execute `git clone https://github.com/casta-114/il-docker-workshop.git`
3. execute `cd il-docker-workshop`

## Run App

Duration: 0:05:00

1. execute `docker-compose up --build`
2. open [http://localhost:8080](http://localhost:8080)
3. play

## Modify docker-compose

Here we will add an environment variable in our app, using the docker-compose file.

1. open docker-compose.yaml
2. under "app:" and the "environment" property with the key-value `World: "Terra"` like the image below:

![compose-environment](./images/compose-environment.png)

3. if application is running, close it. Usually `ctrl + z` works
4. execute `docker-compose up --build` to rebuild application
5. open [http://localhost:8080](http://localhost:8080)