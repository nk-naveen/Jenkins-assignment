FROM ubuntu 
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt install openjdk-11-jdk git openssh-server unzip awscli -y
RUN mkdir -p /run/sshd
RUN wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip

RUN unzip aws-sam-cli-linux-x86_64.zip -d sam-installation RUN./sam-installation/install
RUN rm -rf aws-sam-cli-linux-x86_64.zip

EXPOSE 22 
CMD ["/usr/sbin/sshd", "-D"]