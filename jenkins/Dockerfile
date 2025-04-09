FROM jenkins/jenkins:lts

USER root

RUN curl -sfL -o docker.tgz "https://download.docker.com/linux/static/stable/x86_64/docker-27.2.0.tgz" && \
  tar -xzf docker.tgz --directory /usr/local/bin  docker/docker --strip=1 && \
  rm docker.tgz

RUN groupadd -g 1001 docker && usermod -aG docker jenkins

COPY --from=docker/buildx-bin /buildx /usr/libexec/docker/cli-plugins/docker-buildx

USER jenkins