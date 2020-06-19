#!/bin/bash
# tmux_init.sh
# diphia@2019
# This script is used to start tmux with speciffic windows and panes

tmux new-session -s main -d 
tmux rename-window "emacs"

cd /home/diphia/scripts
tmux new-window -n "temp" 

cd /home/diphia/Westfall
tmux new-window -n "service" 

#cd ~
#tmux new-window -n "remote" 

#cd ~
#tmux new-window -n "vigtd" 

tmux select-window -t 1
tmux -2 attach-session -t main
