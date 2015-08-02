#!/usr/bin/python
# demo.py - CMD Args Demo By nixCraft
import sys,RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

GPIO.setup(16,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)

def bit_balancer(bit):
	if len(bit)<4:
		for i in xrange(4-len(bit)):
			bit.insert(0,0)
	return bit

def binary(n):
	t= n
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
def first(t):
	if t[0]==1:
		GPIO.output(5,GPIO.HIGH)
	else:
		GPIO.output(5,GPIO.LOW)
	if t[1]==1:
                GPIO.output(6,GPIO.HIGH)
        else:
                GPIO.output(6,GPIO.LOW)
	if t[2]==1:
                GPIO.output(13,GPIO.HIGH)
        else:
                GPIO.output(13,GPIO.LOW)
	if t[3]==1:
                GPIO.output(19,GPIO.HIGH)
        else:
                GPIO.output(19,GPIO.LOW)

def second(t):
        if t[0]==1:
                GPIO.output(17,GPIO.HIGH)
        else:
                GPIO.output(17,GPIO.LOW)
        if t[1]==1:
                GPIO.output(18,GPIO.HIGH)
        else:
                GPIO.output(18,GPIO.LOW)
        if t[2]==1:
                GPIO.output(27,GPIO.HIGH)
        else:
                GPIO.output(27,GPIO.LOW)
        if t[3]==1:
                GPIO.output(22,GPIO.HIGH)
        else:
                GPIO.output(22,GPIO.LOW)

def third(t):
        if t[0]==1:
                GPIO.output(26,GPIO.HIGH)
        else:
                GPIO.output(26,GPIO.LOW)
        if t[1]==1:
                GPIO.output(16,GPIO.HIGH)
        else:
                GPIO.output(16,GPIO.LOW)
        if t[2]==1:
                GPIO.output(20,GPIO.HIGH)
        else:
                GPIO.output(20,GPIO.LOW)
        if t[3]==1:
                GPIO.output(21,GPIO.HIGH)
        else:
                GPIO.output(21,GPIO.LOW)

s = str(sys.argv[1])
x = s.split('.')
for i in x:
	t = digit_splitter(int(i))
	temp=binary(int(t[0]))
	first(temp)
	temp=binary(int(t[1]))
	second(temp)
	temp = binary(int(t[2]))
	third(temp)
	time.sleep(3)
GPIO.cleanup()
