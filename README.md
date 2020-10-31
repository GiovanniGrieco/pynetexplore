# pyNetexplore

pyNetexplore is a basic ICMP-based network scanner to easily find hosts in a classic IPv4 network.

## Dependencies
Of course, Python 3.x is needed to run a script written in Python 3.x. Tested on Python 3.9.

Netexplore depends on [icmplib](https://github.com/ValentinBELYN/icmplib) to enable network scan in constrained environments, even if the classic `ping` utility is not available.

After cloning this repository, just issue the following command to install the aforementioned dependencies:
```bash
$ pip install -r requirements.txt
```

## Usage
Just issue `./netexplore.py --help` to look up requested arguments.
