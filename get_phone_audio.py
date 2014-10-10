from SpeechLabel import SpeechLabel
import sys
import os

if (len(sys.argv)) != 6:
    print "USAGE: get_phone_audio.py [LABEL FILE] [AUDIO FILE] [PHONE] [OUTPUT AUDIO] [PRAAT LABEL FILE]"
    print "\t\t [LABEL FILE] is the path to the input label file."
    print "\t\t [AUDIO FILE] is the path to the input audio file."
    print "\t\t [PHONE] is the phone to extract."
    print "\t\t [OUTPUT AUDIO] is the location of the output audio files."
    print "\t\t [PRAAT LABEL FILE] 1 if label file generated from TextGrid, 0 otherwise."
    print "EXAMPLE: get_phone_audio.py 'lab/cw_0001.lab' 'wav/cw_0001.wav' 'i:' 0"
    sys.exit()

labelFile = sys.argv[1]
audioFile = sys.argv[2]
phone = sys.argv[3]
isPraatLabel = int(sys.argv[5])
audioOut = sys.argv[4]


labels = SpeechLabel(labelFile,  audioFile,  isPraatLabel)

eachLabel = labels.GetPhoneTimestamp(phone)

baseFilename = os.path.basename(labelFile).split(".")[0]
wavCounter = 0
for label in eachLabel:
    fileName = audioOut + "/" + baseFilename + "_" + str(wavCounter) + ".wav"
    if (labels.StripWavFile(label[0], label[1],  fileName, 0.1)):
        wavCounter += 1
    
