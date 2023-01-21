FROM ghcr.io/scc365/mn:latest

WORKDIR /topology
COPY topology.py .

CMD [ "--custom /topology/topology.py --topo tutorialTopology --switch ovsk --controller remote,ip=0.0.0.0,port=6633" ]
