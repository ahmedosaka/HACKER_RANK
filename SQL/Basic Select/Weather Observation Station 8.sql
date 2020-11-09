
SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[aeiou].*[aeiou]$';
'''

notes:
DISTINCT : to avoid the duplicates
instead of name, City has been used 
REGEXP : check it here https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/



'''