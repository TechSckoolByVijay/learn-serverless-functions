
DROP TABLE IF EXISTS StudentsData;

CREATE TABLE StudentsData (
  UserName VARCHAR(200) NOT NULL,
  CourseID VARCHAR(200) NOT NULL,
  TransactionStatus VARCHAR(50) NOT NULL,
  User_Email VARCHAR(100) NOT NULL
);

-- INSERT INTO StudentsData (UserName, CourseID, TransactionStatus, User_Email ) VALUES ('SainiVijay', 'Course101', 'SUCCESS', 'VijaySaini@professional@gmail.com' );

select * from StudentsData;




DROP TABLE IF EXISTS FailedToConvert;

CREATE TABLE FailedToConvert (
  UserName VARCHAR(200) NOT NULL,
  CourseID VARCHAR(200) NOT NULL,
  TransactionStatus VARCHAR(50) NOT NULL,
  User_Email VARCHAR(100) NOT NULL
);

--INSERT INTO FailedToConvert (UserName, CourseID, TransactionStatus, User_Email ) VALUES ('SainiVijay', 'Course101', 'SUCCESS', 'VijaySaini@professional@gmail.com' );

select * from FailedToConvert;