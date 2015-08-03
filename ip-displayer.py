#!/usr/bin/python
# demo.py - CMD Args Demo By nixCraft
import sys,RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
GPIO.output(26,GPIO.HIGH)
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
	return t	
def display_number(t,pins):
	for pin in pins :
		GPIO.setup(pin,GPIO.OUT)
	for p in pins:
		if t[0]==1:
			GPIO.output(p,GPIO.HIGH)
		else:
			GPIO.output(p,GPIO.LOW)		
		t=t[1:]
	time.sleep(1)
def display_dot():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26,GPIO.OUT)
	GPIO.output(26,GPIO.LOW)
def display_letter(flag):
	pass;		
argument = []
argument.append(sys.argv[1])
argument.append(sys.argv[-1])
for ip in argument:
	s = str(ip)
	x = s.split('.')
	pins = [5,6,13,19]
	print x
	for i in x:
		count=0
		digits = digit_splitter(int(i))
		for digit in digits:
			temp=binary(digit)
			display_number(temp,pins)
			count+=1
		GPIO.cleanup()
		display_dot()	
		time.sleep(2)
		GPIO.output(26,GPIO.HIGH)

