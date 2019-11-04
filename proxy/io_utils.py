import time
import os

def write_log(log_file, log):

    """
    Write or append to log file
    :param log_file: filename
    :param log: log from proxy
    :return:
    """

    if os.path.exists(log_file):
        write = 'a'
    else:
        write = 'w'

    with open(log_file, write) as f:
        f.write(' '.join([str(m) for m in log])+'\n')
        f.close()


def generate_log(ts, tf, tput, avg_tput, req_bitrate, server_ip, chunkname):

    """
    Generate lines for log file
    :param ts: start time
    :param tf: end time
    :param tput: throughput
    :param avg_tput: estimated throughput
    :param req_bitrate: requested bit rate
    :param server_ip: server ip
    :param chunkname: video chunk name
    :return: log iteration
    """
    current_time = round(time.time())
    duration = tf-ts

    log = [current_time
           , duration
           , int(tput)
           , int(avg_tput)
           , req_bitrate
           , server_ip
           , chunkname
           ]

    return log