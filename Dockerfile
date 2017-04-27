FROM registry.centos.org/kbsingh/openshift-nginx:latest

USER root

RUN yum -y install python-pip python-devel gcc git &&\
    cd /opt &&\
    git clone https://github.com/syamgk/status-api &&\
    cd status-api && pip install -r requirements.txt &&\
    yum -y remove python-devel git; yum clean all

ADD root /

RUN chown -R 1001:0 /opt/status-api  &&\
    chmod -R ug+rw /opt/status-api &&\
    chmod 777 /run.sh


USER 1001
WORKDIR /opt/status-api
EXPOSE 8080

ENTRYPOINT ["/run.sh"]
