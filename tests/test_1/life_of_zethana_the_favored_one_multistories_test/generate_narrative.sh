#!/bin/bash
# AI-Generated Narratives About The Favored One, eight of them!
# Execute while the shell's working directory is same directory as `the_favored_one.png` (this directory)
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")" 
pushd "${SCRIPT_DIR}" # actually I did it for you.
n=0
while [[ $n -lt 8 ]] ; do 
    echo "Write a detailed narrative on how a little infant girl grew up into the adulthood position as pictured in "'`'"$(pwd)/the_favored_one.png"'`'". Tell me her life story. Her name is Zethana and her title is The Favored One. Aim for a length of 5000 words." | ollama run gemma3:27b -- --nowordwrap | tee "tfo_narrative_${n}"
    n=$((n+1))
done
popd