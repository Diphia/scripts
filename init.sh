#!/bin/bash
# init.sh
# diphia@2019
# This script is used to initialize personal configurations on a newly deployed machine

username="diphia"

if [ ! -d "/home/${username}/scripts/" ]
then
	cd /home/${username}
	git clone git@github.com:Diphia/scripts.git
fi

if [ ! -d "/home/${username}/dotfiles/" ]
then
	cd /home/${username}
	git clone git@github.com:Diphia/dotfiles.git 
fi
#sed '6d' -i /home/${username}/dotfiles/dotfiles_setup.sh
sh /home/${username}/dotfiles/dotfiles_setup.sh
