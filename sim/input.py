# -*- coding: utf-8 -*-
import serial
from serial.tools import list_ports


# Processes input from the Teensy-augmented PS4 controller.
class TeensyInputController:
    
    # [x,y,z] accelerometer data
    imu = [0] * 3
    
    # [x,y] of finger position in touchpad
    tpad = [0] * 2
    
    # Array of booleans
    buttons = [False] * 15
    
    # [x,y] of left joystick position
    joy_left = [0] * 2
    
    # [x,y] of right joystick position
    joy_right = [0] * 2
    
    # displacement of left trigger
    trig_left = 0
    
    # displacement of right trigger
    trig_right = 0
    
    # Integer 0-7 for direction clockwise from noon; 8 for no press
    dpad = 0
    
    __ser = None
    
    def __init__(self):
        pass
    
    # Look for a COM port and try to connect to it.
    # returns True if successfully connected; False otherwise
    def connect(self, baud_rate = 1000000):
        # Gets a list of available devices
        ports = list_ports.comports()
        
        # If there are no devices return None
        if (len(ports) == 0):
            return "No port found"
        
        # Try to connect to first port
        try:
            self.__ser = serial.Serial(ports[0].device, baud_rate)
            return True
        except:
            return False
    
    # Close any open COM port
    def close(self):
        if self.__ser != None:
            self.__ser.close()
    
    # Update data fields by reading a new packet from the controller
    def read(self, autoconnect = True):
        try:
            # Read a packet, then discard the others - the controllers feeds
            # much too quickly for the python, and we need to make sure the
            # buffer doesn't fill. This does introduce latency, but whatever
            packet = self.__ser.readline().decode('utf-8')
            self.__ser.reset_input_buffer()
            
            # Split the comma-separated data into fields
            data = packet.split(',')
            self.imu = data[0:3]            # [x, y, z] Accel
            self.tpad = data[3:5]           # [x, y] of touch location
            self.buttons = data[5]          # Bit array
            self.joy_left = data[6:8]       # [x, y]
            self.joy_right = data[8:10]     # [x, y]
            self.trig_left = data[10]
            self.trig_right = data[11]
            self.dpad = data[12]            # dpad is 0-8 clockwise from noon
            return True
        
        except:
            return False

