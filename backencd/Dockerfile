FROM centos:8

ARG project_dir=/web/app

RUN yum install -y \
    python3 \
    git \
    wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

WORKDIR $project_dir
ADD requirements.txt $project_dir
RUN pip3 install -r requirements.txt

#VOLUME ./app

#CMD ["python3", "-c", "print('Hello')"]
