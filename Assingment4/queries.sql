                                     


SELECT * FROM Emp WHERE DeptNo IN (10, 30);


SELECT DeptNo, Dname, Loc 
FROM Dept 
WHERE DeptNo IN (SELECT DeptNo FROM Emp GROUP BY DeptNo HAVING COUNT(*) > 1);


SELECT * FROM Emp WHERE Ename LIKE 'S%';


SELECT * FROM Emp 
WHERE DATEDIFF(YEAR, Hire_Date, GETDATE()) > 2;


SELECT Ename, REPLACE(Ename, 'a', '#') AS Modified_Name FROM Emp;


SELECT e1.Ename AS Employee, e2.Ename AS Manager
FROM Emp e1
LEFT JOIN Emp e2 ON e1.Mgr = e2.EmpNo;


SELECT d.Dname, SUM(e.Sal) AS Total_Salary
FROM Emp e 
JOIN Dept d ON e.DeptNo = d.DeptNo
GROUP BY d.Dname;


SELECT e.*, d.Dname, d.Loc 
FROM Emp e 
RIGHT JOIN Dept d ON e.DeptNo = d.DeptNo


UPDATE Emp 
SET Sal = Sal * 1.10;


DELETE FROM Emp 
WHERE DeptNo IN (SELECT DeptNo FROM Dept WHERE Loc = 'Chennai');


SELECT Ename, (Sal + ISNULL(Commission, 0)) AS Gross_Salary FROM Emp;


ALTER TABLE Emp ALTER COLUMN Ename VARCHAR(250);


SELECT GETDATE();


CREATE TABLE STUDENT (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Course VARCHAR(50),
    EnrollmentDate DATE
);


SELECT COUNT(*) AS Emp_Count FROM Emp WHERE Sal > 10000;


SELECT MIN(Sal) AS Min_Salary, MAX(Sal) AS Max_Salary, AVG(Sal) AS Avg_Salary FROM Emp;


SELECT d.Loc, COUNT(e.EmpNo) AS Employee_Count
FROM Emp e
JOIN Dept d ON e.DeptNo = d.DeptNo
GROUP BY d.Loc;

SELECT Ename FROM Emp ORDER BY Ename DESC;

e
SELECT * INTO EMP_BKP FROM Emp;


SELECT LEFT(Ename, 3) + CAST(Sal AS VARCHAR) AS Employee_Info FROM Emp;


SELECT * FROM Emp WHERE Ename LIKE 'S%';


SELECT e.* FROM Emp e 
JOIN Dept d ON e.DeptNo = d.DeptNo
WHERE d.Loc = 'Bangalore';


SELECT * FROM Emp WHERE Ename LIKE '[A-K]%';


SELECT e1.* FROM Emp e1 
JOIN Emp e2 ON e1.Mgr = e2.EmpNo
WHERE e2.Ename = 'Stefen';


SELECT Mgr, COUNT(*) AS Employee_Count 
FROM Emp 
WHERE Mgr IS NOT NULL 
GROUP BY Mgr 
ORDER BY Employee_Count DESC 
LIMIT 1;


SELECT e1.*, d.*, e2.Ename AS Manager_Name
FROM Emp e1
JOIN Dept d ON e1.DeptNo = d.DeptNo
LEFT JOIN Emp e2 ON e1.Mgr = e2.EmpNo
WHERE e1.Sal = (SELECT DISTINCT Sal FROM Emp ORDER BY Sal DESC OFFSET 1 ROWS FETCH NEXT 1 ROWS ONLY);


SELECT * FROM Emp WHERE EmpNo IN (SELECT DISTINCT Mgr FROM Emp WHERE Mgr IS NOT NULL);


SELECT e.*, DATEDIFF(YEAR, Hire_Date, GETDATE()) AS Experience 
FROM Emp e 
WHERE EmpNo IN (SELECT DISTINCT Mgr FROM Emp WHERE Mgr IS NOT NULL);


SELECT e.* FROM Emp e 
JOIN Dept d ON e.DeptNo = d.DeptNo
WHERE e.EmpNo IN (SELECT DISTINCT Mgr FROM Emp WHERE Mgr IS NOT NULL)
AND ISNULL(e.Commission, 0) < 1000 
AND d.Loc = 'Delhi';

SELECT * FROM Emp 
WHERE Hire_Date < (SELECT Hire_Date FROM Emp WHERE Ename = 'Martin');
