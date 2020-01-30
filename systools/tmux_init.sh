#!/bin/bash
# tmux_init.sh
# diphia@2019
# This script is used to start tmux with speciffic windows and panes

cd ~
tmux new-session -s main -d 
#tmux split-window -v 'ipython'
#tmux split-window -h
tmux rename-window "code"
#tmux split-window -v
tmux new-window -n "note" 
tmux new-window -n "test"
tmux new-window -n "config"
tmux new-window -n "service" 
tmux new-window -n "remote" 
tmux select-window -t 1
tmux -2 attach-session -t main
