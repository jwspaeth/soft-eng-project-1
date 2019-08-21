# soft-eng-project-1
Sample Problem: Random number generator that sits on a web server

File Descriptions
    random_generator.py: contains the generator method, which generates a random integer given arguments. If run directly, it prints a random sample. By calling generator within another program, it returns the actual sample
    test.py: contains the test method. If run directly, prints whether the test was passed (True, False), and the number of unique samples generated in the test. By calling test within another program, it returns the test boolean and number of unique samples
    
Two methods to run (need Python 3 installed):
    (1) Run directly with python interpreter
        (1.1) Enter "python filename" on the command line
            (1.1.1) If this fails, try "python3 filename"
    (2) Run like a bash script
        (1.1) Enter "chmod u+x filename"
        (1.2) Enter "./filename"