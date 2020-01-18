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

## 以下の設定だと下記で起動する
## docker run -p 5000:5000 -v ${PWD}/app:/web/app --name vue-py vue-py:1.0
ENV FLASK_APP ./run.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
