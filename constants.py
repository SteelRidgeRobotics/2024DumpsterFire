from phoenix6.configs import Slot0Configs
from phoenix6.configs.talon_fx_configs import *
from robotpy_apriltag import AprilTagField, AprilTagFieldLayout
from wpilib import RobotBase

class Constants:

    class CanIDs:

        k_left_front_drive = 1
        k_left_rear_drive = 2
        k_right_front_drive = 3
        k_right_rear_drive = 4
            
        k_left_front_direction = 5
        k_left_rear_direction = 6
        k_right_front_direction = 7
        k_right_rear_direction = 8
            
        k_left_front_encoder = 5
        k_left_rear_encoder = 6
        k_right_front_encoder = 7
        k_right_rear_encoder = 8

        k_pigeon = 9
        
        k_pivot_motor = 9
        k_intake_motor = 10
        
        k_lift_right = 11
        k_lift_left = 12

    class IntakeConstants:

        k_gear_ratio = 5
        k_intake_speed = 1

    class PivotConstants:

        k_gains = Slot0Configs() \
        .with_k_p(10).with_k_i(0).with_k_d(0.2) \
        .with_k_s(0.2).with_k_v(0.12).with_k_a(0)

        k_acceleration = 4
        k_cruise_velocity = 0.5
        k_jerk = 20

        k_stow_pos = 0
        k_intake_pos = 0.361
        k_score_down_pos = 0.268
        k_score_up_pos = 0.107 #For scoring up into the amp (yell at Kaylee not me ;-;) 

        k_gear_ratio = 50
        k_supply_current = 5

    class LiftConstants:

        k_gains = Slot0Configs() \
        .with_k_p(1).with_k_i(0.1).with_k_d(0) \
        .with_k_s(0).with_k_v(0).with_k_a(0)

        k_acceleration = 75
        k_cruise_velocity = 100

        k_supply_current = 25

        k_top_pos = 78.635 # lol big number
        k_score_pos = 22.254
        k_bottom_pos = 0

        k_gear_ratio = 12

    class LedConstants:

        k_led_pwm_port = 9 
        k_led_length = 114

    k_apriltag_layout = AprilTagFieldLayout.loadField(AprilTagField.k2024Crescendo)
    
    class Swivel:
        MM_ACCELERATION = 0
        MM_CRUISE_VEL = 0
        TRANSFERPOS = 0
        K_P = 0
        K_I = 0
        K_D = 0
        K_V = 0
        K_S = 0
        GEAR_RATIO = 1
        SUPPLY_LIMIT = 0
        MAX_ANGLE = 80.0

    class LimeLight:
        
        k_enable_vision_odometry = RobotBase.isReal() # False if there's no Limelight on the robot.
        
        k_limelight_name = "limelight" # "limelight" by default. Name of the limelight to use for vision.

        k_use_mega_tag_2 = False # If False, uses MegaTag 1.
        
        k_standard_deviations = [0.3, 0.3, 999999] # (x, y, radians) Basically how confident we are with our vision, lower = more confident. Angle is set really high because we have a gyro.

        k_auto_align_kp = 0.04

        k_mount_angle = 0.0  # degrees for the angle that the limelight is mounted from the floor
        k_mount_height = 23.25 # distance from the center of the limelight lens to the floor in inches
        k_target_height = 82.5 # height of the speaker in inches
        k_tag_height = 51.9 # height of april tag in inches

        REDSPEAKERID = 4
        BLUESPEAKERID = 7