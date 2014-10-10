import sys


class SpeechLabel:
    audioFile = ""
    labelFile = ""
    labelData = []
    
    def __init__(self,  labelFile,  audioFile,  labelFromPraat=False):
        self.audioFile = audioFile
        self.labelFile = labelFile
            
        self.labelData = self.__LoadLabelFile(labelFile,  labelFromPraat)
    
    '''
    Load label file into memory
    '''
    def __LoadLabelFile(self, labelFile="",  labelFromPraat=False):
        
        if labelFromPraat == True:
            delimeter = ","
        else:
            delimeter = " "        
        
        if labelFile == "":
            labelFile = this.labelFile
        
        
        f = open(labelFile)
        labels = f.read().split("\n")
        
        # We don't care about the last element and the first element
        labels.pop()
        labels.pop(0)
        
        if labelFromPraat == False:
        # Split into format [start time] [number] [phone]
            for i in range(0, len(labels)-1):
                labels[i] = labels[i].split(delimeter);
                labels[i][0] = float(labels[i][0])
            
        
            # Convert into format [start time] [end time] [phone]
            for i in range(0, len(labels)-1):
                labels[i][1] = labels[i][0]
                if i == 0:
                    labels[i][0] = 0
                else:
                    labels[i][0] = labels[i-1][1]
            
            
            labels.pop()
        else:
            #Already in [start time] [end time] [phone] format
            for i in range(0, len(labels)-1):
                labels[i] = labels[i].split(delimeter);
                labels[i][0] = float(labels[i][0])
                labels[i][1] = float(labels[i][1])
        
        
        return labels
        

    '''
    Get Timestamps of phone in label
    '''
    def GetPhoneTimestamp(self, phone):
        labels = []
        for data in self.labelData:
            if phone == data[2]:
                labels.append(data)
                
        return labels







    def StripWavFile(self, startTime, endTime, saveAsFilename="",  minTime=-1):
        import wave
        w = wave.open(self.audioFile)
        params = w.getparams()
        fs = params[2]
        nframes = params[3]
        startFrame = int(max(0, fs * float(startTime)))
        endFrame = int(min(nframes,  float(fs*endTime)))
        
        if minTime > -1:
            if endTime - startTime < minTime:
                return False
                        
        if saveAsFilename == "":
            return False

        w.setpos(startFrame)
        phoneWav = w.readframes(endFrame-startFrame)
        w.close()
        
        outWav = wave.open(saveAsFilename,  'w')
        outWav.setparams(params)
        outWav.writeframes(phoneWav)
        outWav.close()
        
        return True
