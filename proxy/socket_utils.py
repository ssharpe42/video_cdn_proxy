
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import time



def receive(con_rec, con_send, max_size):

	"""
	Receive messages from connections

	:param con_rec: connection to receive from
	:param con_send: connection for sending (doesn't send just closes if needed)
	:param max_size: max number of bits to send
	:return:
	"""

	msg = '' # start with empty message
	#print 'recv from {}'.format(con_rec.getpeername())
	# If it is first packet not going to time in case we are waiting for server to send
	first = True

	while True:
		# recieve packet
		ts = time.time()
		packet = con_rec.recv(max_size)
		tf = time.time()-ts

		# append packet to message
		msg += packet

		# if EOM, break
		if '\n' in packet:
			break
		if len(packet) == 0:
			# if packet is empty, connection is disabled so close
			con_rec.close()
			con_send.close()
			print 'No data received. Closing connection.'
			break

	return msg


def socket_bind_listen(address, port):

	"""
	Create socket, bind to address and port, and listen

	:param address: ip address
	:param port: port
	:return: socket
	"""

	try:
		s = socket(AF_INET, SOCK_STREAM)
		s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		s.bind((address, port))
		s.listen(10)
		s.setblocking(0)
	except:
		return False

	return s

def socket_bind_connect(fake_addr, fake_port, server_addr, server_port):

	"""
	Create socket, bind to fake ip address and port, connect to server

	:param fake_addr: fake ip address
	:param fake_port: fake port
	:param server_addr: server ip address
	:param server_port: server port
	:return: socket
	"""

	try:
		s = socket(AF_INET, SOCK_STREAM)
		# s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		s.bind((fake_addr, fake_port))
		s.connect((server_addr, server_port))
		s.setblocking(0)

	except:
		return False

	return s
