#!/bin/bash

if [ "$#" -ne 3 ]; then
   echo ""
   echo "$0: Save TextGrid and audio files for a set of utterances";
   echo "USAGE: $0 RawTextDirectory AudioDirectory VoiceName";
   echo "EXAMPLE: $0 ../text/ ../wav/ ennz-cw-adapt_02-hsmm";
   exit 1
fi

textDir=$1
audioDor=$2
voice=$3
for file in $1*.txt; do
  base=$(basename $file .txt)
  echo $base
  # Save TextGrid
  wget "http://localhost:59125/process?INPUT_TEXT=`cat $file`&INPUT_TYPE=TEXT&OUTPUT_TYPE=PRAAT_TEXTGRID&LOCALE=en_NZ&VOICE=$3" -O TextGrid/$base.TextGrid

  # Save WAV
  wget "http://localhost:59125/process?INPUT_TEXT=`cat $file`&INPUT_TYPE=TEXT&OUTPUT_TYPE=AUDIO&LOCALE=en_NZ&AUDIO=WAVE_FILE&VOICE=$3" -O $2/$base.wav

done


