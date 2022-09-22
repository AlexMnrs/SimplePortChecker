import sys
import socket


def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return True
    except:
        return False


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("\n")
        print("[*] Error: missing arguments")
        print(
            f"[*] Usage: python3 {sys.argv[0]} [ip address] [port]")
        sys.exit(1)

ip = sys.argv[1]
port = sys.argv[2]
status = isOpen(ip, port)

if status:
    print("Port " + port + " is open")
else:
    print("Port " + port + " is closed")
