ARG VARIANT="3.6"
FROM python:$VARIANT

ARG USERNAME="appuser"
ARG USER_UID=2000
ARG USER_GID=$USER_UID

# requiremnets install
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

# update system
RUN apt-get update 

# user groups
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
    && chmod 0440 /etc/sudoers.d/$USERNAME 

# user home dir
ENV HOME /home/$USERNAME

# copy project dir
COPY . /home/$USERNAME/etl-project-template

# run as user
USER $USERNAME


