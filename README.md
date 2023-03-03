# movie-watchlist

> A Simple Python Flask app for keeping track off movies you watched

## Docker local testing

> Run mongodb container

```sh
docker container run  -p 27017:27017 -d --rm --name mongodb mongo:6.0.4
```

> Build the Python Flask image

```sh
docker build -t movie-library:1.0.0 .
```

> Run the Python Flask container

```sh
MY_IP=$(ifconfig en0 | awk '/inet / {print $2}')
MONGODB_URI="mongodb://${MY_IP}:27017/movies"
docker run --env MONGODB_URI=${MONGODB_URI} -p 8080:80 --rm --name movietime movie-library:1.0.0
```

## Deploy to Kubernetes
