#!./venv/bin/python3

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from mne.io import read_raw_edf, concatenate_raws
from mne.datasets import eegbci
from mne import find_events, pick_channels, Epochs
from mne.preprocessing import create_eog_epochs
import numpy as np

import sys

if __name__ == "__main__":
	subject = 1
	runs = [6, 10, 14]

	raw_fnames = eegbci.load_data(subject, runs)
	raw_files = [read_raw_edf(f, preload=True, stim_channel='auto') for f in raw_fnames]
	raw = concatenate_raws(raw_files)
	raw.rename_channels(lambda x: x.strip('.'))

	raw.filter(None, 50., l_trans_bandwidth='auto', h_trans_bandwidth='auto', filter_length='auto', phase='zero')

	event_ids = dict(hands=2, feet=3)
	events = find_events(raw, shortest_event=0, stim_channel='STI 014')
	epochs = Epochs(raw, events, event_ids, baseline=None, preload=True)

	print(epochs)

	raw.plot(n_channels=65, title='Raw data ploting', show=True, block=True)

	# e_1 = epochs['1'].get_data()
	# e_2 = epochs['2'].get_data()
	# e_3 = epochs['3'].get_data()

	# channel = 10
	# plt.plot(e_1[1][channel], color='b')
	# plt.plot(e_2[1][channel], color='r')
	# plt.plot(e_3[1][channel], color='g')
	# plt.xlabel('time(s)')
	# plt.legend(['T0', 'T1', 'T2'])
	# plt.show()

	# raw.pick_types(eeg=True,meg=False, stim=False, eog=False, exclude='bads').plot(n_channels=64, block=True)
	# epochs = mne.Epochs(raw, events, event_id=1, tmin=-1, tmax=4, proj=True, picks=picks, baseline=(None, 0), preload=True, reject=reject)
	# raw.filter(7., 30., fir_design='firwin', skip_by_annotation='edsge')
