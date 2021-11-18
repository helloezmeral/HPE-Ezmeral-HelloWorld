# setup registry to azure


```
image=bluedata/kd-api-serving:1.4
registry=hpelabimageregistry.azurecr.io

docker pull ${image}
docker tag ${image} ${registry}/${image}
docker push ${registry}/${image}
```

