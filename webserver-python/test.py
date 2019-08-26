#!/usr/bin/env python3

import sys

from random_generator import generator_wrapper

def test(n_test_samples=1000, n_target_length=750, lower_bound=1, upper_bound=1000000):
    '''
    Method
        test: tests randomness of a generator
        
    Args
        n_test_samples: number of samples to pull from generator
        n_target_length: number of unique samples which qualify a success. Equal or greater than this value returns True, less returns False
    
    Return
        test_result: boolean. Determines if test was passed (True) or failed (False)
        n_unique_samples: number of unique samples obtained at the end of test. Used for debugging purposes
    '''
    
    unique_samples = []

    generator = generator_wrapper(lower_bound, upper_bound)

    for i in range(n_test_samples):
        
        sample = next(generator)
        
        if sample not in unique_samples:
            unique_samples.append(sample)

    if len(unique_samples) >= n_target_length:
        return True, len(unique_samples)
    else:
        return False, len(unique_samples)
    
if __name__ == "__main__":
    test_result, n_unique_samples = test()

    lower_bound = 1
    upper_bound = 1000000
    for arg in sys.argv:
        if "-lower_bound=" in arg:
            lower_bound = int(arg.replace("-lower_bound=", ""))
        
        if "-upper_bound=" in arg:
            upper_bound = int(arg.replace("-upper_bound=", ""))

    test_result, n_unique_samples = test(lower_bound=lower_bound, upper_bound=upper_bound)
    
    print_string = "\nTest result: {}\nNumber of unique samples: {}\n".format(test_result, n_unique_samples)
    print(print_string)
