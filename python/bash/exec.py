#!/usr/bin/python
import os
import re
import exceptions
import subprocess

def start_process(args):
    try:
        p = subprocess.Popen(args,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE)
        out, err = p.communicate()
        return (p.returncode, out, err)
    except exceptions.OSError:
        return (-1, None, None)



def do_get_iface_ip(iface) :
    """
    This function returns tuple - ip and mask that was assigned to the
    interface.
    """

    args = ["ifconfig", iface]
    ret, out, _err = start_process(args)

    if ret == 0:
        ip = re.search(r'inet addr:(\S+)', out)
        mask = re.search(r'Mask:(\S+)', out)
        if ip is not None and mask is not None:
            return (ip.group(1), mask.group(1))
        else:
            return ret


def do_get_routes():
    args = ["route", "-n"]
    ret, out, _err = start_process(args)

    if ret == 0:
        lines = out.splitlines()
        return lines

# Demo
val=do_get_iface_ip("eth0")
print val[0]+"/"+val[1]

routes=do_get_routes()
i = 0
for l in routes:
    print  l

