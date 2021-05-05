# Ways to Interact with Ezmeral K8s
Last edit: May 2021

# Summary
[![png](https://github.com/helloezmeral/cdn/blob/main/HelloWorld%20with%20EPIC%20MLOps.png?raw=true)](https://helloezmeral.github.io/cdn/interact.pdf)

---
# 1. kubectl with plugins (kubectl-hpecp)
## Resources
- https://docs.containerplatform.hpe.com/53/reference/kubernetes/using-kubernetes/Using_the_HPE_Kubectl_Plugin.html?hl=kubectl

## Getting Started
### install
```bash
wget https://bluedata-releases.s3.amazonaws.com/kubectl-epic/3.4/14/linux/kubectl-hpecp.star
tar xf kubectl-hpecp.star
# move the file to the path
kubectl plugin list
wget https://storage.googleapis.com/kubernetes-release/release/v1.18.6/bin/linux/amd64/kubectl
# move the file to the path
```
### usage
```bash
# install the kubectl
curl -LO "<https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl>"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
# or
snap install kubectl --classic
# or
wget https://storage.googleapis.com/kubernetes-release/release/v1.18.6/bin/linux/amd64/kubectl
chmod +x kubectl


# install HPE-kubectl
kubectl plugin list
wget https://bluedata-releases.s3.amazonaws.com/kubectl-epic/3.4/14/linux/kubectl-hpecp.star
tar xf kubectl-hpecp.star

# move the file to PATH
sudo mv ./kubectl-hpecp /usr/local/bin
kubectl plugin list
kubectl hpecp -h
kubectl hpecp version	
kubectl hpecp version --output=yaml

# kubeconfig
kubectl hpecp refresh 172.16.10.41 --insecure --hpecp-user=your_username --hpecp-pass=your-pass
kubectl hpecp refresh ez53-gateway.hpeilab.com --insecure --hpecp-user=your_username --hpecp-pass=your-pass
kubectl hpecp refresh ez53-gateway.hpeilab.com --insecure

export KUBECONFIG="/home/hpeadmin/.kube/.hpecp/ez53-gateway.hpeilab.com/config"
KUBECONFIG="/home/hpeadmin/.kube/.hpecp/ez53-gateway.hpeilab.com/config:/home/hpeadmin/.kube/config" kubectl config view
```

### Alternative using kubeconfig file
- This is a temperary method, the key will expire
- download the file, view it inside the browser and copy to the bash
```
hpeadmin@awb51:~/myAWB/app01/deliverables$ nano kubeconfig
hpeadmin@awb51:~/myAWB/app01/deliverables$ export KUBECONFIG=./kubeconfig 
hpeadmin@awb51:~/myAWB/app01/deliverables$ kubectl get pods

save the kubeconfig file
export KUBECONFIG="kubeconfig"
kubectl get pods
```

### Kubedirector
```
# these are running application
kubectl get KubeDirectorCluster
kubectl delete  KubeDirectorCluster codeserver

```


---
# 2. REST APIs
## Resources
- https://docs.containerplatform.hpe.com/53/reference/accessing-the-applications/API_Access.html
- https://github.com/HewlettPackard/hpe-notebooks/tree/master/HPECPAPI
- https://github.com/bluedatainc/solutions/tree/master/APIs

## Getting Started
### HPECPAPI notes

```bash
curl -k -i -s --request POST "http://ez53-gateway.hpeilab.com:8080/api/v2/session" \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "username",
"password": "password",
"tenant_name": "test-tenant"
}'

#
HTTP/1.1 201 Created
Access-Control-Allow-Origin: *
Content-Length: 13
Content-Type: text/plain
Date: Fri, 30 Apr 2021 13:18:38 GMT
Location: /api/v2/session/thisisthesessionid
Server: HPE Ezmeral Container Platform 5.3

201 Created
```
```bash
curl -k -s --request GET "http://ez53-gateway.hpeilab.com:8080/api/v2/k8skubeconfig" \
--header "X-BDS-SESSION: /api/v2/session/dac075f6-5bcf-4f3d-9a22-5dd0bf67a804" \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' > ./kubeconfig

export KUBECONFIG=kubeconfig
```


### code
```bash
curl -k -s --request GET "http://ez53-gateway.hpeilab.com:8080/api/v2/k8skubeconfig" \
--header "X-BDS-SESSION: $(curl -k -i -s --request POST "http://ez53-gateway.hpeilab.com:8080/api/v2/session" \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "change-your-user-name",
"password": "change-your-user-password",
"tenant_name": "change-the-tenant-you-want"
}' | grep Location | awk '{print $2}' | tr -d '\r')" \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' > ./kubeconfig

export KUBECONFIG="./kubeconfig"

kubectl get pods
```


---
# 3. hpecp python library
## Resources
- https://github.com/hpe-container-platform-community/hpecp-python-library
- https://hpe-container-platform-community.github.io/hpecp-python-library/hpecp.license.html
- https://pypi.org/project/hpecp/
## Getting Started
