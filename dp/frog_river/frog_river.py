"""
river = "*****  *   * * *  *  *" => crossable
         011 2  3   4   4  3   4
         011 2  3   4   4  3  3   4
         01111  3   4   4  3  3   4

river = "*****      " => not crossable
         011 2  3

Initial speed: 0
Initial location: 0

Speed = {speed - 1, speed, speed + 1}
Loc = loc + speed
"""


SPEED_OFFSETS = [-1, 0, 1]


def is_crossable(river, pos, speed):
    """
    print is_crossable("** *", 0, 0), "should be True"
    print is_crossable("*****          *", 0, 0), "should be False"

    :param river:
    :param pos:
    :param speed:
    :return:
    """
    if river[pos] == " ":
        return False

    for offset in SPEED_OFFSETS:
        if speed + offset <= 0:
            continue

        ns = speed + offset
        np = pos + ns
        if np >= len(river):
            return True
        if river[np] == " ":
            continue
        if is_crossable(river, np, ns):
            return True

    return False


def is_crossable_optimized(river):
    # Cached attempts elements are two-tuples of position and speed that
    # have been attempted
    cached_attempts = set()

    return _is_crossable_helper(river, cached_attempts, 0, 0)


def _is_crossable_helper(river, cached_attempts, pos, speed):
    if (pos, speed) in cached_attempts:
        return False # been there, done that

    cached_attempts.add((pos, speed))

    if pos >= len(river):
        return True # crossed - yay!
    if river[pos] == " ":
        return False # drowned :(

    for offset in SPEED_OFFSETS:
        new_speed = speed + offset
        if new_speed <= 0: # may only go forward
            continue

        if _is_crossable_helper(river, cached_attempts, pos + new_speed, new_speed):
            return True

    return False
