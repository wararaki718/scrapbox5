import socket


def main():
    domain = "localhost"

    ips = set()
    for info in socket.getaddrinfo(domain, None, family=socket.AF_INET, type=socket.SOCK_STREAM):
        print(info)
        ips.add(info[-1][0])
    
    print(ips)
    print("DONE")


if __name__ == "__main__":
    main()
