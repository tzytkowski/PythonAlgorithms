def main():
    #Declare local variables
    studentName      = ""
    studentAvg       = 0.0
    sumOfStudentAvgs = 0.0
    classAvg         = 0.0
    numStudents      = 0
    anotherStudent   = "yes"
    numTests = getNumTests()
    
    while anotherStudent == "yes":
        #Ask user for the name of a student
        studentName      = input("Enter the name of a student ==>  ")
        studentAvg       = getStudentAverage(studentName, numTests)
        #Add the student's average to the total average
        sumOfStudentAvgs = sumOfStudentAvgs + studentAvg
        #Increment the number of students
        numStudents      = numStudents + 1
        anotherStudent   = getAnotherStudent()
    #Calculate and display the class average
    classAvg = sumOfStudentAvgs / numStudents
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("The class average is: {0:.2f}%".format(classAvg))
def getNumTests():
    #Declare local variables
    strNumTests = ""
    numTests    = 0
    
    #Get the number of tests per student
    strNumTests = input("How many test scores do you have for each student? ==>  ")
    #Validate that the number of tests is a positive integer (w/o a sign)
    while True:
        if strNumTests.isdigit():
            numTests = int(strNumTests)
            print()
            return numTests
        else:
            print("Sorry, you did not enter a positive integer")
            strNumTests = input("Please try again (digits only) ==>  ")
def getStudentAverage(studentName, numTests):
    #Declare local variables
    strTestScore = ""
    testScore    = 0.0
    testSum      = 0.0
    studentAvg   = 0.0
    counter      = 0
    #Get the test scores for each student
    for counter in range (numTests):
        strTestScore = input("Enter a test score ==>  ")
        #Validate that the test score is a positive number
        while True:
            try:
                testScore = float(strTestScore)
                if testScore > 0:
                    break
                else:
                    print("Sorry, you did not enter a positive number")
                    strTestScore = input("Please try again ==>  ")
            except ValueError:
                    print("Sorry, you did not enter a number")
                    strTestScore = input("Please try again ==>  ")
        #Add each test score to the accumulator
        testSum = testSum + testScore
    #Calculate the student's average
    studentAvg = testSum / numTests
    #Output the student's name and average
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Student Name: {0:15s} Average: {1:.2f}%".format(studentName, 
studentAvg))
    return studentAvg
def getAnotherStudent():
    #Declare local variables
    response = ""
    #Ask the user if they have another student
    print()
    response = input("Do you wish to enter another student's grades? ==>  ")
    response = response.lower()
    #Validate that the response was "yes" or "no"
    while True:
        if response == "yes" or response == "no":
            return response
        else:
            print('Sorry, you did not enter "yes" or "no"')
            response = input("Please try again ==>  ")
            response = response.lower()
main()
    
        