Notes:

Currently browser needs to be refreshed 3 times to start streaming. It doesn't
seem to request after receiving objects. 


Files:

socket_utils.py
---------------

receive - Receive messages from connections

socket_bind_listen -  bind to an address and port, then listen

socket_bind_connect -  bind to a fake address and port and connect to server


vid_utils.py
-------------

bits - Calculate bits in message

calc_tp - Calculate throughput

ewma - Calculate exponential moving average

is_vid_request - Check if a video fragment name is inside string

get_chunkname - Get the name of the video chunk

get_req_bitrate - Get the requested bit rate

parse_f4m - Parse the f4m file for available bitrates

modify_uri_bitrate - Modify the requested bitrate
    

proxy
------
Proxy - proxy class that implements a proxy server