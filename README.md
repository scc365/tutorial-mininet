# Tutorial: Mininet

This tutorial looks at running emulated network topologies on your device using [Mininet](https://github.com/mininet/mininet). Network emulation allows you to test networks on your device that you would otherwise need access to a lot of real hardware to recreate, and it does so primarily though the use of network namespaces and software bridges. Mininet is a popular tool for creating emulated networks though simple Python scripts.

> ⏰ **Estimated Completion Time**: 1-2 Hours

## Getting Started

To complete this tutorial you should clone this repository onto the provided [virtual machine](https://github.com/scc365/virtual-machine):

```
git clone https://github.com/scc365/tutorial-mininet
cd ./tutorial-mininet
```

Alternatively you can use this as a _Template Repository_ if you wish to have a copy in your own GitHub profile.

> 🔗 You may find these [links](#links) useful throughout this tutorial

## Stages

This tutorial consists of seven stages, each of which building on the prior: 

  1. [Understanding the Topology](#stage-1-understanding-the-topology)
  2. [Running the Topology](#stage-2-running-the-topology)
  3. [Extending the Topology](#stage-3-extending-the-topology)
  4. [Basic Testing](#stage-4-basic-testing)
  5. [Multiple Topologies](#stage-5-multiple-topologies)
  6. [Adding Realism](#stage-6-adding-realism)
  7. [Welcome SDN](#stage-7-welcome-sdn)

## Tasks

To test your knowledge, some stages contain tasks. If you are completing this tutorial as part of the advanced networking module @ Lancaster University, you should complete these tasks so that you can get feedback from a TA.

  1. [More Hosts](#task-1-more-hosts)
  2. [More Switches](#task-2-more-switches)
  3. [Advanced Links](#task-3-adding-link-constraints)

---

## Stage 1: Understanding the Topology

This template provides you with a very basic topology (`./topology.py`) that, through Mininet, will produce an emulated network consisting of 1 host and 1 switch, connected via a virtual link. But what exactly does all that mean?

> 🔎 Think you know already? Go to the next step and get running the topology and see if it as you think!

So the basics, there are 4 fundamental components to a Mininet topology: Hosts, Switches, Links, and Controllers.

- **Hosts:** hosts in a Mininet topology on the surface act like computers. It gets its own terminal window where you can execute commands acting as that host. It gets other features too when in added to a topology with switches and links such as an IP address and ports that have MAC addresses.

- **Switches:** these are applications that can forward packets. Typically, by default these act like bridges, however, when using OpenFlow-enabled software switches (like Open vSwitch) the functionality can be dictated by the controller.

- **Links:** links act like the cables connecting nodes (hosts and switches) together. For these to exist, virtual interfaces (like ethernet ports) are created where necessary.

- **Controllers:** switches such as OvS switches that are OpenFlow-enabled need a controller to be the control plane to their data plane. These can be defined inside the Mininet topology definition, or controllers can be defined as `remote` (where are created outside Mininet, but accessible via a known IP:port).

## Stage 2: Running the Topology

> 🧑‍🏫 LU Students: This will be covered interactively in a lab session

The quickest way to get topologies running is via the `mn` command-line tool. You can run the provided minimal topology like so:

```bash
sudo mn --custom ./topology.py --topo tutorialTopology --switch ovsk
```

<details>
<summary>Do this with Docker 🐳</summary>
<br>
Build the container image (each time you make a change to the topology code):
<pre>
docker build --rm -t topology:latest .
</pre><br>
Run the container:
<pre>
docker run --rm -it --privileged --network host --name topology topology:latest
</pre><br>
</details>
<br>

> 🙋 The flag `--switch ovsk` just specifies the type of bridge to use by default in the topology. For scc365 course materials you should use this flag, however, feel free to investigate others.

You can see how you can use the other features provided by `mn` using its help function: `mn -h` (or see the man page [here](./MN.md)).

### Using `mn`

Once the topology has been created, you should see a prompt on your terminal that looks like this: `mininet> `. This interface will allow you to interact with the network and the nodes it contains. To see what commands are available in this interface, run the command: `help`.

You can see what nodes and links are in the topology via the `net` command. This lets you make sure that the topology you have instantiated is the one you expected. Similarly, `links` lets you check all the links connecting nodes are as you expected. To close the topology and exit the `mn` interface, you can run the `exit` command.

### Running Commands

When you have the topology running and the `mn` prompt (`mininet> `) available, you can not only run commands that `mn` supports, but can run commands acting as a host in the topology. This can be really useful when wanting to perform complex tests. Each node has access to any command available on the host system running the topology (or any command in the Docker image for those using Docker). To do this, simply add the name of the host before the command, for example: `h1 echo "Hello World!"` will run the `echo "Hello World"` command as `h1`.

## Stage 3: Extending the Topology

> 🧑‍🏫 LU Students: This will be covered interactively in a lab session

The topology provided is very minimal, containing only a single connected host and switch. Most topologies are far larger, so the given topology is of little use. In this stage you should attempt the 2 tasks presented to extend the topology with more nodes and switches.

> 💡 **Tip:** after each run of `mn`, run the command `sudo mn -c` to perform a cleanup to prevent some unexpected behavior. If using Docker, this is done automatically by the provided base image.

### Task 1: More Hosts

Modify the provided `topology.py` file to add 4 more hosts to the switch (`s1`). To check if you have completed the task, you should run the `net` and/or `links` commands and match the result with the answer below.

Remember, you can run commands as hosts if you want to run a particular test. E.g. if you want to check the full information of a `ping` between `h1` and `h4`, you can do so like: `h1 ping h4` from the `mn` prompt.

<details>
<summary>Answer ✅</summary>
<br>
Expected output from the <code>net</code> command:
<pre>
h1 h1-eth0:s1-eth1
h2 h2-eth0:s1-eth2
h3 h3-eth0:s1-eth3
h4 h4-eth0:s1-eth4
h5 h5-eth0:s1-eth5
s1 lo:  s1-eth1:h1-eth0 s1-eth2:h2-eth0 s1-eth3:h3-eth0 s1-eth4:h4-eth0 s1-eth5:h5-eth0
c0
</pre><br>
Expected output from the <code>links</code> command:
<pre>
h1-eth0<->s1-eth1 (OK OK) 
h2-eth0<->s1-eth2 (OK OK) 
h3-eth0<->s1-eth3 (OK OK) 
h4-eth0<->s1-eth4 (OK OK) 
h5-eth0<->s1-eth5 (OK OK)
</pre><br>
Expected output from the <code>pingall</code> command:
<pre>
h1 -> h2 h3 h4 h5 
h2 -> h1 h3 h4 h5 
h3 -> h1 h2 h4 h5 
h4 -> h1 h2 h3 h5 
h5 -> h1 h2 h3 h4 
*** Results: 0% dropped (20/20 received)
</pre><br>
</details>
<br>

### Task 2: More Switches

Now you should have a topology that has 5 hosts connected to a single switch. In this task, double this topology so that there are 2 switches, each with 5 unique hosts connected to them. These 2 switches should then be linked up.

Again, use the `net` and `links` commands to check that your solution is working as expected. Keep in mind that there might be some variability in node and port names when comparing your output to the answers below.

<details>
<summary>Answer ✅</summary>
<br>
Expected output from the <code>net</code> command:
<pre>
h1 h1-eth0:s1-eth1
h2 h2-eth0:s1-eth2
h3 h3-eth0:s1-eth3
h4 h4-eth0:s1-eth4
h5 h5-eth0:s1-eth5
h6 h6-eth0:s2-eth1
h7 h7-eth0:s2-eth2
h8 h8-eth0:s2-eth3
h9 h9-eth0:s2-eth4
h10 h10-eth0:s2-eth5
s1 lo:  s1-eth1:h1-eth0 s1-eth2:h2-eth0 s1-eth3:h3-eth0 s1-eth4:h4-eth0 s1-eth5:h5-eth0 s1-eth6:s2-eth6
s2 lo:  s2-eth1:h6-eth0 s2-eth2:h7-eth0 s2-eth3:h8-eth0 s2-eth4:h9-eth0 s2-eth5:h10-eth0 s2-eth6:s1-eth6
c0
</pre><br>
Expected output from the <code>links</code> command:
<pre>
h1-eth0<->s1-eth1 (OK OK) 
h2-eth0<->s1-eth2 (OK OK) 
h3-eth0<->s1-eth3 (OK OK) 
h4-eth0<->s1-eth4 (OK OK) 
h5-eth0<->s1-eth5 (OK OK) 
h6-eth0<->s2-eth1 (OK OK) 
h7-eth0<->s2-eth2 (OK OK) 
h8-eth0<->s2-eth3 (OK OK) 
h9-eth0<->s2-eth4 (OK OK) 
h10-eth0<->s2-eth5 (OK OK) 
s1-eth6<->s2-eth6 (OK OK)
</pre><br>
Expected output from the <code>pingall</code> command:
<pre>
h1 -> h2 h3 h4 h5 h6 h7 h8 h9 h10 
h2 -> h1 h3 h4 h5 h6 h7 h8 h9 h10 
h3 -> h1 h2 h4 h5 h6 h7 h8 h9 h10 
h4 -> h1 h2 h3 h5 h6 h7 h8 h9 h10 
h5 -> h1 h2 h3 h4 h6 h7 h8 h9 h10 
h6 -> h1 h2 h3 h4 h5 h7 h8 h9 h10 
h7 -> h1 h2 h3 h4 h5 h6 h8 h9 h10 
h8 -> h1 h2 h3 h4 h5 h6 h7 h9 h10 
h9 -> h1 h2 h3 h4 h5 h6 h7 h8 h10 
h10 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 
*** Results: 0% dropped (90/90 received)
</pre><br>
</details>
<br>

### Bonus Task

You may notice that the Python code for the tasks looks a little messy and repetitive. As this topology definition is written in Python, you can use normal programming logic too. For example, you can add nodes to arrays rather than declaring a separate variable for each, or you could use for loops for host creation etc...

This task has no specific answer, but you should attempt to use normal Python programming practices cleaning up your topology files from the prior 2 tasks.

## Stage 4: Basic Testing

Now that you have topologies that you've created yourself, you should test them to make sure they are running as you expect. Using the Mininet provided shortcut commands such as `pingall`, `net`, and `links` are a good way to get very quick information, but they lack some details that you may be interested in. Using the provided system to run commands as hosts mentioned [here](#running-commands), you can run the tests you would typically test networks with in Linux. Try using the tools below on the topology you created previously.

> 🧰 These tools are covered more in-depth in the [`Network Testing`](https://github.com/scc365/guide-network-testing) guide

### Testing Connectivity

To check the details regarding connectivity between 2 points in a network, you can run `ping` (`pingall` uses this in the background). Not only will `ping` provide you with a boolean answer to "can these 2 points communicate?", but it provides other metrics such as packet loss percentages and round trip times. Below is an example output from the `ping` command:

<details>
<summary>Running <code>ping</code> in Mininet 🏃</summary>
<pre>
mininet> h1 ping -c 5 h8
PING 10.0.0.8 (10.0.0.8) 56(84) bytes of data.
64 bytes from 10.0.0.8: icmp_seq=1 ttl=64 time=0.600 ms
64 bytes from 10.0.0.8: icmp_seq=2 ttl=64 time=0.106 ms
64 bytes from 10.0.0.8: icmp_seq=3 ttl=64 time=0.107 ms
64 bytes from 10.0.0.8: icmp_seq=4 ttl=64 time=0.227 ms
64 bytes from 10.0.0.8: icmp_seq=5 ttl=64 time=0.107 ms

--- 10.0.0.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4083ms
rtt min/avg/max/mdev = 0.106/0.229/0.600/0.191 ms
</pre><br>
</details>
<br>

This tells you firstly, that as packet loss is `0%`, these points (`h1` and `h8`) can communicate. Secondly, the average round trip time between the 2 points is `0.229ms`. And finally, another interesting point to note from the data, the first ping between the hosts was `0.6ms`, but the subsequent pings were around `0.1-0.2ms`. This gives us an indication that some connection setup logic was happening when the ping took place, but that logic established a faster connection for future communication.

> 🧰 See the `ping` guide [here](https://github.com/scc365/guide-network-testing/blob/main/ping/PING.md)!

### Testing Bandwidth

So like the `ping` command gives a measure of latency via its round trip time output, `iperf` (or `iperf3`) can give a measure of bandwidth between 2 points. Unlike `ping`  that just the sending client runs, `iperf` requires one node run an `iperf` server (e.g. `iperf3 -s`), and another a client that specifies the server to communicate with (e.g. `iperf3 -c h8 -p 5201`). 

<details>
<summary>Running <code>iperf</code> in Mininet 🏃</summary>
<pre>
mininet> h8 iperf3 -s &
-----------------------------------------------------------
Server listening on 5201
-----------------------------------------------------------

mininet> h1 iperf3 -c h8 -p 5201
Connecting to host 10.0.0.8, port 5201
[  4] local 10.0.0.1 port 44808 connected to 10.0.0.8 port 5201
[ ID] Interval           Transfer     Bandwidth       Retr  Cwnd
[  4]   0.00-1.00   sec  4.41 GBytes  37.8 Gbits/sec  1763   1.02 MBytes       
[  4]   1.00-2.00   sec  9.58 GBytes  82.3 Gbits/sec    0   1.02 MBytes       
[  4]   2.00-3.00   sec  8.56 GBytes  73.5 Gbits/sec    0   1.02 MBytes       
[  4]   3.00-4.00   sec  8.44 GBytes  72.4 Gbits/sec    0   1.02 MBytes       
[  4]   4.00-5.00   sec  8.33 GBytes  71.6 Gbits/sec    0   1.02 MBytes       
[  4]   5.00-6.00   sec  8.08 GBytes  69.4 Gbits/sec  200    730 KBytes       
[  4]   6.00-7.00   sec  8.35 GBytes  71.7 Gbits/sec  319    730 KBytes       
[  4]   7.00-8.00   sec  8.18 GBytes  70.3 Gbits/sec    0    730 KBytes       
[  4]   8.00-9.00   sec  8.34 GBytes  71.6 Gbits/sec    0    730 KBytes       
[  4]   9.00-10.00  sec  8.28 GBytes  71.1 Gbits/sec    0    730 KBytes       
- - - - - - - - - - - - - - - - - - - - - - - - -
[ ID] Interval           Transfer     Bandwidth       Retr
[  4]   0.00-10.00  sec  80.5 GBytes  69.2 Gbits/sec  2282             sender
[  4]   0.00-10.00  sec  80.5 GBytes  69.2 Gbits/sec                  receiver

iperf Done.
</pre><br>
</details>
<br>

This output tells us that the link between `h1` and `h8` has a maximum capacity of `69Gbps` (_nice_).

> 🧰 See the `iperf` guide [here](https://github.com/scc365/guide-network-testing/blob/main/iperf/IPERF.md)!

## Stage 5: Multiple Topologies

Sometimes you might need quick access to multiple topologies. Luckily, you can very easily define multiple topologies in `mn` topology files. 

At the bottom of your topology file, you should have noticed the `topos` variable being set to a dictionary that is populated with the name of your topology matched with the class that your topology is built within. If you have another class in the same file that extends `Topo`, you can just add to the `topos` dictionary:

<details>
<summary>Adding to the <code>topos</code> dictionary 📖</summary>
If you have a class that extends <code>Topo</code> called <code>MyNewExampleTopology</code>, you can add that to the <code>topos</code> dictionary:
<pre>
topos = { 
          'tutorialTopology': ( lambda: TutorialTopology() ),
          'newTopology': ( lambda: MyNewExampleTopology() ) 
        }
</pre>
Then you can just change the value used in the <code>--topo</code> flag to <code>newTopology</code> when running <code>mn</code> to chose the topology defined in <code>MyNewExampleTopology</code>.
</details>
<br>

## Stage 6: Adding Realism

So now you can run virtual networks on your devices that can vary in complexity. However, real networks typically have well-defined constraints and limitations, a trait not present in the topologies you have created thus far. For example, a hardware networking device such as a simple switch for a small home network might have 8 ports, each of which being limited to 1Gb. However, Mininet does provide a mechanism that allows **t**raffic **c**ontrol features to be applied to **link**s: `tclink`. In this, where you would typically define a link in a topology, you would add synthetic constraints. Below are some examples of setting these constraints within a Mininet topology file:

<details>
<summary>Import the TCLink class 🐍</summary>
<br>
At the top of your topology file, add the following line:
<pre>
from mininet.link import TCLink
</pre><br>
</details>
<br>

```python
# add a link between s1 and h1 with a max bandwidth of 100Mbps
self.addLink(h1, s1, cls=TCLink, bw=100)
```

```python
# add a link between s1 and h2 with a minimum delay of 75ms
self.addLink(h2, s1, cls=TCLink, delay='75ms')
```

```python
# add a link between s1 and h3 with 5% packet loss
self.addLink(h3, s1, cls=TCLink, loss=5)
```

Try adding these to your topology and check if they are working using common Linux networking tools:

 - You can test the bandwidth limits using `iperf`
 - You can test the delay and loss limits using `ping`

### Task 3: Adding Link Constraints

Working atop your topology from [task 2](#task-2-more-switches), add the following constraints to the link between the 2 switches:

 - Bandwidth: `50Mbps`
 - Latency: `30ms`
 - Loss: `10%`

Once you have done this, using the basic testing tools highlighted [in stage 4](#stage-4-basic-testing), confirm that the constraints are working as you expect.


## Stage 7: Welcome SDN

Using the `--switch ovsk` flag in the `mn` command tells Mininet to use Open vSwitch software bridges as the default switches in the topologies. These are OpenFlow enabled, an SDN protocol that improves network configurability. These devices do have default functionality as the topologies you have been running thus far have been working, however, further functionality can be added to these software bridges via an external OpenFlow controller. In Mininet, this is simply defined as using a _remote controller_.

A remote controller is specified in the `mn` CLI via the flag "`--controller remote`" and can also specify the IP address and Port number that the OpenFlow controller is listening via. For example, if an OpenFlow controller was running on a device with the IP address `10.50.50.33` and Port `6633`, this could be specified in the `mn` CLI like so:

```bash
sudo mn --custom ./topology.py --topo tutorialTopology \
--switch ovsk --controller remote,ip=10.50.50.33,port=6633
```

> 💡 **Note:** the `\` in the command above simply tells bash to allow the command to move onto the line below

To test this, you will first need to have access to a remote controller. Luckily there is a controller that you can use that provides functionality similar to that provided by default. To bring up this controller at `localhost:6633`, you simply need to run the following command:

```bash
sudo controller ptcp:6633
```

<details>
<summary>Do this with Docker 🐳</summary>
<br>
Just run the provided container image for the <code>ptcp</code> controller:
<pre>
docker run --rm -it --network host --name ptcp ghcr.io/scc365/ptcp:latest
</pre><br>
</details>
<br>

Next, modify your `mn` command to bring up the topology created as part of this tutorial's [tasks](#tasks) to use a remote controller found locally (`127.0.0.1`) at port `6633`. This should look the same or similar to:

```bash
sudo mn --custom ./topology.py --topo tutorialTopology \
--switch ovsk --controller remote,ip=127.0.0.1,port=6633
```

<details>
<summary>Do this with Docker 🐳</summary>
<br>
Add the controller remote flag to the Dockerfile's command:
<pre>
CMD [ "--custom /topology/topology.py --topo tutorialTopology --switch ovsk --controller remote,ip=127.0.0.1,port=6633" ]
</pre><br>
Build the container image (each time you make a change to the topology code):
<pre>
docker build --rm -t topology:latest .
</pre><br>
Run the container:
<pre>
docker run --rm -it --privileged --network host --name topology topology:latest
</pre><br>
</details>
<br>

Now your topology should act the same as it did prior to using a remote controller. But try running the topology with your updated `mn` command, but with no `ptcp` controller running.

<!-- TODO: Add Link to P4 Tutorial -->
For more on remote controllers with Mininet, see the [`Ryu Tutorial`](https://github.com/scc365/tutorial-ryu)


## Solution

Solutions for the tasks in this tutorial will be available [here](https://github.com/scc365/tutorial-solution-mininet) on GitHub (in week 12). However, this tutorial is not assessed and is designed to help you get familiar with Mininet, so make sure you make your own attempt at the tasks before looking at these solutions.

<!-- TODO: Upload Solution -->

## Submission & Feedback

You can submit your final solution to this tutorial via Moodle for some feedback. This must be done prior to the deadline on the submission point as no late solutions will be checked.

## Links
- The Mininet Source Code: [GitHub](https://github.com/mininet/mininet)
- Official Mininet Walkthrough: [Mininet.org](http://mininet.org/walkthrough/)
