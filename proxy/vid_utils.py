import re


def bits(s):
    """Calculate bits in message"""
    return len(s) * 8.0

def get_length(string):

    re.search('(?<=Content-Length:?\s)[0-9]+', string).group()


def calc_tp(ts, tf, n_bits):
    """
    Calculate throughput
    :param ts: start time
    :param tf: end time
    :param n_bits: bits transferred
    :return: kb/s
    """
    return n_bits / 1000.0 / (tf - ts)


def ewma(current, new, alpha):
    """
    Calculate exponential moving average
    :param current: current estimate
    :param new: new sample
    :param alpha: alpha
    :return: new estimate
    """

    return alpha * new + current * (1 - alpha)


def is_vid_request(string):
    """Check if a video fragment name is inside string"""
    return bool(re.search('\/vod\/[0-9]+Seg[0-9]+-Frag[0-9]+', string))


def get_chunkname(request):
    """Get the name of the video chunk"""
    return re.search(r'\/vod\/[0-9]+Seg[0-9]+-Frag[0-9]+', request).group()


def get_req_bitrate(request):
    """Get the requested bit rate"""
    return re.search('(?<=\/vod\/)[0-9]+', request).group()


def parse_f4m(data):
    """Parse the f4m file for available bitrates"""
    bitrates = re.findall('(?<=bitrate=\")[0-9]+(?=\")', data)

    return [int(b) for b in bitrates]


def modify_uri_bitrate(request, available_bitrates, tp_estimate):

    """
    Modify the requested bitrate
    :param request: original client request
    :param available_bitrates: available bitrates
    :param tp_estimate: current throughput estimate
    :return: new request
    """

    allowed_bitrates = [b for b in
                       available_bitrates if b <= tp_estimate / 1.5]

    if len(allowed_bitrates)==0:
        max_bitrate  = 10
    else:
        max_bitrate = max([b for b in
                           available_bitrates if b <= tp_estimate / 1.5])

    return re.sub(r'[0-9]+(?=Seg[0-9]+\-Frag[0-9]+)', str(max_bitrate), request)
