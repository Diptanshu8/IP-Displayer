import RPi.GPIO as GPIO
import time
def binary(n):
	t = []
	if n >9:
		return [0,0,0,0]
	while n>0:
		t.append(n%2)
		n = n/2
	t.reverse()
	z = bitadjuster(t)
	return z
def bitadjuster(s):
	if len(s) < 4:
		for i in xrange(4-len(s)):
			s.insert(0,0)
	return s

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

#x = input("Enter the number:")
print 'Hi'
x = 0
while 1:
	if x > 9:
		x =  0
	s = binary(x)
	print s
	if s[0] == 1:
		GPIO.output(17,GPIO.HIGH)
		GPIO.output(5,GPIO.HIGH)
		GPIO.output(26,GPIO.HIGH)
	else:
		GPIO.output(5,GPIO.LOW)
		GPIO.output(17,GPIO.LOW)
		GPIO.output(26,GPIO.LOW)
	if s[1]==1:
		GPIO.output(6,GPIO.HIGH)
		GPIO.output(18,GPIO.HIGH)
		GPIO.output(16,GPIO.HIGH)
	else:
		GPIO.output(6,GPIO.LOW)
		GPIO.output(18,GPIO.LOW)
		GPIO.output(16,GPIO.LOW)
	if s[2]==1:
		GPIO.output(13,GPIO.HIGH)
		GPIO.output(27,GPIO.HIGH)
		GPIO.output(20,GPIO.HIGH)
	else:
		GPIO.output(13,GPIO.LOW)
		GPIO.output(27,GPIO.LOW)
		GPIO.output(20,GPIO.LOW)
	if s[3]==1:
		GPIO.output(19,GPIO.HIGH)
		GPIO.output(22,GPIO.HIGH)
		GPIO.output(21,GPIO.HIGH)
	else:
		GPIO.output(21,GPIO.LOW)
		GPIO.output(19,GPIO.LOW)
		GPIO.output(22,GPIO.LOW)
	time.sleep(1)
	x+=1

