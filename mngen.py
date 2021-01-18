#!/usr/bin/python

delays = ['10', '15', '20', '25']
bws = ['0.1','0.5','1','10','50','100']
losses = ['0','5','10','15','20']

#fin = open('sample-end.py', "r")
#data2 = fin.read()
#fin.close()

for delay in delays:
    for bw in bws:
        for loss in losses:
            delay2=str(int(delay)*2)
            fname = delay2 + '_' + bw + '_' + loss
            filename = fname + '.py'
            template = open('sample.py', 'rt').read()
            data = {"d": delay, "b": bw, "l": loss, "f": fname}
            with open (filename, 'wt') as output:
                output.write (template % data)
#            fout = open(filename, "a")
#            fout.write(data2)
#            fout.close()
