#!/bin/env python3
from argparse import ArgumentParser
from ipaddress import IPv4Address, ip_network
from multiprocessing import Pool
from os import cpu_count

from icmplib import ping

def get_args():
    parser = ArgumentParser()

    parser.add_argument('cidr', type=str,
                        help='Target CIDR Address to scan.')

    return parser.parse_args()

def reach_host(ip_addr: IPv4Address):
    host_state = ping(ip_addr.exploded, count=1, interval=0.2, timeout=1)
    if host_state.is_alive:
        print(ip_addr)

def scan(cidr):
    net_addr = ip_network(cidr)

    with Pool(cpu_count()) as p:
        p.map(reach_host, net_addr.hosts())

if __name__ == '__main__':
    args = get_args()
    scan(args.cidr)
