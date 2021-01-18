h1 ping -c50 h4 >> results.txt
h1 iperf -s -p 5866 &
h4 iperf -c 10.0.0.1 -p 5866 -n 512m >> results.txt
h4 iperf -c 10.0.0.1 -p 5866 -n 512m >> results.txt
h4 iperf -c 10.0.0.1 -p 5866 -n 512m >> results.txt
