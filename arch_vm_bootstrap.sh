xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
xrandr --addmode Virtual1 1920x1080_60.00
xrandr --output Virtual1 --mode 1920x1080_60.00
xrandr --dpi 150

sudo ip link set enp0s3 up && sudo dhcpcd enp0s3
sudo ip link set enp0s8 up && sudo dhcpcd enp0s8

VBoxClient-all && sudo mount -t vboxsf iCloudDrive /mnt/icloud && cd /mnt/shared_download && sudo mount -t vboxsf Downloads /mnt/shared_download
