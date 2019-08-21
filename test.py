#!/usr/bin/env python3

if __name__ == "__main__":
    test_result = main()
    print("Test result: {}".format(test_result))

import random_generator.main as random_generator

def main(n_test_samples=1000, n_target_length=750):
    
    unique_samples = []

    for i in range(n_test_samples):
        
        sample = random_generator()
        
        if sample not in unique_samples:
            unique_samples.append(sample)

    if length(unique_samples) >= n_target_length:
        return True
    else:
        return False
    
    
