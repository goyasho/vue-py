FROM node:12.14

ARG project_dir=/web/app/frontend
WORKDIR $project_dir

COPY package*.json .

RUN yarn

#ARG project_dir=/web/app/backend
#
#RUN yum install -y \
#    python3 \
#    git \
#    wget
#RUN wget https://bootstrap.pypa.io/get-pip.py
#RUN python3 get-pip.py
#
#WORKDIR $project_dir
#ADD requirements.txt $project_dir
#RUN pip3 install -r requirements.txt

