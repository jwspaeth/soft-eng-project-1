#!/usr/bin/env python3

import random

def generator(lower_bound=1, upper_bound=1000000):
    """
    Method
        generator: randomly samples integer between lower bound and upper bound

    Args
        lower_bound: lower bound of random sampling, inclusive
        upper_bound: upper bound of random sampling, inclusive
        
    Return
        sample: random sample inclusively between lower and upper bound
    """
    
    sample = random.randint(lower_bound, upper_bound)
    
    return sample

if __name__ == "__main__":
    sample = generator()
    print("\nRandom sample: {}\n".format(sample))