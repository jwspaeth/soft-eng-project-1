#!/usr/bin/env python3

if __name__ == "__main__":
    sample = main()
    print("Random sample: {}".format(sample))

import random

def main(lower_bound=1, upper_bound=1000000):
    """
    Description: randomly samples integer between lower bound and upper bound

    lower_bound: lower bound of random sampling, inclusive
    upper_bound: upper bound of random sampling, inclusive
    """
    
    sample = random.randint(lower_bound, upper_bound)
    
    return sample
