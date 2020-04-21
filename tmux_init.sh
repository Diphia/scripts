#!/bin/bash
# tmux_init.sh
# diphia@2019
# This script is used to start tmux with speciffic windows and panes

cd /home/diphia/scripts
tmux new-session -s main -d 
tmux rename-window "code"

cd /home/diphia/Westfall
tmux new-window -n "note" 

cd /home/diphia/test
tmux new-window -n "test"

cd /home/diphia/dotfiles
tmux new-window -n "config"

cd /home/diphia/Westfall
tmux new-window -n "service" 

#cd ~
#tmux new-window -n "remote" 

#cd ~
#tmux new-window -n "vigtd" 

tmux select-window -t 1
tmux -2 attach-session -t main
