from typing import Optional

def rectilinear_motion(
        initial_position: Optional[float] = None, 
        final_position: Optional[float] = None, 
        velocity: Optional[float] = None, 
        time: Optional[float] = None
    ) -> float:
    """
    This function applies the basic rectilinear motion formula:
        x = x0 + vt
    where x is the final position, x0 is the initial position, v is the velocity, and t is the time.

    Solve for any parameter (initial position, final position, velocity, time) in the rectilinear motion equation.

    Provide any three of the four parameters to solve for the fourth.
    The function returns the value of the parameter set to None.

    Args:
    initial_position (float, optional): The initial position of the object (in meters).
    final_position (float, optional): The final position of the object (in meters).
    velocity (float, optional): The velocity of the object (in meters per second).
    time (float, optional): The time duration of the motion (in seconds).

    Returns:
    float: The computed value of the missing parameter.

    Examples:
    >>> solve_rectilinear_motion(initial_position=0, final_position=50, time=5)
    10.0  # velocity

    >>> solve_rectilinear_motion(final_position=40, velocity=-20, time=3)
    100.0  # initial_position

    >>> solve_rectilinear_motion(initial_position=0, final_position=100, velocity=5)
    20.0  # time
    """
    if initial_position is None:
        return final_position - velocity * time
    elif final_position is None:
        return initial_position + velocity * time
    elif velocity is None:
        return (final_position - initial_position) / time
    elif time is None:
        return (final_position - initial_position) / velocity
    else:
        raise ValueError("One parameter must be None to solve for it.")
