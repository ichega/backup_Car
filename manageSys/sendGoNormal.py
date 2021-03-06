# -*- coding: utf-8 -*-

import serial
import time
import math
import os
import sys
import struct

def send_motion(way):
	if way == 'up':
		msg = [0xF0, 0x02, 0x30, 0x01, 0x31]
	elif way == 'left':
		msg = [0xF0, 0x02, 0x31, 0xFF, 0x30]
	elif way == 'down':
		msg = [0xF0, 0x02, 0x30, 0xFF, 0x2F]
	elif way == 'right':
		msg = [0xF0, 0x02, 0x31, 0x01, 0x32]
	print('push the button = ' + ''.join(map(chr,msg)))
	tty = '/dev/ttyUSB0'
	port = serial.Serial(tty, baudrate=9600, timeout=0)
	port.write(''.join(map(chr,msg)))
	
def send_stop(stop):
	if stop == ('up'):
		msg = [0xF0, 0x01, 0x20, 0x20]
	if stop == ('down'):
		msg = [0xF0, 0x01, 0x20, 0x20]	
	elif stop == ('left'):
		msg = [0xF0, 0x02, 0x31, 0x00, 0x31]
	elif stop == ('right'):
		msg = [0xF0, 0x02, 0x31, 0x00, 0x31]	
	print('push the button = ' + stop)
	tty = '/dev/ttyUSB0'
	port = serial.Serial(tty, baudrate=9600, timeout=0)
	port.write(''.join(map(chr,msg)))
	
def send_autoMot(what, value):
	if what == 'Go':
		msg = [0xF0, 0x05, 0x10]
		print('Go = ' + str(value) + ' metr')
		value = map(ord, struct.pack('<f', float(value)))
		checkSum = (0x10 + value[0] + value[1] + value[2] + value[3]) & 0xFF
		msg.extend(value)
		msg.append(checkSum)
	elif what == 'Turn':
		msg = [0xF0, 0x05, 0x11]
		print('Turn = ' + value + ' degreese')
		value = map(ord, struct.pack('<f', float(value)))
		checkSum = (0x11 + value[0] + value[1] + value[2] + value[3]) & 0xFF
		msg.extend(value)
		msg.append(checkSum)
	print(msg);
	tty = '/dev/ttyUSB0'
	port = serial.Serial(tty, baudrate=9600, timeout=0)
	port.write(''.join(map(chr, msg)))
	
def send_emerStop():
	print('EMERGENCY STOP!')
	msg = [0xF0, 0x01, 0x20, 0x20]
	tty = '/dev/ttyUSB0'
	port = serial.Serial(tty, baudrate=9600, timeout=0)
	port.write(''.join(map(chr,msg)))