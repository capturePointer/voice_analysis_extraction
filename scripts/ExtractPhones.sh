
if [ "$#" -ne 2 ]; then
   echo ""
   echo "$0: Extract phone sounds from utterances";
   echo "USAGE: $0 DataDirectory IsFromPraat";
   echo "EXAMPLE: $0 adapt_02/ 1";
   exit 1
fi


datadir=$1
isFromPraat=$2

for lab in $datadir/lab/*.lab; do
  base=$(basename $lab .lab)
  echo $lab
  python ../get_phone_audio.py $lab $datadir/wav/$base.wav "6:" $datadir/phone_out/en4 $isFromPraat
  python ../get_phone_audio.py $lab $datadir/wav/$base.wav "U\\" $datadir/phone_out/en13 $isFromPraat
  python ../get_phone_audio.py $lab $datadir/wav/$base.wav "i:" $datadir/phone_out/en16 $isFromPraat
  python ../get_phone_audio.py $lab $datadir/wav/$base.wav "o:" $datadir/phone_out/en20 $isFromPraat
  python ../get_phone_audio.py $lab $datadir/wav/$base.wav "}:" $datadir/phone_out/en25 $isFromPraat
  
done

