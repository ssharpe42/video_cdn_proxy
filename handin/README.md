Files:

socket_utils.py
---------------
These functions deal with binding and connecting sockets and receiving data. 

receive - Receive messages from connections

socket_bind_listen -  bind to an address and port, then listen

socket_bind_connect -  bind to a fake address and port and connect to server


vid_utils.py
-------------
These functions perform calculations that relate to video streaming.

bits - Calculate bits in message

calc_tp - Calculate throughput

ewma - Calculate exponential moving average

is_vid_request - Check if a video fragment name is inside string

get_chunkname - Get the name of the video chunk

get_req_bitrate - Get the requested bit rate

parse_f4m - Parse the f4m file for available bitrates

modify_uri_bitrate - Modify the requested bitrate
    


io_utils.py
-------------
These functions aggregate and write log files. 

write_log - Write or append to log file

generate_log - Generate lines for log file

proxy
------
Proxy - proxy class that implements a proxy server