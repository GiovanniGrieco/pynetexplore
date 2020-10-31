# netexplore

Netexplore is a basic ICMP-based network scanner to easily find hosts in a classic IPv4 network.

## Dependencies
Netexplore depends on [https://pypi.org/project/icmplib/](icmplib) to enable network scan in constrained environments, even if the classic `ping` utility is not available.

After cloning this repository, just issue the following command to install the aforementioned dependencies:
```bash
$ pip install -r requirements.txt
```