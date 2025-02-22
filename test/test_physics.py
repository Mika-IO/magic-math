from magic_math.physics import rectilinear_motion

def test_rectilinear_motion_final_position():
    assert rectilinear_motion(initial_position=0, velocity=10, time=5) == 50

def test_rectilinear_motion_initial_position():
    assert rectilinear_motion(final_position=50, velocity=10, time=5) == 0

def test_rectilinear_motion_velocity():
    assert rectilinear_motion(initial_position=100, final_position=40, time=3) == -20

def test_rectilinear_motion_time():
    assert rectilinear_motion(initial_position=0, final_position=100, velocity=5) == 20
