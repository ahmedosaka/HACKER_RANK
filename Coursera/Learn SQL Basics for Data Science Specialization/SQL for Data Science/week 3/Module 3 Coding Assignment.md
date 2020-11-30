##### question 1 code
    select albums.title, tracks.name
    from albums
    left join tracks on albums.albumid = tracks.albumid
    where albums.title = "Californication"

##### question 2 code
    select c.customerid, c.firstname, c.lastname , c.city, c.email, count(i.invoiceid)
    from 
    customers c
    left join invoices i on c.customerid = i.customerid 
    where c.firstname = "František" and c.lastname = "Wichterlová"
##### question 3 code
    select a.title as album_title, t.name as track_name , t.albumid as albumid, t.trackid as trackid
    from albums a 
    left join tracks t on a.albumid = t.albumid 
    where t.trackid = 12 and a.title like "For Those About to Rock We Salute You" 

##### question 4 code

    SELECT M.LastName AS Manager, 

       E.LastName AS Employee

    FROM 
        Employees E 
    INNER JOIN 
        Employees M 
    ON E.ReportsTo = M.EmployeeID

##### question 5 code
    select a.artistid, a.name, m.title
    from artists a
    left join albums m on a.artistid = m.artistid 
    where m.title is Null
##### question 6 code
    select firstname, lastname
    from employees 
    Union 
    select 
    firstname,lastname
    from customers 
    order by 
    lastname desc
##### question 7 code
    SELECT C.FirstName,
           C.LastName,
           C.City AS CustomerCity,
           I.BillingCity
    FROM Customers C
    INNER JOIN Invoices I
    ON C.CustomerId = I.CustomerId
    WHERE CustomerCity != BillingCity



<a href="https://image.prntscr.com/image/eB8Fg4BGQb29K5aJzQPZ0w.png"><img src="https://image.prntscr.com/image/eB8Fg4BGQb29K5aJzQPZ0w.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/fUXujP8yQqOAQvoPqTo0NA.png"><img src="https://image.prntscr.com/image/fUXujP8yQqOAQvoPqTo0NA.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/F3SXhNFXRHm1xBTTHqNrDA.png"><img src="https://image.prntscr.com/image/F3SXhNFXRHm1xBTTHqNrDA.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/M7usQPuvTfyRWduHb2mJHA.png"><img src="https://image.prntscr.com/image/M7usQPuvTfyRWduHb2mJHA.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/0yG5Q9Y6TfK8BY7Powe0lw.png"><img src="https://image.prntscr.com/image/0yG5Q9Y6TfK8BY7Powe0lw.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/wYhypD9PSj6hSMZNN-Pl8Q.png"><img src="https://image.prntscr.com/image/wYhypD9PSj6hSMZNN-Pl8Q.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/hAdD-yWVRsqo8SWaqJhNUQ.png"><img src="https://image.prntscr.com/image/hAdD-yWVRsqo8SWaqJhNUQ.png" alt="Screenshot-10" border="0"></a>



