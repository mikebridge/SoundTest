#!/usr/bin/env python

## Note: need to install http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

import math
import wave
import struct
import matplotlib.pyplot as pyplot

frate = 44100.00
#amp = 8000.0
amp = 64000.0
datasize = 20000


def write_wav(notes, datasize=10000, fname="test.wav"):
    """
    :param frate:
    :param sine_set:
    :param datasize:
    :param fname:
    """
    wav_file = wave.open(fname, "w")
    nchannels = 1
    sampwidth = 2
    framerate = int(frate)
    nframes = datasize
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))
    for sine_set in notes:
        for s in sine_set:
            wav_file.writeframes(struct.pack('h', s))
    wav_file.close()

def synth_complex(freq=[440], coef=[1], datasize=10000):

    sine_list=[]

    for x in range(datasize):

        samp = 0
        for k in range(len(freq)):
            point = coef[k] * math.sin(2 * math.pi * freq[k] * (x / frate))
            samp += int(point * amp / 2) # combine amplified point

        sine_list.append(samp)

    return sine_list

notes = []

#sine_list1 = synth_complex(frate, [440,880,1200], [0.4,0.3,0.1], datasize)
sine_list1 = synth_complex([369, 440, 587, 880], [0.2, 0.2,0.3, 0.3], datasize)
#sine_list1 = synth_complex([369, 440, 587], [0.3, 0.4,0.3], datasize)
#sine_list1 = synth_complex([440, 466], [0.5,0.5], datasize)
sine_list2 = synth_complex([466], [1], datasize)


#sine_list2 = synth_complex(frate, [410,820,1230], [0.4,0.3,0.1], datasize)

pyplot.plot(sine_list1[0:5000])
#pyplot.plot(sine_list1)
#pyplot.show(block = False);

pyplot.savefig('test.png')

#pyplot.plot(sine_list2[0:1000])
#pyplot.show();

notes.append(sine_list1)
notes.append(sine_list2)

#write_raw([sine_list1, sine_list2], "tone.csv")

write_wav(notes, datasize, "tone.wav")