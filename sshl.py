#!/usr/bin/env python3
# sshl.py
# diphia@2021, refactored@2022
# This script is used to show the saved ssh targets

def parse_lines(lines):
    """ parse a list of lines to Host object

    >>> target = ["Host router", "    HostName 10.0.0.1", "    User root", "    Port 22", "    IdentityFile /Users/diphia/.ssh/id_rsa"]
    >>> router = parse_lines(target)
    >>> print(router)
    router: root@10.0.0.1:22
    """
    dict = {}
    for l in lines:
        segments = l.strip().split(" ")
        key, value = segments[0].lower(), segments[1].lower()
        dict[key] = value
    if not 'port' in dict: dict['port'] = '22'
    if not 'identityfile' in dict: dict['identityfile'] = ""
    if not 'preferredauthentications' in dict: dict['preferredauthentications'] = ""
    return Host(dict.get('host'), dict.get('hostname'), dict.get('user'), dict.get('port'), dict.get('identityfile'), dict.get('preferredauthentications'))

def slice_file(config_file):
    """ slice whole file, return a list of segments shaped in list

    >>> file = open("/Users/diphia/temp/ssh_config_test", 'r', encoding = "UTF-8")
    >>> segments = slice_file(file)
    >>> print(parse_lines(segments[0]))
    router: root@10.0.0.1:22
    >>> print(parse_lines(segments[1]))
    hecs: diphia@124.71.123.123:22
    >>> file.close()
    """
    segment, result = [], []
    for l in config_file:
        if l.split(' ')[0] == 'Host' and segment:
            result.append((list(segment)))
            segment = []
        segment.append(l)
    result.append((list(segment)))
    return result

class Host:
    """

    >>> router = Host("router", "10.0.0.1", "root")
    >>> router
    < Host router >
    >>> print(router)
    router: root@10.0.0.1:22
    >>> remote_mac = Host("remote_mac", "17.0.0.1", "diphia", 6022)
    >>> print(remote_mac)
    remote_mac: diphia@17.0.0.1:6022
    """
    def __init__(self, label, hostname, user, port = '22', identity_file = "", preferred_authentications = "publickey"):
        self.label = label
        self.hostname = hostname
        self.user = user
        self.port = port

    def show_with_align(self):
        port_output = "" if self.port == '22' else ":{}".format(self.port)
        return "{}: {} @ {}{}".format(self.label[:10].ljust(10), self.user, self.hostname, port_output)

    def __repr__(self):
        return "< Host {} >".format(self.label)

    def __str__(self):
        return "{}: {}@{}:{}".format(self.label, self.user, self.hostname, self.port)

if __name__=="__main__":
    path = "/Users/diphia/.ssh/config"
    with open(path) as f:
        slices = slice_file(f)
        host_objects = map(parse_lines, slices)
        for host in host_objects:
            print(host.show_with_align())
