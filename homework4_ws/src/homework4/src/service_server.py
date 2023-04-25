#!/usr/bin/env python3

import rospy
from homework4.srv import OddEvenCheck, OddEvenCheckResponse

def determine_odd_even(req):
    remainder = req.number % 2
    res = OddEvenCheckResponse()
    if remainder == 0:
        res.answer = "Even"
    elif remainder == 1:
        res.answer = "Odd"
    else:
        return False
    return res
if __name__ == "__main__":
    rospy.init_node("odd_even_service_server_node")

    service = rospy.Service("odd_even_check", OddEvenCheck, determine_odd_even)

    rospy.loginfo("Odd Even Check Server Running...")

    rospy.spin()
