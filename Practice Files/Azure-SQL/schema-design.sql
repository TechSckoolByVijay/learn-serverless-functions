-- Script 1

DROP TABLE IF EXISTS OnlineCourses;

CREATE TABLE OnlineCourses (
  CourseID INT NOT NULL,
  Title VARCHAR(200) NOT NULL,
  Topic VARCHAR(50) NOT NULL,
  Instructor VARCHAR(100) NOT NULL,
  Level VARCHAR(100) NOT NULL,
  PRIMARY KEY (CourseID)
);

INSERT INTO OnlineCourses (CourseID, Title, Topic, Instructor, Level ) 
VALUES
(1, 'Automating Administration With Windows PowerShell', 'PowerShell', 'Vijay', 'Intermediate' ),
(2, 'Microsoft Azure Storage - The Complete Guide', 'Azure', 'Vijay', 'Intermediate' ),
(3, 'Windows PowerShell Hands On Training for Beginners', 'PowerShell', 'Vijay', 'All' ),
(4, 'Learning Azure Process Automation using PowerShell', 'Azure', 'Vijay', 'All' ),
(5, 'Learning Microsoft Azure -A Hands-On Training [Azure][Cloud]', 'Azure', 'Vijay', 'All' ),
(6, '[Azure] AZ-900 Microsoft Azure Fundamentals Exam Quick Prep', 'Azure', 'Vijay', 'Beginner' ),
(7, 'AZ-900: Microsoft Azure Fundamentals Practice Tests', 'Azure', 'Pooja', 'Beginner' ),
(8, 'GUI Automation using Python | Use Python for [Automation]', 'Python', 'Vijay', 'All' ),
(9, 'Python Automation for Everyone', 'Python', 'Vijay', 'Beginner' ),
(10, '[Active Directory] Management using Windows PowerShell', 'Azure', 'Vijay', 'Intermediate' ),
(11, 'Advanced Scripting & Tool Making using Windows PowerShell', 'PowerShell', 'Vijay', 'Intermediate' ),
(12, 'Learning Task Automation using Windows PowerShell', 'PowerShell', 'Vijay', 'All' ),
(13, 'Learn Azure Functions in a Weekend', 'Azure', 'Vijay', 'Intermediate' )

--########===================================########
--========###################################========
--========###################################========
--########===================================########


-- Script 2

DROP TABLE IF EXISTS StudentReviews;

CREATE TABLE StudentReviews (
  ReviewTime VARCHAR(200) NOT NULL,
  ReviewText VARCHAR(200) NOT NULL
);

INSERT INTO StudentReviews (ReviewTime, ReviewText ) 
VALUES
(4, 'I Love  Azure Functions')


--########===================================########
--========###################################========
--========###################################========
--########===================================########