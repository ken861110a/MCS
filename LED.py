#!/usr/bin/python
import requests
import socket
import threading
import logging
import RPi.GPIO as GPIO
# change this to the values from MCS web console
DEVICE_INFO = {
    'device_id' : 'DB1TNo8P',
    'device_key' : 'HKLjwIxe47sjXhS3'
}

# change 'INFO' to 'WARNING' to filter info messages
logging.basicConfig(level='INFO')

heartBeatTask = None

def establishCommandChannel():
    # Query command server's IP & port
