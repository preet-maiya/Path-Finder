import sys,time,math
import matplotlib.pyplot as plt
from bt_proximity import BluetoothRSSI
t = time.time()
mini=100
maxi=-100
x=[]
y=[]
elapsed = 0.0
t1 = 0.0
dist = 0.0
if len(sys.argv)<2:
	print "usage: python bluetoothRSSI <address>"
else:
    while 1:
        try:
            rssi = BluetoothRSSI(addr = sys.argv[1])
            value = float(rssi.get_rssi())
            if value != 0:
                if mini>value:
                    mini = value
                if maxi<value:
                    maxi = value
		t1 = time.time()
		elapsed = elapsed + (t1 - t)
                print value," after time ",elapsed," seconds"
                t = time.time()
		dist = math.pow(10,-value) 
		x.append(elapsed)
		y.append(value)
        except KeyboardInterrupt:
            print "Minimum: ",mini," Maximum: ",maxi
	    plt.plot(x,y, marker='o')
	    plt.show()
	    bins = range(int(min(y)),int(max(y)))
	    plt.hist(y)
	    plt.show()
            sys.exit(0)
 
