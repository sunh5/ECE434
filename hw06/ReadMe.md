# Homework04
-------
# Watch RT

1. Where does Julia Cartwright work?
She works at National Insstruments
2. What is PREEMT_RT? Hint: Google it.
PREEMT_RT is real-time kernel patch
3. What is mixed criticality?
Mixed criticality is that the system may run in two type of tasks, one is real-time task and another is non-real-time task.
4. How can drivers misbehave?
Driver misbehave is the driver involved in the process of delivering an interrupt. 
5. What is ? in Figure 1?
Delta is the latency, which is the time differnece between the thread wake up and thread really scheduled. 
6. What is Cyclictest[2]?
Cyclictest can accurately and repeatedly measures the difference between a thread's intended wake-up time and the time at which it actually wakes up in order to provide statistics about the system's latencies.
7. What is plotted in Figure 2?
It's preempt and preempt_rt latencies histogram. 
8. What is dispatch latency? Scheduling latency?
Dispatch latency describes the amount of time a system takes to respond to a request for a process to begin operation. 
Scheduling latency is the time between the last instruction of the user's interrupt handler and the execution of the first instruction of a driver thread.
9. What is mainline?
Mainline is the timeline of interrupt executed. 
10. What is keeping the External event in Figure 3 from starting?
Longest running interrupt handler.
Non critical IRQ
11. Why can the External event in Figure 4 start sooner?
Because the external event begins by interrpting non critical IRQ. 


# PREEMPT_RT
The four images for latencies measurement are in the file, which show the latencies with and without load in RT and non RT kernel. 
I used the led makefile and the makefile I wrote in last homework for the load. We can see clearly from images, RT kernel doesn't have bounded latencies. 