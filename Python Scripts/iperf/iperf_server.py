import iperf3

server = iperf3.Server()
server.bind_address = '10.10.10.15'
# server.port = 6969
server.verbose = False
while True:
    server.run()