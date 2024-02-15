#!/bin/bash

logfile=job_results.log

/usr/bin/echo "The script ran at the following time: $(/usr/bin/date)" > $logfile

#  Notes:
#  Line 3: Specifies that the file to log the output to is "job_results.log"
#  Line 5: Call the echo command to output this message in parenthesis into the "logfile"
#  After the time specified when scheduling the job using the "at" command (refer to instructions.txt", enter the command
#    "cat job_results.log" to print the output to the terminal, and the message above along with the chosen time shouldbe displayed.
