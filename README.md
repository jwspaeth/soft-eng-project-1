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
## Run it in Python
    To run the Python server, type the following commands into the command line: 
        > cd docs
        > ./python-webpage.py
    This will generate a URL for the webpage in the format 'http://x.x.x.x:5000'.
    Click this URL to access the webpage.
    To end this session, type CTRL+C into the command line.
    Enjoy!

## Install and Deploy TomCat9
### 1) Add apache-tomcat9 zip file to your directory:
We will need to install the zip file onto your machine. Go to this website https://tomcat.apache.org/download-90.cgi and download 
the zip file in Binary Distributions --> Core --> zip. Keep the file in its zipped form and upload it onto your server. Make sure
to move the file into the directory that you would like.

### 2) Install unzip and unzip the folder:
After moving the file to your specified directory. We need to install unzip:

    > sudo apt-get update
    > sudo apt-get install unzip
    
Now that we have unzip, we unzip the folder with the following commands

    > unzip <PATH TO FOLDER>/apache-tomcat-9.0.{xx}
    
{xx} is just a representation of your version, so type in the correct version you have. Rename the apache-tomcat9-{x} folder 
to "tomcat" for use of use
        
    > mv apache-tomcat-9.0.{xx} tomcat
    
### 3) Install Java:
Next we will need to install java. To check if you already have java, type in:
       
    > java -version

If the response to this command is "The program 'java' can be found in the folloing packages" then you do not have java installed.
To install, run this command:

    > sudo apt-get install default-jre
    
This will install the default version of java.

### 4) Setup the configuration files:
Now we will need to change some of the properties of certain configuration files. First cd into tomcat's conf folder

    > cd <TOMCAT PATH>/tomcat/conf
        
We will need to change small parts of server.xml, web.xml, and context.xml:

#### 4.1) Change default port in server.xml:
Within server.xml, we need to change the default port number. This number is configured to 8080, but you can choose any number
from 1024 and 65535. Make sure to have the port that you would like open on the server as well. If the port is not open on the 
server's side, then the page we want to load will not load.
    
Locate the following within server.xml:
    
    <!-- A "Connector" represents an endpoint by which requests are received
    and responses are returned. Documentation at :
    Java HTTP Connector: /docs/config/http.html
    Java AJP  Connector: /docs/config/ajp.html
    APR (HTTP/AJP) Connector: /docs/apr.html
    Define a non-SSL HTTP/1.1 Connector on port 8080
    -->
    <Connector port="8080" protocol="HTTP/1.1"
        connectionTimeout="20000"
        redirectPort="8443" />
     
Change the port within Connector to whatever port you would like. Make sure to save the file after editing

#### 4.2) Enable listings in web.xml:
Now we will change a small portion of the web.xml file:
This change will enable directory listing so that we can navigate into our files through the webpage. We will need to 
change listings from "false" to "true"
     
     Locate the following within web.xml:
     <servlet>
        <servlet-name>default</servlet-name>
        <servlet-class>org.apache.catalina.servlets.DefaultServlet</servlet-class>
        <init-param>
            <param-name>debug</param-name>
            <param-value>0</param-value>
        </init-param>
        <init-param>
            <param-name>listings</param-name>
            <param-value>false</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
      </servlet>

Locate "fasle" under "listings" and change it to "true"

#### 4.3) Add reloadable attribute in context.xml:
Finally, we will look at context.xml:

We will need to add the reloadable attribute and set it to "true." This will allow us to reload the webpage after the code changes.

Locate <Context> start element, and add the reloadable attribute set to "true"
    
    <Context reloadable="true">
        ......
        ......
    </Context>

### 5) Start Tomcat Server
To start the server, go into the bin folder from the tomcat folder. Issue this command once in that directory:

    > cd tomcat/bin
    
To run the startup script, execute this command:

    > ./startup.sh

This will start up the server. Please check the logs to make sure that the server was started correctly. If there are any problems go to the debug section (5.4).

#### 5.1) Access server through port number

Go to your local browser as an HTTP client. Issue the URL

    http://<IP ADDRESS OF SERVER>:<PORT NUMBER SPECIFIED IN SERVER.XML>
    
If you see the Apache Tomcat logo and website, then you're all good. If not, go to the debug section.

#### 5.2) Shutdown the server
To shutdown the server, we need to go back into the bin folder within tomcat. Once in the bin, issue this command:

    > ./shutdown.sh
    
#### 5.4) Debug

1. The first problem that might occur is that tomcat won't show up on the URL. This is most likely because the server hasnt started yet. You need to give at least 10 minutes for tomcat to start before anything will actually show up on the webpage.

2. If the server has started, and waited at least 10 minutes, and still nothing shows up. Check the logs. Go to tomcat's home folder and issue this:
    
        > cd log
        > cat <MOST RECENT LOG>

Errors should appear specifying what they are. Here is a common error:

        > SEVERE [main] org.apache.catalina.util.LifecycleBase.handleSubClassException Failed to initialize component [Connector[HTTP/1.1-9999]]
        > .....
        > Caused by: java.net.BindException: Address already in use

If this error occurs, then you have more than one instance of tomcat running. All instances need to be killed before you can startup another tomcat instance. Issue this to find out what ports are being used:

        > ps -aux | grep java

This command will show all of the java processes running and their process ids. You need to kill every process by issues this command:

        > kill -9 <PROCESS ID>
        
After killing all processes, go back into the bin folder and run a startup and wait at least 10 minutes before accessing the URL. Please check the logs again once you do a second startup. 

### 6) Develop and Deploy the WebApp

To deploy the random number app, we need to first set up a file structure. While in the tomcat home folder cd into the webapps folder

Under webapps, create a file structure as represented below:

      >tomcat
        >bin
        >conf
        >webapps
          ><NAME OF WEBAPP>
             >WEB_INF
                >classes
                
Under the classes folder, create your Java Servlet. This is where you java code goes. 

Within the java file we need a specific line.

    > @WebServlet("/<NAME>")
    
This line will tell us what how to access the servlet from the URL. You will NEED to specify a name within this piece of code.

#### 6.1) Compile Java Servlet and Run

Once the Java file is in the classes folder, we need to compile the file so that the servlet can render it properly. To compile the java file, we need the servlet-api.jar file that tomcat provides. Issue this command to compile your java code:

    >javac -cp .:<PATH TO TOMCAT FOLDER>/tomcat/lib/servlet-api.jar <NAME OF JAVA FILE TO COMPILE>

The outpult will be a class file. 

### 7) Accessing the Deployed WebApp

Run a startup to fire up tomcat. After waiting at least 10 minutes. Access the server by issues the URL as you did previously. This time we need to route to the servlet:

        >http://localhost:<PORT>/<NAME OF WEBAPP>/<WEB SERVLET NAME>
