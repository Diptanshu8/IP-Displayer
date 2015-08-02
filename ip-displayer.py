#!/usr/bin/python
# demo.py - CMD Args Demo By nixCraft
import sys,RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
def bit_balancer(bit):
	if len(bit)<4:
		for i in xrange(4-len(bit)):
			bit.insert(0,0)
	return bit

def binary(n):
	bit = []
	while n>0:
		bit.append(n%2)
		n = n/2
	bit.reverse()
	b = bit_balancer(bit)
	return b
def digit_splitter(n):
	t=[]
	while n>0:
		k = n % 10
		t.append(k)
		n=n/10
	t.reverse()
	if len(t)<3:
		for i in xrange(3-len(t)):
			t.insert(0,0)
	return t	
def display(t,pins):
	p_count =0
	for pin in pins :
		GPIO.setup(pin,GPIO.OUT)
	for i in t:
		print pins[p_count]
		if i==1:
			GPIO.output(pins[p_count],GPIO.HIGH)
		else:
			GPIO.output(pins[p_count],GPIO.LOW)
		p_count+=1
s = str(sys.argv[1])
x = s.split('.')
pins = [[5,6,13,19],[17,18,27,22],[26,16,20,21]]
for i in x:
	count=0
	print "i ="+ str(i)
	digits = digit_splitter(int(i))
	print len(digits)
	for digit in digits:
		temp=binary(digit)
		display(temp,pins[count])
		count+=1
	time.sleep(2)
GPIO.cleanup()
