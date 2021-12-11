# Mininet: `mn`

`mn` - create a Mininet network. (`v2.3.0`)

---

## Synopsis

```
mn [options]
``` 

## Description

```
(type mn -h for details)

The  mn  utility creates Mininet network from the command line. It can create parametrized
topologies, invoke the Mininet CLI, and run tests.
```

## Options

```
-h, --help
      show this help message and exit

--switch=SWITCH
      default|ivs|lxbr|ovs|ovsbr|ovsk|user[,param=value...]               user=UserSwitch
      ovs=OVSSwitch   ovsbr=OVSBridge   ovsk=OVSSwitch   ivs=IVSSwitch   lxbr=LinuxBridge
      default=OVSSwitch

--host=HOST
      cfs|proc|rt[,param=value...]     proc=Host     rt=CPULimitedHost{'sched':     'rt'}
      cfs=CPULimitedHost{'sched': 'cfs'}

--controller=CONTROLLER
      default|none|nox|ovsc|ref|remote|ryu[,param=value...]                ref=Controller
      ovsc=OVSController         nox=NOX         remote=RemoteController          ryu=Ryu
      default=DefaultController none=NullController

--link=LINK
      default|ovs|tc|tcu[,param=value...] default=Link tc=TCLink tcu=TCULink ovs=OVSLink

--topo=TOPO
      linear|minimal|reversed|single|torus|tree[,param=value   ...]   minimal=MinimalTopo
      linear=LinearTopo     reversed=SingleSwitchReversedTopo     single=SingleSwitchTopo
      tree=TreeTopo torus=TorusTopo

-c, --clean
      clean and exit

--custom=CUSTOM
      read custom classes or params from .py file(s)

--test=TEST
      pingall|pingpair|iperf|iperfudp|all|none|build

-x, --xterms
      spawn xterms for each node

-i IPBASE, --ipbase=IPBASE
      base IP address for hosts

--mac  automatically set host MACs

--arp  set all-pairs ARP entries

-v VERBOSITY, --verbosity=VERBOSITY
      debug|info|output|warning|warn|error|critical

--innamespace
      sw and ctrl in namespace?

--listenport=LISTENPORT
      base port for passive switch listening

--nolistenport
      don't use passive listening port

--pre=PRE
      CLI script to run before tests

--post=POST
      CLI script to run after tests

--pin  pin hosts to CPU cores (requires --host cfs or --host rt)

--nat  [option=val...]  adds  a  NAT  to  the  topology that connects Mininet hosts to the
      physical network.  Warning: This may route any traffic on  the  machine  that  uses
      Mininet's  IP  subnet  into the Mininet network. If you need to change Mininet's IP
      subnet, see the --ipbase option.

--version
      prints the version and exits

-w, --wait
      wait for switches to connect

-t WAIT, --twait=WAIT
      timed wait (s) for switches to connect

--cluster=server1,server2...
      run on multiple servers (experimental!)

--placement=block|random
      node placement for --cluster (experimental!)
```
