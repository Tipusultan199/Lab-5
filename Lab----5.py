import numpy as np  # Make sure to import numpy
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS

def main():

    # Define the joint angles in radians considering the joint limits
    joint_positions = [np.radians(90), np.radians(-45), np.radians(0), np.radia>

    # Initialize the robot
    bot = InterbotixManipulatorXS(
        robot_model='px100',
        group_name='arm',
        gripper_name='gripper'
    )

    # Move the robot to home position
    bot.arm.go_to_home_pose()

    # Set the joint positions
    bot.arm.set_joint_positions(joint_positions)

    # Move the robot back to home pose
    bot.arm.go_to_home_pose()

    # Move the robot to sleep pose
    bot.arm.go_to_sleep_pose()

    # Shutdown the robot
    bot.shutdown()

if __name__ == '__main__':
    main()

