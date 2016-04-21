#!/usr/bin/python

output = []
output.append("NXST_FLOW reply (xid=0x4):")
output.append("cookie=0x0, duration=30.625s, table=4, n_packets=0, n_bytes=2612, idle_timeout=180,priority=33000,in_port=1 actions=output:2")
output.append("cookie=0x0, duration=22.5s, table=4, n_packets=0, n_bytes=2612, idle_timeout=180,priority=33000,in_port=2 actions=output:1") 


print output


f = output[1]

print f
