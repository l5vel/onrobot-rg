#!/usr/bin/env python3

import time
import argparse

from onrobot import RG
from onrobot_sg import SG


def run_demo():
    """Runs gripper open-close demonstration once."""
    if gripper == "sga":
        grip_obj = SG(toolchanger_ip, toolchanger_port)
        grip_obj.set_model_id(2)
        grip_obj.set_gentle(True)
        grip_obj.set_init()
        grip_obj.set_move()
    else:
        grip_obj = RG(gripper, toolchanger_ip, toolchanger_port)
    
    target = 115
    while grip_obj.get_gp_wd() != target:
        print(grip_obj.get_gp_wd())
        grip_obj.set_target(target)    
    print(f"Current width is: {grip_obj.get_gp_wd()}")

    grip_obj.close_connection()

def get_options():
    """Returns user-specific options."""
    parser = argparse.ArgumentParser(description='Set options.')
    parser.add_argument(
        '--gripper', dest='gripper', type=str,
        default="rg6", choices=['sga'],
        help='set gripper type, sga')
    parser.add_argument(
        '--ip', dest='ip', type=str, default="192.168.1.1",
        help='set ip address')
    parser.add_argument(
        '--port', dest='port', type=str, default="502",
        help='set port number')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_options()
    gripper = args.gripper
    toolchanger_ip = args.ip
    toolchanger_port = args.port
    run_demo()
