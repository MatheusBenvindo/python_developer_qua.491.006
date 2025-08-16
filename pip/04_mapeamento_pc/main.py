import os 
import platform
import psutil
import socket



print(f"Sistema Operacional: {platform.system()}, {platform.release()}")
print(f"Usuário: {os.environ.get("USERNAME")}")
print(f"IPV4: {socket.gethostbyname(socket.gethostname())}")

print(f"Portas abertas:\n ")
connectall = psutil.net_connections(kind="inet")
only_udp = [conn for conn in psutil.net_connections(kind="inet") if conn.type == socket.SOCK_DGRAM]

#separar as informações sobre as portas
only_tcp_listening_ports = [conn.laddr.port for conn in connectall if conn.status == psutil.CONN_LISTEN]
only_udp_listening_ports = [conn.laddr.port for conn in only_udp] #udp

#remover as portas repetidas da lista 
only_tcp_listening_ports = list(set (only_tcp_listening_ports))
only_udp_listening_ports = list(set (only_udp_listening_ports))

#organizar as portas na sequência
only_tcp_listening_ports.sort()
only_udp_listening_ports.sort()

print("Portas TCP:\n")
for port in only_tcp_listening_ports:
    print(f"Porta TCP: {port} ABERTA")

print("Portas UDP:\n")
for port in only_udp_listening_ports:
    print(f"Porta TCP: {port} ABERTA")