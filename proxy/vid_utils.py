import re


def bits(s):
    return len(s) * 8.0


def calc_tp(ts, tf, n_bits):

    return n_bits/1000.0/(tf-ts)

def ewma(current, new, alpha):

    if current<0:
        current = new

    return alpha * new + current * (1 - alpha)


def is_vid_request(string):
    return bool(re.match('\/vod\/[0-9]+Seg[0-9]+-Frag[0-9]+', string))

def get_chunkname(request):
    return re.search(r'\/vod\/[0-9]+Seg[0-9]+-Frag[0-9]+', request).group()

def get_req_bitrate(request):
    return re.search('(?<=\/vod\/)[0-9]+', request).group()

def parse_f4m(data):
    # media = re.search('(?<=<media)((.|\n|\r)*)>', data)
    bitrates = re.findall('(?<=bitrate=\")[0-9]+(?=\")', data)

    return [int(b) for b in bitrates]

def modify_uri_bitrate(request, bitrate):
    return re.sub(r'[0-9]+(?=Seg[0-9]+\-Frag[0-9]+)', str(bitrate), request)



