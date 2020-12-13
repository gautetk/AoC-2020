import math
from math import gcd


def main(source):
    with open(source) as r:
        lines = r.readlines()

    timeStamp = int(lines[0].rstrip('\n'))
    busses = lines[1].split(',')

    result1 = part1(timeStamp, busses)
    print(result1)

    result2 = part2(busses)
    print(result2)


def part1(timeStamp, busses):
    waitMin = [(int(x), int(x)-timeStamp%int(x)) for x in busses if x.isdigit()]
    minBuss = min(waitMin, key = lambda x: x[1])
    return minBuss[0]*minBuss[1]


def part2(busses):
    bussTimes = [(i, int(x)) for i, x in enumerate(busses) if x.isdigit()]
    y, x =bussTimes[0]
    for b in bussTimes[1:]:
        x, y =combine_phased_rotations(x, y, b[1], -b[0])
    return y
        


def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def arrow_alignment(red_len, green_len, advantage):
    """Where the arrows first align, where green starts shifted by advantage"""
    period, phase = combine_phased_rotations(
        red_len, 0, green_len, -advantage % green_len
    )
    return -phase % period
    
def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

if __name__ == '__main__':
    challenge = '13'
    source = fr'resources\day{challenge}.txt'
    main(source)
