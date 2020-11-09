SELECT concat(name,'(',LEFT(Occupation, 1),')')FROM OCCUPATIONS
ORDER BY Name;

SELECT concat('There are a total of ',Count(Name),' ',LOWER(Occupation),'s.')
FROM Occupations
GROUP BY Occupation
ORDER BY Count(Name), Occupation;


