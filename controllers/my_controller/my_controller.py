from controller import Robot

# Initialize the robot
robot = Robot()

# Get the time step of the current world (usually 32ms for e-puck)
timestep = int(robot.getBasicTimeStep())

# ===== GET DEVICES (MOTORS & SENSORS) =====
# Get the motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Set the motors to velocity control mode
# (setting position to 'infinity' means continuous rotation)
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set initial velocity to 0
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Get distance sensors (for obstacle avoidance)
# e-puck has 8 distance sensors: ps0 to ps7
ps0 = robot.getDevice('ps0')
ps1 = robot.getDevice('ps1')
ps2 = robot.getDevice('ps2')
ps3 = robot.getDevice('ps3')
ps4 = robot.getDevice('ps4')
ps5 = robot.getDevice('ps5')
ps6 = robot.getDevice('ps6')
ps7 = robot.getDevice('ps7')

# Enable all distance sensors
ps0.enable(timestep)
ps1.enable(timestep)
ps2.enable(timestep)
ps3.enable(timestep)
ps4.enable(timestep)
ps5.enable(timestep)
ps6.enable(timestep)
ps7.enable(timestep)

# Get camera (optional)
camera = robot.getDevice('camera')
camera.enable(timestep)

# ===== MAIN CONTROL LOOP =====
# This runs repeatedly while the simulation is running
while robot.step(timestep) != -1:
    
    # ----- READ SENSORS -----
    # Read distance sensor values
    ps0_value = ps0.getValue()
    ps1_value = ps1.getValue()
    ps2_value = ps2.getValue()
    ps3_value = ps3.getValue()
    ps4_value = ps4.getValue()
    ps5_value = ps5.getValue()
    ps6_value = ps6.getValue()
    ps7_value = ps7.getValue()
    
    # Print sensor values to console (for debugging)
    print(f"Front sensors: left={ps7_value:.2f}, right={ps0_value:.2f}")
    
    # ----- DECIDE WHAT TO DO -----
    # This is where your robot logic goes
    
    # Simple behavior: move forward
    left_speed = 10.0
    right_speed = 10.0
    
    # ----- SEND COMMANDS TO MOTORS -----
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)