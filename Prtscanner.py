import socket
import termcolor
import pyfiglet


def scan(target, ports):
    print('\n' + "[!]Starting scan for %s" % (str(target)))
    for port in range(1, ports):
        scan_port_status(target, port)


def scan_port_status(ipaddress, port):
    try:
        port_name = str(socket.getservbyport(port, protocol))
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(termcolor.colored("[+] Port %s Is Open (%s)" % (str(port), port_name), 'green'))
        sock.close()
    except:
        if filter_cports.lower() == "no":
            print(termcolor.colored("[-] Port %s Is Closed!" % (str(port)), 'red'))
        else:
            pass


ascii_banner = pyfiglet.figlet_format("Simple PortScanner !")
print(ascii_banner)
targets = input("[!]Enter targers to scan seperated by [,]: ")
ports = int(input("[!]Enter amount of ports to scan: "))
protocol = 'tcp'
filter_cports = str(input("[?]Would you like to filter closed ports ? (Yes/No)\n"))

if ',' in targets:
    print("[!]Scanning multiple targets...")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    print("[!]Scanning the target...")
    scan(targets, ports)
