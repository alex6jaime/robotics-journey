def calculate_motor_power(torque, angular_velocity):
    power = torque * angular_velocity
    return power


torque = 2.5
angular_velocity = 10

result = calculate_motor_power(torque, angular_velocity)

print("Power:", result, "W")