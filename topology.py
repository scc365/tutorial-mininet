from mininet.topo import Topo

class TutorialTopology(Topo):

    def build(self):
        # Sdd a host to the network.
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')

        # Add a switch to the network.
        s1 = self.addSwitch('s1')

        # Add a link between the host 'h1' and the 's1' switch.
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)
        self.addLink(h4, s1)
        self.addLink(h5, s1)

# The topologies accessible to the mn tool's '--topo' flag.
# note: if using the Dockerfile, this must be the same as in the Dockerfile.
topos = {'tutorialTopology': (lambda: TutorialTopology())}