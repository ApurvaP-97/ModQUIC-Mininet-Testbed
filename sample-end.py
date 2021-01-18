
    for i in range(0,3,1):
        print h1.cmd('ping -c20 h2 >> %s.txt' % nombre)
        print h1.cmd('iperf -s -p 5866 &')
        print h2.cmd('iperf -c 10.0.0.1 -p 5866 -n 10240m >> %s.txt' % nombre)
        #myScript = "test.sh"
        #CLI(net, script=myScript)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
