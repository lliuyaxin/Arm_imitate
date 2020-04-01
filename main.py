#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Author: Liuyaxin <17865196312@163.com>

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
'''
sys.path.append()将不在同一目录下模块的路径添加到程序中
os.path.join()将多个路径组合后返回
os.path.dirname(__file__)返回该脚本所在的完整路径
'''
from xarm.wrapper import XArmAPI
from BodyGameRuntime import BodyGameRuntime
from ArmControl import ArmControl
from SerialCommunication import SerialCommunication

if __name__ == '__main__':

    arm_left = XArmAPI('192.168.1.209')
    arm_right = XArmAPI('192.168.1.151')    # 连接控制器

    arm_left.motion_enable(enable=True)
    arm_right.motion_enable(enable=True)    # 使能

    arm_left.set_mode(0)
    arm_right.set_mode(0)                   # 运动模式：位置控制模式

    arm_left.set_state(state=0)
    arm_right.set_state(state=0)            # 运动状态：进入运动状态


    s=SerialCommunication()
    game = BodyGameRuntime()
    arm=ArmControl(arm_left,arm_right)

    while True:
        a=s.ser()
        if a=='88':
            arm.initial()
            game.run(arm)
            arm.initial()


