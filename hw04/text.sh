# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/boris.png

# From: http://www.imagemagick.org/Usage/text/
convert tux.png -background Grey  label:'Haoxuan Sun' -gravity Center -append tux.png
# convert -background lightblue -fill blue -font Times-Roman -pointsize 24 \
#       -size $SIZE \
#       label:'ImageMagick\nBoris\nby Haoxuan Sun' \
#       -draw "text 0,200 'ECE434 HW04'" \
#       $TMP_FILE
sudo fbi -noverbose -T 1 tux.png


