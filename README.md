# mattmcn9/flask-basic-auth

This is a lightweight file server built with Flask, featuring:

- HTTP file browsing (like python3 -m http.server)

- HTTP Basic Authentication

- Configurable via environment variables

- Dockerized for easy deployment

### Installation from [Docker registry hub](https://hub.docker.com/repository/docker/mattmcn9/flask-basic-auth/).

You can download the image with the following command:

```bash
docker pull mattmcn9/flask-basic-auth
```

Environment variables
----

This image uses environment variables to allow the configuration of some parameters at run time:

* Variable name: `USERNAME`
* Default value: user
* Accepted values: Any string. Avoid whitespaces and special chars.
* Description: Username for the login. If you don't specify it through the `USERNAME` environment variable at run time, `user` will be used by default.

----

* Variable name: `PASSWORD`
* Default value: password
* Accepted values: Any string. Avoid whitespaces and special chars.
* Description: Password for the login. If you don't specify it through the `PASSWORD` environment variable at run time, `password` will be used by default.

----

* Variable name: `DATA_DIR`
* Default value:  /data
* Accepted values: Any string.
* Description: Data directory for the http service to display. If you don't specify it through the `DATA_DIR` environment variable at run time, `/data` will be used by default.

----

* Variable name: `PORT`
* Default value: 8080
* Accepted values: Any port number
* Description: If you don't specify a port number, through the `PORT` environment variable at run time, `8080` will be used by default 

----


Use cases
----

1) Create a temporary container for testing purposes:

```bash
  docker run --rm -p 8080:8080 mattmcn9/flask-basic-auth
```

2) Create a container and set the login information, with a binded data directory:

```bash
docker run -d -p 8080:8080 -v /my/data/directory:/data -e USERNAME=myUser -e PASSWORD=MyPassword! --name flask-http-auth mattmcn9/flask-basic-auth
```
