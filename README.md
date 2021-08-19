# CountDownTimer_Pytest
CountdownTimer on Pytest Frameowrk

About - A countdown timer can be defined as a virtual clock that counts down from a certain date or number to indicate the end or beginning of an offer or event. 
While such timers were typically used on landing pages, they’ve now found their way to checkout pages, as well.
The main purpose of a countdown timer is to create a sense of urgency and give the feeling that “time is running out.” 

Project Description- The countdown timer is a application that asks the user to enter how much time (in seconds) they want to set the timer for — once time is up,
print out “Countdwon completed!”.
Project is set up on Page Object model and the framework used is Pytest .
Page Object Model (POM) is a design pattern, popularly used in test automation that creates Object Repository for web UI elements. 
The advantage of the model is that it reduces code duplication and improves test maintenance.


Language used - Python
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Dependencies - 
Package            Version
------------------ ---------
packaging          21.0
pip                21.2.1
pytest             6.2.4
requests           2.26.0
selenium           3.141.0
setuptools         56.0.0
toml               0.10.2
urllib3            1.26.6
webdriver-manager  3.4.2

To install the packages -Run the below commands cmd
1) Install Python 3.9.6 from https://www.python.org/downloads/ and place it in the environment/system variables in the path variables
C:\Users\User>python --version
Python 3.9.6

2) Install Selenum - Open Terminal/Cmd and Write Command as written Below
python -m pip install selenium
selenium           3.141.0

3) Install Pytest by running the below cmd from the command mode
C:\Users\User>pip install pytest

All other packages are installed as part of project
*********************************************************************************************************************************

How to run the Project -
Open the project in any IDE
open the project terminal and run the below command in the terminal
C:\Users\User\PycharmProjects\CountDownTimer>pytest
It will give the output like this which means it had one test which succeeded
.                                                                                                                             [100%]

================================================================= 1 passed in 44.32s ==================================================================


Note :- Also It can be run without typing anything on terminal buy editing the configuration in your IDE and selecting pytest as default runner

*********************************************************************************************************************************
For Reporting use the below command while running in terminal
C:\Users\User\PycharmProjects\CountDownTimer>py.test --html=Reports\report.html


*********************************************************************************************************************************
Platform depedencies- Code can be run on IDEs which have python installed on it
********************************************************************************************************************************
Improvments - Reporting could be improved by integrting 3rd party tools in the project.

********************************************************************************************************************************
