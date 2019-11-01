import time

def write_log(log_file, log):

    with open(log_file) as f:
        f.write(' '.join([str(m) for m in log]))


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