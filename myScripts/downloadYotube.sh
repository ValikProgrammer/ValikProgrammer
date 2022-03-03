#!/bin/bash
# tool to play audio :  sudo apt install sox && sudo apt install libsox-fmt-mp3 && sudo apt install libsox-fmt-all 
# play audio : play <audiofilename>
# tool to play video and audio: sudo apt install mpv  
# play <video> or play audio

# ===colors===
RED='\033[31m' # red
GREEN='\033[32m' # green
YELLOW='\033[33m'#'\033[33m' # orange
BLUE='\033[35m' # blue
UNDERLINED='\033[4m'
BOLD='\033[1m'
END='\033[0m' # simple text (stop colourful text)


audio=""
video=""
true="true"


print_usage() {
  echo "$RED Usage $END: sh $0 -flag[audio/video] arguments"
}

download_best_audio(){
    echo "$GREEN [audio] $END : $WARNING $1 $END"
    yt-dlp --ignore-errors -f 'ba' -x --audio-format mp3 $1


}
download_video1080(){
    echo "$GREEN [video] $END : $WARNING $1 $END"
    yt-dlp --ignore-errors -f "bestvideo[ext=mp4][height=1080]+bestaudio[ext=m4a]" $1
}

case "$1" in
  -video) video=true ;;
  -audio) audio=true ;;
    *) print_usage;;
esac
shift # так как флаг это тоже аргумент то он будет считаться усли мы не сдвинем аргументы

len=$# # len of arguments
echo $len
if [ "$audio" = "$true" ]
then
    echo "I am gonna dowload best $RED audio $END"
    for link in "$@" 
    do
        download_best_audio "${link}"
        len=$((len-1))
        echo "LEFT : $RED $len $END"
    done
elif [ "$video" = "$true" ]
then
    echo "I am gonna dowload $RED video $END in 1080"
    for link in "$@" 
    do
        download_video1080 "${link}"
    done
fi

# while getopts 'audio,video' flag; do
#   case "${flag}" in
#     audio) audio=true ;;
#     video) video=true ;;
#     *) print_usage
#        exit 1 ;;
#   esac
# done
