import time
import os

def write_log(log_file, log):

    if os.path.exists(log):
        write = 'a'
    else:
        write = 'w'

    with open(log_file, write) as f:
        f.write(' '.join([str(m) for m in log])+'\n')
        f.close()


def generate_log(ts, tf, tput, avg_tput, req_bitrate, server_ip, chunkname):

    current_time = time.time()
    duration = tf-ts

    log = [current_time
           , duration
           , tput
           , avg_tput
           , req_bitrate
           , server_ip
           , chunkname
           ]

    return log