# setup registry to azure
<img width="633" alt="image" src="https://user-images.githubusercontent.com/72959956/143213838-2b1f74dc-b7a9-45eb-9236-b70dc7c8011c.png">


```
image=bluedata/kd-api-serving:1.4
registry=hpelabimageregistry.azurecr.io

docker pull ${image}
docker tag ${image} ${registry}/${image}
docker push ${registry}/${image}
```
![image](https://user-images.githubusercontent.com/72959956/142351755-542ad51e-7c2e-4f5a-ada2-e50e0f4fcfa1.png)
![image](https://user-images.githubusercontent.com/72959956/142351794-05796971-ebaf-4d57-9d5f-f1137bf40d0d.png)


Full list
- bluedata/hpecp-agent:1.1.5
- bluedata/hpecp-bootstrap-hpecp-agent:1.1.5-1
- bluedata/hpecp-bootstrap-hpecp-monitoring:6.6.5-6.0
- bluedata/hpecp-bootstrap-kube-state-metrics:1.9.6-1
- bluedata/hpecp-bootstrap-kubedirector:1.7.2-1
- bluedata/hpecp-bootstrap-tools:0.4
- bluedata/kubedirector:0.5.3
- bluedata/metricbeat:6.6.5-2.0
- quay.io/coreos/kube-state-metrics:v1.9.6

MLOps
- bluedata/kd-notebook:1.15
- bluedata/kd-api-serving:1.3
- bluedata/kd-api-serving:1.4
- bluedata/hpecp-dtap:1.6.7


Spark (You don't have the needed permissions to perform this operation)
- gcr.io/mapr-252711/spark-hs-2.4.4:202009090453C
- gcr.io/mapr-252711/tenantcli-6.1.0:202009090453C
- gcr.io/mapr-252711/hivemeta-2.3:202007091835C
