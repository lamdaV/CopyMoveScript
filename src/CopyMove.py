"""
This is a proof of concept. This is an automated grading script. Given that the user has a folder of student repositories,
the user must first fill out the read.txt file. 
 - The first line is the the path to the UnitTest.
 - The second line is the path to the root directory of where the students repositories are.
 - The third line is the name of the UnitTest.
 By running the script, the UnitTest case will by copied from the specified location to each student's repository. Then
 the script will run each UnitTest case one-by-one, allowing the user to read results of the UnitTest at their own pace.
 Once completed, the files will be removed from each student's repository as well as any additional folders/files generated
 by the UnitTest.

Created on May 22, 2015.
Written by: lamd.
"""
import os
import shutil
import subprocess
import time

def main():
    """ 
        Runs the script.
    """
    # Constants.
    SOURCE_LOCATION = 0
    ROOT_DIRECTORY_LOCATION = 0
    DIRECTORY_LOCATION = 1
    UNIT_TEST_LOCATION = 2

    # Global Variables Passed to Other Functions.
    global source
    global unitTestName
    global directoryOfFiles
    global rootDirectory

    # Open the read.txt file and split it into a list. Close it after.
    file = open("read.txt")
    listOfData = file.read().split("\n")
    file.close()

    # Assign global values.
    source = listOfData[SOURCE_LOCATION]
    directoryOfFiles = listOfData[DIRECTORY_LOCATION]
    unitTestName = listOfData[UNIT_TEST_LOCATION]

    # Generate destinations list from directory. Assign rootDirectory value.
    destinations = generateDestinationList()
    rootDirectory = destinations[ROOT_DIRECTORY_LOCATION]

    # Copy UnitTest to destinations.
    copyTestToDestination(destinations)

    # Execute UnitTest and display information.
    executeUnitTest(destinations)

    # Remove UnitTest and residue files.
    removeUnitTest(destinations)

    print("Completed")

def removeUnitTest(destinations):
    """
        Remove the UnitTest from the directories and any generated files/directories.
        
        Preconditions:
            :type destinations :list
    """
    for k in range(1, len(destinations)):
        fileName = destinations[k] + "/" + unitTestName
        os.remove(fileName)
        fileName = destinations[k] + "/__pycache__"
        shutil.rmtree(fileName)
        time.sleep(1)

def executeUnitTest(destinations):
    """
        Executes the copied UnitTest with input pause.
        
        Preconditions:
            :type destinations :list
    """

    for k in range(1, len(destinations)):
        # Prints name of file (hopefully the student's name).
        print()
        print(destinations[k].replace(rootDirectory + "/", ""))
        fileName = destinations[k] + "/" + unitTestName
        subprocess.call(fileName, shell=True)
        input("Press Enter key to continue...")
        time.sleep(1)

def copyTestToDestination(destinations):
    """
        Copies the UnitTest case to the file location.
        
        Preconditions:
            :type destinations :list
    """
    for k in range(1, len(destinations)):
        copyTest(destinations[k])

def generateDestinationList():
    """
        Generates a list of files at the specified Destination.
        
        Preconditions:
            :type location :str
    """
    destinations = []
    for root, _, _ in os.walk(directoryOfFiles):
        destinations.append((str(root).replace("\\", "/")))
    return destinations

def copyTest(destination):
    """
        Copies the UnitTest file to the given destination.
        
        Precondtions:
            :type destination :str
    """
    shutil.copy(source, destination)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
