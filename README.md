# soft-eng-project-1

Link to Github Page: https://jwspaeth.github.io/soft-eng-project-1/

Sample Problem: Random number generator that sits on a web server

File Descriptions
    random_generator.py: contains the generator method, which generates a random integer given arguments. If run directly, it prints a random sample. By calling generator within another program, it returns the actual sample
    test.py: contains the test method. If run directly, prints whether the test was passed (True, False), and the number of unique samples generated in the test. By calling test within another program, it returns the test boolean and number of unique samples
    
Two methods to run (need Python 3 installed):
    (1) Run directly with python interpreter
        (1.1) Enter "python filename" on the command line
            (1.1.1) If this fails, try "python3 filename"
    (2) Run like a bash script
        (2.1) Enter "chmod u+x filename"
        (2.2) Enter "./filename"


# Instructions for Installation and Use
## Prerequisites for Installation
    You will need access to the Google Cloud Platform, and a git login and password.
## Create Google Compute Engine Instance and Pull Repository
    You will need a Google Cloud instance or shell to run this application. In order to set up an instance, follow the next few steps. 
    1. Go to the Google Cloud Platform page. 
        > https://console.cloud.google.com
    2. Click on the 'Activate Cloud Shell' icon. This will pull up a Google Cloud shell for you to interact with.
        ![Google Cloud Screenshot](C:\Users\Darby\Documents\Fall 2019\Software Engineering I\Google_Cloud_Settings)
    3. In the Cloud Shell, we need to access the git repository with all of the code. Copy and paste the line in your Cloud Shell and press Enter:
        > git clone https://github.com/jwspaeth/soft-eng-project-1.git
    4. Go into the repository using the command
        > cd soft-eng-project-1
## Install Flask
    We will need to install Flask. Use the command 
        > sudo pip3 install Flask
     on the command line in your shell. 
## Install TomCat
## Run it (Separate for Python and Java)
    To run the Python server, type the following commands into the command line: 
        > cd docs
        > ./python-webpage.py
    This will generate a URL for the webpage in the format 'http://x.x.x.x:5000'.
    Click this URL to access the webpage.
    To end this session, type CTRL+C into the command line.
    Enjoy!