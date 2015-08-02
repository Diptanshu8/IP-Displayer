#!/usr/bin/python
# demo.py - CMD Args Demo By nixCraft
import sys,RPi.GPIO as pin

pin.setmode(pin.BCM)
def bit_balancer(bit):
	if len(bit)<4:
		for i in xrange(4-len(bit)):
			bit.insert(0,'0')
	return bit

def binary(n):
	t= n
	bit = []
	while n>0:
		bit.append(str(n%2))
		n = n/2
	bit.reverse()
	b = bit_balancer(bit)
	print "%d ---  %r"%(t,b)

def digit_splitter(n):
	t=[]
	while n>0:
		t.append(str(n%10))
		n=n/10
	t.reverse()
	if len(t)<3:
		for i in xrange(3-len(t)):
			t.insert(0,'0')
	for i in t:
		binary(int(i))	
print sys.argv[1]
s = str(sys.argv[1])
x = s.split('.')
for i in x:
	digit_splitter(int(i))

