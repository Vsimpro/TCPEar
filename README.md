## TCP - Ear
Simple Tool with a horrible name,
that logs the TCP packets coming in to your machine. Specifically from port 22.

### Currently only works on ubuntu.

#### Modification into a specific use case.
Tracking any port is easy with just minor adjustments. On line 19, you'll find the main culprit of this crime,
> "sudo tcpdump -nlq "tcp[13] == 2 and dst port 22" | while read x; do echo "${x}"; echo -en \\a; done" 

by changing the number "-- dst port 22" | --" into the desired port number, i.e "-- dst port 23",
it will now begin to listen to TCP packets flowing into that port. You might also want to change this number a few lines below,
> log_dict(line, "22")

to have it write the port number into the .txt log.
