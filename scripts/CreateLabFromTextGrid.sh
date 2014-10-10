for file in TextGrid/*.TextGrid; do  
  base=$(basename $file .TextGrid); 
  echo $base; 
  praat get_om_timestamps.praat lab/ TextGrid/ $base 1; 
done

