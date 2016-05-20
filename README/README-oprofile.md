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

--callgraph

samples  %        image name               symbol name
  197       0.1548  cg                       main
  127036   99.8452  cg                       repeat
84590    42.5084  libc-2.3.2.so            strfry
  84590    66.4838  libc-2.3.2.so            strfry [self]
  39169    30.7850  libc-2.3.2.so            random_r
  3475      2.7312  libc-2.3.2.so            __i686.get_pc_thunk.bx
-------------------------------------------------------------------------------

Function()
    The non-indented line is the function we're focussing upon. This line is the same as you'd get from a normal opreport output.

Caller()
    Above the non-indented line, its the caller()
    samples:  number of times we took a sample whenever we found this caller() in the stack.
    percentage: related to all other callers()
    These values are not actual call counts.
    if a call is found in the stack at the time of a sample, it is recorded in this count

Callees()
    Below the non-indented line, are callees().
    
    [self]
        sample: is the normal sample count
        percentage: relative to all other callees() under this function. 
        This allows you to compare time spent in the function itself compared to functions it calls


## Annotate

        opannotate --source --demangle smart --exclude-dependent --output-dir ./temp/ cpu:2
        
...
               :static uint64_t pop_buffer_value(struct transient * trans)
 11510  1.9661 :{ /* pop_buffer_value total:  89901 15.3566 */
               :        uint64_t val;
               :
 10227  1.7469 :        if (!trans->remaining) {
               :                fprintf(stderr, "BUG: popping empty buffer !\n");
               :                exit(EXIT_FAILURE);
               :        }
               :
               :        val = get_buffer_value(trans->buffer, 0);
  2281  0.3896 :        trans->remaining--;
  2296  0.3922 :        trans->buffer += kernel_pointer_size;
               :        return val;
 10454  1.7857 :}
...


<Sample>  <relative percentage of total samples> : <Code>
        

    


# 3. Event Counter
collect raw event counts on per-application/per-process/per-cpu/system-wide basis
usefull when you want to see CPI(cycles per instraction) for an application only
  
    ocount [ options ] [ --system-wide | --process-list <pids> | --thread-list <tids> | --cpu-list <cpus> [ command [ args ] ] ]

Example:
    ocount --events=CPU_CLK_UNHALTED,INST_RETIRED my_test_program my_arg

To know possible options for --events
    ophelp

        ocount --separate-thread --process-list 27815 --time-interval 1 --events CPU_CLK_UNHALTED
        ocount -p 27815 --time-interval 1 --separate-thread --events=LLC_MISSES
        ocount -p 27815 --time-interval 1 --separate-thread --events=l2_lines_out:0x06
        
        
        
