                                        --  Assignment 4: SQL -- 

-- 1. Select employee details  of dept number 10 or 30
SELECT * FROM Emp WHERE DeptNo IN (10, 30);

-- 2.  Fetch all the dept details with more than 1 employee
SELECT DeptNo, Dname, Loc 
FROM Dept 
WHERE DeptNo IN (SELECT DeptNo FROM Emp GROUP BY DeptNo HAVING COUNT(*) > 1);

-- 3. Fetch employee details whose name starts with the letter “S”
SELECT * FROM Emp WHERE Ename LIKE 'S%';

-- 4. Select Emp Details Whose experience is more than 2 years
SELECT * FROM Emp 
WHERE DATEDIFF(YEAR, Hire_Date, GETDATE()) > 2;

-- 5. Replace the char “a” with “#” in Employee Name
SELECT Ename, REPLACE(Ename, 'a', '#') AS Modified_Name FROM Emp;

-- 6. Fetch employee name and his/her manager name
SELECT e1.Ename AS Employee, e2.Ename AS Manager
FROM Emp e1
LEFT JOIN Emp e2 ON e1.Mgr = e2.EmpNo;

-- 7. Fetch Dept Name, Total Salary of the Dept
SELECT d.Dname, SUM(e.Sal) AS Total_Salary
FROM Emp e 
JOIN Dept d ON e.DeptNo = d.DeptNo
GROUP BY d.Dname;

-- 8. Fetch ALL employee details along with department name and location
SELECT e.*, d.Dname, d.Loc 
FROM Emp e 
RIGHT JOIN Dept d ON e.DeptNo = d.DeptNo

-- 9. Increase the employee salary by 10%
UPDATE Emp 
SET Sal = Sal * 1.10;

-- 10. Delete employees belonging to Chennai location
DELETE FROM Emp 
WHERE DeptNo IN (SELECT DeptNo FROM Dept WHERE Loc = 'Chennai');

-- 11. Get Employee Name and Gross Salary (Sal + Commission)
SELECT Ename, (Sal + ISNULL(Commission, 0)) AS Gross_Salary FROM Emp;

-- 12. Increase the data length of the column Ename in Emp table
ALTER TABLE Emp ALTER COLUMN Ename VARCHAR(250);

-- 13. Get current datetime
SELECT GETDATE();

-- 14. Create STUDENT table with 5 columns
CREATE TABLE STUDENT (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Course VARCHAR(50),
    EnrollmentDate DATE
);

-- 15. Get the number of employees getting salary more than 10000
SELECT COUNT(*) AS Emp_Count FROM Emp WHERE Sal > 10000;

-- 16. Fetch minimum, maximum, and average salary
SELECT MIN(Sal) AS Min_Salary, MAX(Sal) AS Max_Salary, AVG(Sal) AS Avg_Salary FROM Emp;

-- 17. Fetch number of employees in each location
SELECT d.Loc, COUNT(e.EmpNo) AS Employee_Count
FROM Emp e
JOIN Dept d ON e.DeptNo = d.DeptNo
GROUP BY d.Loc;

-- 18. Display employee names in descending order
SELECT Ename FROM Emp ORDER BY Ename DESC;

-- 19. Create a backup table (EMP_BKP) from EMP table
SELECT * INTO EMP_BKP FROM Emp;

-- 20. Fetch first 3 characters from employee name appended with salary
SELECT LEFT(Ename, 3) + CAST(Sal AS VARCHAR) AS Employee_Info FROM Emp;

-- 21. Get details of employees whose name starts with "S"
SELECT * FROM Emp WHERE Ename LIKE 'S%';

-- 22. Get details of employees who work in Bangalore location
SELECT e.* FROM Emp e 
JOIN Dept d ON e.DeptNo = d.DeptNo
WHERE d.Loc = 'Bangalore';

-- 23. Get employee details whose name starts with any letter between A and K
SELECT * FROM Emp WHERE Ename LIKE '[A-K]%';

-- 24. Display employees whose manager name is "Stefen"
SELECT e1.* FROM Emp e1 
JOIN Emp e2 ON e1.Mgr = e2.EmpNo
WHERE e2.Ename = 'Stefen';

-- 25. List managers with the maximum number of employees under them
SELECT Mgr, COUNT(*) AS Employee_Count 
FROM Emp 
WHERE Mgr IS NOT NULL 
GROUP BY Mgr 
ORDER BY Employee_Count DESC 
LIMIT 1;

-- 26. Employee details, department details, and manager details of the employee with second highest salary
SELECT e1.*, d.*, e2.Ename AS Manager_Name
FROM Emp e1
JOIN Dept d ON e1.DeptNo = d.DeptNo
LEFT JOIN Emp e2 ON e1.Mgr = e2.EmpNo
WHERE e1.Sal = (SELECT DISTINCT Sal FROM Emp ORDER BY Sal DESC OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY);

-- 27. List all details of all managers
SELECT * FROM Emp WHERE EmpNo IN (SELECT DISTINCT Mgr FROM Emp WHERE Mgr IS NOT NULL);

-- 28. List details and total experience of all managers
SELECT e.*, DATEDIFF(YEAR, Hire_Date, GETDATE()) AS Experience 
FROM Emp e 
WHERE EmpNo IN (SELECT DISTINCT Mgr FROM Emp WHERE Mgr IS NOT NULL);

-- 29. List employees who are managers, take commission less than 1000, and work in Delhi
SELECT e.* FROM Emp e 
JOIN Dept d ON e.DeptNo = d.DeptNo
WHERE e.EmpNo IN (SELECT DISTINCT Mgr FROM Emp WHERE Mgr IS NOT NULL)
AND ISNULL(e.Commission, 0) < 1000 
AND d.Loc = 'Delhi';

-- 30. Display details of employees who are senior to Martin
SELECT * FROM Emp 
WHERE Hire_Date < (SELECT Hire_Date FROM Emp WHERE Ename = 'Martin');