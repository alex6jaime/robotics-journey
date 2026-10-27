from motor_class import EncoderMotor

def test_zero_counts():
    """Test that 0 counts converts to 0 degrees."""
    motor = EncoderMotor("test", 150, 1320)
    assert motor.counts_to_degrees(0) == 0