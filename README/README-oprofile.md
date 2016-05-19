OProfile is a set of performance monitoring tools for Linux 2.6 and higher systems

OProfile provides the following features:

- Profiler
- Post-processing tools for analyzing profile data
- Event counter

OProfile is capable of monitoring native hardware events
OProfile can collect event information for the whole system in the background with very little overhead
OProfile's event counting tool can collect simple raw event counts.

It can profile a single event or all running process in the system (--system-wide ->root permission required)
perf interfaces with the kernel to collect samples via the Linux Kernel Performance Events Subsystem (hereafter referred to as "perf_events")

# 1. Profiler

With operf, there is no initial setup needed -- 
simply invoke operf with the options you need
    operf [ options ] [ --system-wide | --pid=<PID> | [ command [ args ] ] ]


# 2. Post Processing

# 3. Event Counter
collect raw event counts on per-application/per-process/per-cpu/system-wide basis
usefull when you want to see CPI(cycles per instraction) for an application only
  
    ocount [ options ] [ --system-wide | --process-list <pids> | --thread-list <tids> | --cpu-list <cpus> [ command [ args ] ] ]

Example:
    ocount --events=CPU_CLK_UNHALTED,INST_RETIRED my_test_program my_arg

To know possible options for --events
    ophelp


