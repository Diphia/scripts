#!/usr/bin/env python3

import sys
import subprocess

def combine_path(prefix, file_path):
    return prefix + '/' + file_path

def path_convert(mount_info, path):
    """ convert the original path to remote
    >>> mount_info = {}
    >>> mount_info['Downloads'] = ['root@nas.lab.com', '/mnt/pool1/Downloads']
    >>> path_convert(mount_info, '/Volumes/Downloads/test1/test2')
    '/mnt/pool1/Downloads/test1/test2'
    >>> path_convert(mount_info, '/Users/diphia/temp/test.py')
    '/Users/diphia/temp/test.py'
    """
    path_segments = path.split('/') # ['', 'Volumes', 'Downloads', 'test1', 'test2']
    if len(path_segments) <= 2 or path_segments[1] != 'Volumes':
        return path
    drive = mount_info.get(path_segments[2]) # ['root@nas.lab.com', '/mnt/pool1/Downloads']
    if not drive:
        return path
    path_of_drive = drive[1] + '/' # '/mnt/pool1/Downloads/'
    path_after_drive = '/'.join([str(item) for item in path_segments[3:]]) # 'test1/test2'
    return path_of_drive + path_after_drive

def get_host(mount_info, path):
    """ get host
    >>> mount_info = {}
    >>> mount_info['Downloads'] = ['root@nas.lab.com', '/mnt/pool1/Downloads']
    >>> get_host(mount_info, '/Volumes/Downloads/test1/test2')
    'root@nas.lab.com'
    """
    path_segments = path.split('/') # ['', 'Volumes', 'Downloads', 'test1', 'test2']
    if len(path_segments) <= 2 or path_segments[1] != 'Volumes':
        return None
    drive = mount_info.get(path_segments[2]) # ['root@nas.lab.com', '/mnt/pool1/Downloads']
    if not drive:
        return None
    return drive[0]

def get_full_command(mount_info, file_path, target_path):
    """ get full command
    >>> mount_info = {}
    >>> mount_info['Downloads'] = ['root@nas.lab.com', '/mnt/pool1/Downloads']
    >>> mount_info['Videos'] = ['root@nas.lab.com', '/mnt/pool0/Videos']
    >>> get_full_command(mount_info, '/Volumes/Downloads/test1/test2', '/Volumes/Videos/temp/')
    'ssh root@nas.lab.com cp /mnt/pool1/Downloads/test1/test2 /mnt/pool0/Videos/temp/'
    """
    file_path_host = get_host(mount_info, file_path)
    target_path_host = get_host(mount_info, target_path)
    if not file_path_host or not target_path_host or file_path_host != target_path_host:
        return None
    else:
        host = file_path_host
    command = 'ssh {} cp -r {} {}'.format(host, path_convert(mount_info, file_path), path_convert(mount_info, target_path))
    return command


if __name__ == '__main__':
    mount_info = {}
    mount_info['Downloads'] = ['root@nas.lab.com', '/mnt/pool1/Downloads']
    mount_info['Videos'] = ['root@nas.lab.com', '/mnt/pool0/Videos']
    commands, file_paths = [], []
    path_prefix, target_path = sys.argv[1], sys.argv[-1]
    for item in sys.argv[2:-1]:
        file_paths.append(combine_path(path_prefix, item))
    for file_path in file_paths:
        commands.append(get_full_command(mount_info, file_path, target_path))
    for i in range(len(commands)):
        command = commands[i]
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        print('processing {}/{} : {}'.format(i+1, len(commands), command))
        process.wait()
        if process.returncode != 0:
            print(process.returncode)
