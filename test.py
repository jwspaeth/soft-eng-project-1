#!/usr/bin/env python3

from random_generator import generator

def test(n_test_samples=1000, n_target_length=750):
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

    for i in range(n_test_samples):
        
        sample = generator()
        
        if sample not in unique_samples:
            unique_samples.append(sample)

    if len(unique_samples) >= n_target_length:
        return True, len(unique_samples)
    else:
        return False, len(unique_samples)
    
if __name__ == "__main__":
    test_result, n_unique_samples = test()
    
    print_string = "\nTest result: {}\nNumber of unique samples: {}\n".format(test_result, n_unique_samples)
    print(print_string)
