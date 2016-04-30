sudo apt-get install cgroup-bin libcgroup1
ls /sys/fs/cgroup/
<in linux other than ubuntu> #sudo mount -t cgroup none /mnt

cpu : this subsystem uses the scheduler to provide cgroup processes access to the CPU.
cpuacct : this subsystem generates automatic reports on CPU resources used by processes in a cgroup.
memory : this subsystem sets limits on memory use by processes in a cgroup, and generates automatic reports on memory resources used by those processes.


soumyadc@soumyadc-V:~$ cat /proc/cgroups
#subsys_name    hierarchy       num_cgroups     enabled
cpuset  2       7       1
cpu     3       7       1
cpuacct 4       7       1
memory  5       11      1
devices 6       7       1
freezer 7       7       1
net_cls 8       7       1
blkio   9       7       1
perf_event      10      7       1
net_prio        11      7       1
hugetlb 12      7       1

# Example: Create 2 cgroups called Browsers and Multimedia

We’ll create 2 control groups called Browsers and Multimedia and we’ll set cgropus so that Browsers can use at max half the shares of CPU used by Multimedia
To do it we have 2 ways, working on the filesystem and using some special commands from the command line

## Method 1: Use the media-filesystem of cgroups

### step 1: create 2 cgroups

Its nothing more than a directory in the filesystem
    soumyadc@soumyadc-V:~$ sudo mkdir -p /sys/fs/cgroup/cpu/Browser
    soumyadc@soumyadc-V:~$ sudo mkdir -p /sys/fs/cgroup/cpu/Multimedia

### step 2: set the cpu weightage for the cgroups

we want Multimedia to have 2x weightage than Browser
this is done by creating the cpu.shares file inside the cgroup

    echo 2048 > /sys/fs/cgroup/cpu/Multimedia/cpu.shares
    echo 2048 > /sys/fs/cgroup/cpu/Browser/cpu.shares

### step 3: Define which processes belongs to cgroup Multimedia and Browser explicitly

    firefox &
    sudo echo $! >/sys/fs/cgroup/cpu/Browser/tasks

    rhythmbox & >/dev/null
    sudo echo $! >/sys/fs/cgroup/cpu/Multimedia/tasks




## Method 2: Using cgcreate command

### step 1: creating cgroups

    cgcreate -t uid:gid -a uid:gid -g subsystems:path

    sudo cgcreate -g cpu:/Browser
    sudo cgcreate -g cpu:/Multimedia

### step 2: set the cpu weightage for the cgroups (using cgset)

    cgset -r parameter=value path_to_cgroup

    sudo cgset -r cpu.shares=1024 Browser
    sudo cgset -r cpu.shares=512 Multimedia

### step 3: Move a process to cgroup (using cgclassify)

    cgclassify -g subsystems:path_to_cgroup pidlist

    sudo cgclassify -g cpu:Browser 8010
    sudo cgclassify -g cpu:Multimedia 8011

