#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
import threading
import pyaudio
import struct
import pickle
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 0.5

while True:
    try:
        address = ("127.0.0.1", 8440)
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(address)
        break
    except:
        print("retry to connect...")
        time.sleep(3)
        continue

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

while True:
    while len(data) < 8:
        data += sock.recv(81920)
    packed_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_size)[0]
    while len(data) < msg_size:
        data += self.sock.recv(81920)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frames = pickle.loads(frame_data)
    for frame in frames:
        self.stream.write(frame, CHUNK)