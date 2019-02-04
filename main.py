#!./venv/bin/python3

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from mne.io import read_raw_edf
from mne import find_events
import numpy as np

import sys

if __name__ == "__main__":
	raw = read_raw_edf(sys.argv[1], preload=True, stim_channel='auto')
	print(raw)
	events = find_events(raw, initial_event=True)
	print(events)
	raw.plot(block=True, lowpass=40)
