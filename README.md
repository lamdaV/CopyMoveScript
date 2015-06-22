# CopyMoveScript
Automated Grading Script. This is a similar to AutomatedPythonTest. It allows instructors to hide the UnitTest case from the students. Unfortunately, doing so will remove the possibility of immediate feedback. Therefore, a combination of the two may be preferrable as students may have a seperate UnitTest and the instructor may have a primary UnitTest for grading purposes. This allows for both immediate feedback and the ability to hide certain test cases.

# Bugs:


# How To Use
- Download the repository.  
- Move the testSetup folders to a desired location.
- Edit the read.txt file accordingly:
  - The first line is reserved for the Path to the UnitTest. For testing, set the path to where HelloWorldTest.py is. It is   located in the TestScripts folder.
  - The second line is reserved for the Path to the root folder containing the students completed solutions. For testing, set the path to TestCopyScript.
  - The third line is the name of the UnitTest file. For testing, leave this as is.  
- Navigate to where CopyMove.py is in the command line.  
- Run the following command: 
``` 
$ python CopyMove.py
```
- The test results should be as follows:
  - Fail
  - Pass
  - Pass
