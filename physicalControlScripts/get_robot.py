#!/usr/bin/env python

import urx
from IPython import embed
import logging

if __name__ == "__main__":
    robot = urx.Robot("10.74.48.173")
    try:
        logging.basicConfig(level=logging.INFO)
        #robot = urx.Robot("192.168.1.6")
        #robot = urx.Robot("localhost")
        r = robot
        print("Robot object is available as robot or r")
        embed()
    finally:
        robot.close()
