#!/usr/bin/env python
# encoding: utf-8

from dronekit import connect
vehicle = connect("/dev/ttyACM0", wait_ready=['system_status', 'mode'], baud=57600)

print "Autopilot Firmware version: %s" % vehicle.version
print "Global Location: %s" % vehicle.location.global_frame
print "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
print "Local Location: %s" % vehicle.location.local_frame    #NED
print "Attitude: %s" % vehicle.attitude
print "Velocity: %s" % vehicle.velocity
print "Groundspeed: %s" % vehicle.groundspeed
print "Airspeed: %s" % vehicle.airspeed
print "Gimbal status: %s" % vehicle.gimbal
print "Battery: %s" % vehicle.battery
print "EKF OK?: %s" % vehicle.ekf_ok
print "Last Heartbeat: %s" % vehicle.last_heartbeat
print "Rangefinder: %s" % vehicle.rangefinder
print "Rangefinder distance: %s" % vehicle.rangefinder.distance
print "Rangefinder voltage: %s" % vehicle.rangefinder.voltage
print "Heading: %s" % vehicle.heading
print "System status: %s" % vehicle.system_status.state
print "Mode: %s" % vehicle.mode.name    # settable
print ("vehicle.is_armable:%s" %vehicle.is_armable)
print ("vehicle.armed: %s" %vehicle.armed)
print ("home position:%s" %vehicle.home_location)
