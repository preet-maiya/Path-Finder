import sys,time,math,numpy,collections
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
count = 0

def rssiCalc(arr):
	counter = collections.Counter(y)
	keys = counter.keys()
	maximum = 0
	for key in keys:
		if maximum<counter[key]:
			maximum = counter[key]
	total_count = 0
	total = 0
	for val in keys:
		if float(counter[val])/float(maximum) > .60:
			total += counter[val] * val
			total_count += counter[val]
	return float(total)/float(total_count)

if len(sys.argv)<2:
	print "usage: python bluetoothRSSI <address>"
else:
    while 1:
        try:
            rssi = BluetoothRSSI(addr = sys.argv[1])
            value = rssi.get_rssi()
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
		count += 1
        except KeyboardInterrupt:
            print "Minimum: ",mini," Maximum: ",maxi
	    print "Total readings: ",count
	    counter = collections.Counter(y)
	    print "RSSI VALUE: ",rssiCalc(y)
	    plt.plot(x,y, marker='o')
	    plt.show()
	    bins = max(y)-min(y)
	    plt.hist(y, bins=bins)
	    plt.show()
            sys.exit(0)
