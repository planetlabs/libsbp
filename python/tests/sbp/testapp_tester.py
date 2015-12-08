#! /usr/bin/env python

"""
the :mod:`sbp.client.examples.udp` module contains an example of reading SBP
messages from a serial port and sending them to a UDP socket.
"""

import sys
import time
import argparse
from mux import msg
from sat_utils import arq
from sat_utils.arq import B6Arq
from sat_utils.sat_io import SatFile
from sat_utils.translator import TranslatorB6
from sbp.testapp import *

TESTAPP_TYPE = 41

def get_args():
    """
    Get and parse arguments.
    """
    parser = argparse.ArgumentParser(description="Demonstrate SBP Testapp Messages...")
    parser.add_argument("-p", "--ping",
                        action="store_true",
                        default=False,
                        help="Send the TestappPing message.")

    parser.add_argument("-c", "--setcounter",
                        type=int,
                        default=-1,
                        help="Send the TestappSetCounter message.")

    parser.add_argument("-m", "--setmany",
                        nargs=6,
                        help="Send the TestappSetMany message.")

    parser.add_argument("-f", "--setfixed",
                        type=int,
                        nargs=5,
                        help="Send the TestappFixedArrayMsg message.")

    parser.add_argument("-v", "--setvariable",
                        type=int,
                        nargs='*',
                        help="Send the TestappVariableArrayMsg message.")

    parser.add_argument("-s", "--state",
                        action="store_true",
                        default=False,
                        help="Send the TestappState message.")
    return parser


def main():
    parser = get_args()
    args = parser.parse_args()
    print(args)

    if args.ping:
        p = TestappPing()

    elif args.setcounter >= 0:
        p = TestappSetCounter(counter_value=args.setcounter)

    elif args.setmany:
        a = int(args.setmany[0])
        b = int(args.setmany[1])
        c = float(args.setmany[2])
        d = float(args.setmany[3])
        e = float(args.setmany[4])
        f = args.setmany[5] + '\0'
        p = TestappSetMany(a=a, b=b, c=c, d=d, e=e, f=f)

    elif args.setfixed:
        vector = {'vector' : args.setfixed}
        p = TestappFixedArrayMsg(vector=vector)

    elif args.setvariable:
        vector = {'vector' : args.setvariable}
        p = TestappVariableArrayMsg(vector=vector)

    elif args.state:
        channel = testapp_channel(c1=4294967295, c2=-32767, c3=255)
        info = '1234567\0'
        p = TestappState(channels=channel, info=info)

    else:
        parser.print_usage()
        sys.exit(1)

    m = msg()
    m.hwid = int('0d03', 16)
    m.seqnum = 0
    m.type = TESTAPP_TYPE
    m.data = p.to_binary()
    m.length = len(m.data)

    print ("Sending {0}-byte packet: {1}".format(m.length, str(p.to_json_dict())))
    req = B6Arq(SatFile('7', radio_type="DEBUG"), TranslatorB6('7'))
    req.send_once(m, 0)


if __name__ == "__main__":
  main()
