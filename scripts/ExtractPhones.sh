
if [ "$#" -ne 3 ]; then
   echo ""
   echo "$0: Extract phone sounds from utterances";
   echo "USAGE: $0 Phone OutputDirectory IsFromPraat";
   echo "EXAMPLE: $0 i: phones_out/ 1";
   exit 1
fi



phone=$1
outdir=$2
isFromPraat=$3

for lab in lab/*.lab; do
  base=$(basename $lab .lab)
  python ../get_phone_audio.py $lab wav/$base.wav "$phone" $2 $isFromPraat
done

