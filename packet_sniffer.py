from scapy.all import *


def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_mac = packet.src
        dst_mac = packet.dst

        print(f"Source IP: {src_ip} [{src_mac}] --> Destination IP: {dst_ip} [{dst_mac}]")


def main():
    conf.L3socket = L3RawSocket
    sniff(prn=packet_callback, store=0)


if __name__ == "__main__":
    main()
