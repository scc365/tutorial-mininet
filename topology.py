from mininet.topo import Topo

class TutorialTopology(Topo):

    def build(self):
        numOfHosts = 10
        numOfSwitches = 2
        hosts = []
        switches = []
        
        # Add hosts to the network.
        for i in range(numOfHosts):
            hosts.append(self.addHost("h" + str(i)))

        # Add a switch to the network.
        for i in range(numOfSwitches):
            switches.append(self.addSwitch("s" + str(i)))

        # Add a links between the host on the left and switch on the left.
        for i in range(numOfHosts):
            if(i < numOfHosts / 2):
                self.addLink(hosts[i], switches[0])
            else:
                self.addLink(hosts[i], switches[1])
        
        # Add the link between the switches.
        self.addLink(switches[0], switches[1])
        
class NewTopology(Topo):

    def build(self):
        numOfHosts = 4
        numOfSwitches = 2
        hosts = []
        switches = []
        
        # Add hosts to the network.
        for i in range(numOfHosts):
            hosts.append(self.addHost("h" + str(i)))

        # Add a switch to the network.
        for i in range(numOfSwitches):
            switches.append(self.addSwitch("s" + str(i)))

        # Add a links between the host on the left and switch on the left.
        for i in range(numOfHosts):
            if(i < numOfHosts / 2):
                self.addLink(hosts[i], switches[0])
            else:
                self.addLink(hosts[i], switches[1])
                
        # Add the link between the switches.
        self.addLink(switches[0], switches[1])

# The topologies accessible to the mn tool's '--topo' flag.
# note: if using the Dockerfile, this must be the same as in the Dockerfile.
topos = {
            "tutorialTopology": (lambda: TutorialTopology()),
            "newTopology": (lambda: NewTopology())
        }