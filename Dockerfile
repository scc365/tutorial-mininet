FROM ghcr.io/scc365/mn:latest
ARG topology
ENV TOPOLOGY ${topology}

RUN echo ${TOPOLOGY}

WORKDIR /topology
COPY topology.py .

CMD ["sh", "-c", "--custom /topology/topology.py --topo ${TOPOLOGY} --switch ovsk"]