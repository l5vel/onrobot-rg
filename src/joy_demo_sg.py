#!/usr/bin/env python3

import pygame
import sys
from onrobot_sg import SG
import time

def main():
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    gripper_obj = SG('192.168.0.27', 502)  # Replace with your IP and port
    default_step = 50 # step for moving the gripper
    try:
        step = default_step
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gripper_obj.close_connection()
                    sys.exit()

            # Joystick Y button to control width
            if joystick.get_button(3): 
                target_width = gripper_obj.get_gp_wd() + step  # Increase width
                gripper_obj.set_target(target_width)
            # Joystick A button to control width
            if joystick.get_button(0): 
                target_width = gripper_obj.get_gp_wd() - step  # Increase width
                gripper_obj.set_target(target_width)

            # Joystick LB to set gentle the gripper
            if joystick.get_button(4):  
                gripper_obj.set_gentle()
                step = 50

            # Joystick RB to reset gentle the gripper
            if joystick.get_button(5):  
                gripper_obj.set_gentle()
                step = step * 2

            time.sleep(0.1)
    except KeyboardInterrupt:
        gripper_obj.close_connection()
        sys.exit()

if __name__ == "__main__":
    main()