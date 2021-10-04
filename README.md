Docker Image creation steps
1.	Install docker at your linux machine 
# yum install docker

2.	Create a folder empty folder and place two thing in folder dockerfile and python code.
3.	Content of docker file - 
##### in case there is a scenario to just to trigger a container when ever required
 FROM python:3
RUN pip install requests
RUN groupadd -g 1000 basicuser && useradd -r -u 1000 -g basicuser basicuser
USER basicuser
WORKDIR /usr/src/app
COPY . .
CMD ["notification.py"]
ENTRYPOINT ["python3"] 
Description of docker file:- 
Line 1. taking python:3 image, using this image we will be creating light wait container. 
Line2.  Installing requests lib from pip command that lib is going to use in python script.
Line3. For security reason container should not run with root user so we are creating non root user.
Line4. Define here that code should run with this non root user.
Line5. Defined working directory where our script will run.
Line6. Copy all the continent in docker image. 
Line7. Define code that will run on container. 

################# in case there is a scenario to run the container/pod always and run python script periodically to query pull requests using cronjob

docker file content :------------------

FROM python:3.7
RUN apt-get update && apt-get -y install cron vim
RUN pip install requests
WORKDIR /app
COPY crontab /etc/cron.d/crontab
COPY  notification.py /app/notification.py
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
# run crond as main process of container
CMD ["cron", "-f"]

crontab file content

1 * * * * python /app/notification.py


4.	Docker image creation command. 
# docker build -t demo_final .
5.	Run the docker container for testing. 
#docker run -itd demo_final --entrypoint /bin/bash
6.	For doing deployment from Kubernetes, you have to push this image to docker hub registry. And from that registry you can deploy this container on your Kubernetes cluster. 
7.	Command to push docker image to the registry.
#docker push kandrup/demo_final:latest
#docker pull kandrup/demo_final:latest


###################### in case there is a scenario if Auth token should be passed as an env variable but not through python script then to run the docker container
now you need to provide an env variable at the run time of the container.
docker run -e "var1=ghp_0Di8eEjt4fMFB4lhCnZfhgfjjPnMdzfgUF2V3" -t -d --entrypoint /bin/bash kandrup/demo_final:latest.


