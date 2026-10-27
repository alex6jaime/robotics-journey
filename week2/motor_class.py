class Motor:
    def __init__(self, name, max_rpm):
        """Initialize the motor's name, maximum RPM, and speed."""
        self.name = name
        self.max_rpm = max_rpm
        self.speed_percent = 0

    def set_speed(self, percent):
        """Set the speed percentage, clamped between -100 and 100."""
        self.speed_percent = max(-100, min(100, percent))


class EncoderMotor(Motor):
    def __init__(self, name, max_rpm, counts_per_rev):
        """Initialize the motor and its encoder counts per revolution."""
        super().__init__(name, max_rpm)
        self.counts_per_rev = counts_per_rev

    def counts_to_degrees(self, counts):
        """Convert encoder counts into degrees of rotation."""
        return (counts / self.counts_per_rev) * 360

motor1 = EncoderMotor("test", 150, 1320)

angle = motor1.counts_to_degrees(330)
print(angle)  # 90.0

#----------------

wheel = EncoderMotor("left wheel", 150, 1320)

# Store the desired motor command.
wheel.set_speed(40)

# Suppose the encoder has measured 330 counts.
measured_counts = 330

# Convert the measurement into wheel rotation.
angle = wheel.counts_to_degrees(measured_counts)

print(wheel.speed_percent)  # 40
print(angle)                # 90.0