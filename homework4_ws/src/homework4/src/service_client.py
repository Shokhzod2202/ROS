#!/usr/bin/env python3

import rospy
from homework4.srv import OddEvenCheck

rospy.init_node("odd_even_service_client_node")

client = rospy.ServiceProxy("odd_even_check", OddEvenCheck)

print("Type '0' to quit")

while not rospy.is_shutdown():
    input_num = int(input("Enter an integer: "))

    odd_even_check_srv = OddEvenCheck()
    odd_even_check_srv.number = input_num

    if input_num == 0:
        rospy.loginfo("Exiting Application...")
        break

    try:
        resp = client(odd_even_check_srv)

        print("The number is {}".format(resp.answer))

    except rospy.ServiceException as e:
        rospy.logerr("Service Call Failed: {}".format(e))
        break
