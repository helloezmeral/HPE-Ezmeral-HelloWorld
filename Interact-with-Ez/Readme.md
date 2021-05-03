# Ways to Interact with Ezmeral K8s
Last edit: May 2021

# Summary
[![png](https://github.com/helloezmeral/cdn/blob/main/HelloWorld%20with%20EPIC%20MLOps.png?raw=true)](https://helloezmeral.github.io/cdn/interact.pdf)

---
# 1. kubectl with plugins (kubectl-hpecp)
## Resources


---
# 2. REST APIs
## Resources
- https://docs.containerplatform.hpe.com/53/reference/accessing-the-applications/API_Access.html
- https://github.com/HewlettPackard/hpe-notebooks/tree/master/HPECPAPI

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
