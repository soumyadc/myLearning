# Sample commands to use valgrind 

### use callgrind tool and show after the main function
    valgrind --trace-children=yes --tool=callgrind --show-below-main=yes xterm &

### use callgrind and dont start instrumentation at the start of the process 
    valgrind --trace-children=yes --tool=callgrind --instr-atstart=no xterm &

### dump before main function. usefull to trace the process startup area
    valgrind --trace-children=yes --tool=callgrind --dump-before=main xterm &

### dump after main(). Helpful to avoid unnecessarry dumps during process stratup 
    valgrind --trace-children=yes --tool=callgrind --dump-after=main xterm &

### dont instrument during process startup. and toggle instrumentation while executing func_test()
    valgrind --trace-children=yes --tool=callgrind --instr-atstart=no --toggle-collect=func_test xterm &

# callgrind_control

callgrind_control is a tool used to control the callgrind in the run time

### Dump the current backtrace
    callgrind_control -b
    callgrind_control -b -e

### toggling the instrumentation on|off
    callgrind_control -i on | off

    NOTE: it is useful if used along with -instr-atstart=no    

### Dump the profile data
    callgrind_control -d [hint [PID/Name]]
