# Setting Up Airgap for ECP

https://docs.containerplatform.hpe.com/53/reference/deploying-the-platform/phase-4/configuring-air-gap-K8s-host-settings.html

container registry is a must to host the container images. For rpm repo, as long as you can access the files via http or https should be ok, not necessarily be a proper centos yum repo server. Below are the rough steps:

Task 1: Container Registry Installation Steps\
l Step 1 wget https://github.com/goharbor/harbor/releases/download/v2.2.2/harbor-offline-installer-v2.2.2.tgz \
l Step 2 tar -vxf harbor-offline-installer-v2.2.2.tgz\
l Step 3 vim harbor.yml\
l Step 4 ./install.sh\
l Step 5 docker ps (check container status)\
l Step 6 download https://ezmeral-platform-releases.s3.amazonaws.com/5.3.1/3043/images/images.tar \
l Step 7 download https://ezmeral-platform-releases.s3.amazonaws.com/5.3.1/3043/images/k8s_container_metadata.txt \
l Step 8 download https://ezmeral-platform-releases.s3.amazonaws.com/5.3.1/3043/images/publish.sh \
l Step 9 tar -vxf images.tar\
l Step 10 cp k8s_container_metadata.txt publish.sh images\
l Step 11 cd images\
l Step 12 Harbor create project “ecp531”\
l Step 13 ./publish.sh load k8s_containet_metadata.txt harbor.local/ecp531

Task 2: RPM Server Installation Steps\
l Step 1 download https://bdk8s.s3.us-east-2.amazonaws.com/5.3/3031/k8s-rpms.tar \
l Step 2 install httpd server to Harbor server change default port to 18080\
l Step 3 chown 777 policy for httpd /\
l Step 4 check http://<harbor-server-ip>:18080 can download rpm files

===
1. Install Docker
```
sudo curl -fsSL https://get.docker.com -o get-docker.sh
DRY_RUN=0 sh ./get-docker.sh
  export PATH=/usr/bin:$PATH
  export DOCKER_HOST=unix:///run/user/1000/docker.sock
  
sudo apt install docker-compose
```
2. Install Harbor
```
wget https://github.com/goharbor/harbor/releases/download/v2.2.2/harbor-offline-installer-v2.2.2.tgz
tar -vxf harbor-offline-installer-v2.2.2.tgz
cd harbor
cp harbor.yml.template harbor.yml
nano harbor.yml
# change your hostname, and other config
sudo ./install.sh
# and you will see
#  ----Harbor has been installed and started successfully.----
docker ps # (check container status)
# go to ip:80 to check harbor is running with admin\password
```
### sample harbor.yml
- https://github.com/helloezmeral/HPE-Ezmeral-HelloWorld/blob/main/setting-up-airgap/harbor.yml
3. Download Ezmeral Images and Install it
```
wget https://ezmeral-platform-releases.s3.amazonaws.com/5.3.1/3043/images/k8s_container_metadata.txt
wget https://ezmeral-platform-releases.s3.amazonaws.com/5.3.1/3043/images/publish.sh
wget https://ezmeral-platform-releases-seoul.s3.ap-northeast-2.amazonaws.com/5.3.1/3043/images/images-07122021.tar
tar -vxf images-07122021.tar # this may take longer time to finish
nohup tar -vxf images-07122021.tar & # if you are running with putty, this can run the command in background and you are free to get a coffee break.
# or Press Ctrl - A then Ctrl - D . This will "detach" your screen session but leave your processes running.
  
# Move the Image to Harbor Image folder
cp k8s_container_metadata.txt publish.sh images 
cd images
# Create project ecp531
./publish.sh load k8s_containet_metadata.txt harbor.local/ecp531
# ./publish.sh load k8s_containet_metadata.txt registry.hpeilab.com/ecp531
```
 
## Possible Error
```
# if have error about /data
sudo mkdir /data
sudo chmod 777 /data
sudo ./install.sh
# docker: Error response from daemon: error while creating mount source path '/data': mkdir /data: read-only file system.
# 1. remove docker from snap
# 2. Install docker with apt
# sudo curl -fsSL https://get.docker.com -o get-docker.sh
# DRY_RUN=0 sh ./get-docker.sh
```


  # Possible solution
  https://docs.docker.com/registry/insecure/
  
  setup the registry with this configure
  
# Setting up Azure registry
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

  
  
  
  
  
  
