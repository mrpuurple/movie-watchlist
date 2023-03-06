# movie-watchlist

## A Simple Python Flask app for keeping track off movies you watched

---

![screenshot](./pics/screenshot.png?raw=true "Screenshot picture of the App")

### Docker local testing

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

### Docker build for different architectures using `buildx` on Apple Silicon M1 chip

> ERROR: multiple platforms feature is currently not supported for docker driver. Please switch to a different driver (eg. "docker buildx create --use")

```sh
docker buildx create --use
```

> Build and push in the same command

```sh
docker buildx build --platform  linux/amd64,linux/arm64 --push -t <your repo>/movie-library:1.0.0 .
```

### Deploy to Kubernetes

#### [mongodb helm chart](https://artifacthub.io/packages/helm/bitnami/mongodb)

```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install mongodb bitnami/mongodb -f ./k8s/mongodb-values.yaml
```

> output

```text
MongoDB&reg; can be accessed on the following DNS name(s) and ports from within your cluster:

    mongodb.default.svc.cluster.local

To connect to your database, create a MongoDB&reg; client container:

    kubectl run --namespace default mongodb-client --rm --tty -i --restart='Never' --env="MONGODB_ROOT_PASSWORD=$MONGODB_ROOT_PASSWORD" --image docker.io/bitnami/mongodb:6.0.4-debian-11-r14 --command -- bash

Then, run the following command:
    mongosh admin --host "mongodb"

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace default svc/mongodb 27017:27017 &
    mongosh --host 127.0.0.1
```

> Deploy the movie-watchlist app

```sh
kubectl apply -f ./k8s/movie-watchlist-deploy.yaml
```
