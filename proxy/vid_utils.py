import re


def bits(s):

	return len(s)*8.0

def parse_f4m(data):

	#media = re.search('(?<=<media)((.|\n|\r)*)>', data)
	bitrates = re.findall('(?<=bitrate=\")[0-9]+(?=\")', data)

	return [int(b) for b in bitrates]

def modify_uri_bitrate(request, bitrate):

	return re.sub(r'[0-9]+(?=Seg[0-9]+\-Frag[0-9]+)', str(bitrate), request)

def throughput_to_bitrate(tp, bitrates):

	pass


