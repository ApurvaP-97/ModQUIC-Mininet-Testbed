#!/usr/bin/python

import os
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

nombre = os.path.basename(__file__)


def myNetwork():
    
    net = Mininet( topo=None,
                  build=False,
                  ipBase='10.0.0.0/8')
            
    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                       controller=Controller,
                       protocol='tcp',
                       port=6633)

    info( '*** Add switches\n')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    
    info( '*** Add links\n')
    s1h1 = {'bw':%(b)s,'delay':'%(d)s','loss':%(l)s}
    net.addLink(h1, s1, cls=TCLink , **s1h1)
    s1h2 = {'bw':%(b)s,'delay':'%(d)s','loss':0}
    net.addLink(s1, h2, cls=TCLink , **s1h2)
    s2h3 = {'bw':%(b)s,'delay':'%(d)s','loss':0}
    net.addLink(s2, h3, cls=TCLink , **s2h3)
    s2h4 = {'bw':%(b)s,'delay':'%(d)s','loss':0}
    net.addLink(s2, h4, cls=TCLink , **s2h4)
    s1s2 = {'bw':1024,'delay':'0','loss':0}
    net.addLink(s1, s2, cls=TCLink , **s1s2)
    
    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s2').start([c0])
    net.get('s1').start([c0])

    info( '*** Post configure switches and hosts\n')

#    for i in range(0,3,1):
#        print h1.cmd('ping -c20 h2 >> %(f)s.txt')
#        print h1.cmd('iperf -s -p 5866 &')
#        print h2.cmd('iperf -c 10.0.0.1 -p 5866 -n 10240m >> %(f)s.txt')
    myScript = "test.sh"
    CLI(net, script=myScript)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

