
#### question 1 code :
    select c.customerid, (c.firstname|| " " || c.lastname) as full_name, c.address, UPPER(c.city || " " || c.country) as country
    from customers c
#### question 2 code :
    select lower(SUBSTR(e.firstname,1,4) || SUBSTR(e.lastname,1,2)) as user_id
    from employees e
#### question 3 code :
    SELECT LastName,
           (STRFTIME('%Y', 'now') - STRFTIME('%Y', HireDate)) AS Years
    FROM Employees
    WHERE Years >= 15
    ORDER BY LastName ASC
#### question 4 code :
    SELECT *
    FROM Customers
    where PostalCode is Null
#### question 5 code :
    select count(customerid), city
    from customers
    group by city
    order by count(customerid) desc
#### question 6 code :
    select i.invoiceid, (c.firstname || c.lastname|| i.invoiceid) as new_invoice_id
    from customers c
    inner join invoices i
    where new_invoice_id = "AstridGruber354"

<a href="https://image.prntscr.com/image/m6KfGyasRM61in08ViWfXQ.png"><img src="https://image.prntscr.com/image/m6KfGyasRM61in08ViWfXQ.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/kDm9OcFqQqeVVpeERFfImw.png"><img src="https://image.prntscr.com/image/kDm9OcFqQqeVVpeERFfImw.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/2_DNeAdCSkmD3wehKAXYRg.png"><img src="https://image.prntscr.com/image/2_DNeAdCSkmD3wehKAXYRg.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/hIfMvlEqR2aoeHldo729Eg.png"><img src="https://image.prntscr.com/image/hIfMvlEqR2aoeHldo729Eg.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/3B-epZqyQM_QsV1OgQ9ehQ.png"><img src="https://image.prntscr.com/image/3B-epZqyQM_QsV1OgQ9ehQ.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/l11-pVU1R727CO9RJQt0rQ.png"><img src="https://image.prntscr.com/image/l11-pVU1R727CO9RJQt0rQ.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/k8bEn0e8Tf_lnK2UlL3Jig.png"><img src="https://image.prntscr.com/image/k8bEn0e8Tf_lnK2UlL3Jig.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/zTIc__izRH2O0mhjQIs9CA.png"><img src="https://image.prntscr.com/image/zTIc__izRH2O0mhjQIs9CA.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/U5Ywz5oZS9S64_Xij23f1A.png"><img src="https://image.prntscr.com/image/U5Ywz5oZS9S64_Xij23f1A.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/9tiu4INmQN692jzPAPRJuQ.png"><img src="https://image.prntscr.com/image/9tiu4INmQN692jzPAPRJuQ.png" alt="Screenshot-10" border="0"></a>


