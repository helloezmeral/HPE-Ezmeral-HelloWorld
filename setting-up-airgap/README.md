# Setting Up Airgap for ECP
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
sudo apt install docker-compose
```
2. Install Harbor
```
wget https://github.com/goharbor/harbor/releases/download/v2.2.2/harbor-offline-installer-v2.2.2.tgz & tar -vxf harbor-offline-installer-v2.2.2.tgz
cd harbor
cp harbor.yml.template harbor.yml
nano harbor.yml
# change your hostname, and other config
sudo ./install.sh
# and you will see
#  ----Harbor has been installed and started successfully.----
docker ps # (check container status)
# go to ip:80 to check harbor is running
```
### sample harbor.yml
- https://github.com/helloezmeral/HPE-Ezmeral-HelloWorld/blob/main/setting-up-airgap/harbor.yml
3. Download Ezmeral Images and Install it
```
wget https://ezmeral-platform-releases.s3.amazonaws.com/5.3.1/3043/images/k8s_container_metadata.txt
wget https://ezmeral-platform-releases.s3.amazonaws.com/5.3.1/3043/images/publish.sh
wget https://ezmeral-platform-releases-seoul.s3.ap-northeast-2.amazonaws.com/5.3.1/3043/images/images-07122021.tar
tar -vxf images.tar
  
# Move the Image to Harbor Image folder
cp k8s_container_metadata.txt publish.sh harbor/images
cd harbor/images
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

