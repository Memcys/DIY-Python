FROM python:3.10 as builder

COPY requirements.txt setup.py ./
COPY package package

# use the PyPI mirrior from BFSU. Substitute it by any mirrors nearby instead.
RUN pip install -i https://mirrors.bfsu.edu.cn/pypi/web/simple --user -U pip wheel
RUN pip install -i https://mirrors.bfsu.edu.cn/pypi/web/simple --user --no-warn-script-location -r requirements.txt
# RUN pip install --user -r requirements.txt


# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
# ARG VARIANT="3"
# FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

FROM fedora

# [Optional] Uncomment this section to install additional OS packages.
# RUN microdnf install -y \
#     sudo \
#     shadow-utils

RUN dnf install -y \
    graphviz
    
ARG USERNAME=pdm

# Creates a non-root user with an explicit UID and adds permission to access the work folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers

RUN adduser -u 5678 -m ${USERNAME}
# copy from last build the required packages
COPY --from=builder /root/.local /home/${USERNAME}/.local
RUN chown -R ${USERNAME} /home/${USERNAME}/.local
# RUN usermod -aG sudo ${USERNAME}
USER ${USERNAME}
ENV PATH=/home/${USERNAME}/.local/bin:${PATH}


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# port 8888 is the default port for jupyter
EXPOSE 8888

WORKDIR /home/${USERNAME}/code
COPY . .

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt       #    && rm -rf /tmp/pip-tmp


# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1
