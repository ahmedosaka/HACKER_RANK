#Notes
##### question one 
##### To get the answer, i used the following code :
select *\
from tracks\
where \
Milliseconds >= 5000000;

and to check if my answer is correct, i used to following code:

select *\
from tracks\
order by Milliseconds desc
#

<a href="https://image.prntscr.com/image/qdQV89vIQZCiEeay63_b_g.png"><img src="https://image.prntscr.com/image/qdQV89vIQZCiEeay63_b_g.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/osKye_1zSempR_HeQvdvqg.png"><img src="https://image.prntscr.com/image/osKye_1zSempR_HeQvdvqg.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/KFESZQzWTLC10qIl6TaeFQ.png"><img src="https://image.prntscr.com/image/KFESZQzWTLC10qIl6TaeFQ.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/Ey4gbC7eR9_hG7SKjLY6KQ.png"><img src="https://image.prntscr.com/image/Ey4gbC7eR9_hG7SKjLY6KQ.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/03fYkjkTRr_G_7O4gleglw.png"><img src="https://image.prntscr.com/image/03fYkjkTRr_G_7O4gleglw.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/pJDGcMtXSgSGFXND33CwsQ.png"><img src="https://image.prntscr.com/image/pJDGcMtXSgSGFXND33CwsQ.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/zJ-nS-50QpuGtJAExMj76w.png"><img src="https://image.prntscr.com/image/zJ-nS-50QpuGtJAExMj76w.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/g1jhDYDyTeGHUKz3GboNrg.png"><img src="https://image.prntscr.com/image/g1jhDYDyTeGHUKz3GboNrg.png" alt="Screenshot-10" border="0"></a>
<a href="https://image.prntscr.com/image/QLOFn8HURqihifvY7ZXtDw.png"><img src="https://image.prntscr.com/image/QLOFn8HURqihifvY7ZXtDw.png" alt="Screenshot-10" border="0"></a>

#### Q1
select *
from tracks
where 
Milliseconds >= 5000000;

#### Q2
select * from invoices
where total between 5 and 15;

#### Q3
select *
from customers 
where state = "RJ" or state = "DF" or state = "AB" or state = "BC" or state = "CA" or state = "WA" or state = "NY"
and firstname = "Jack" and lastname = "smith";


#### Q4
select *
from invoices
where customerid = "56" or "58"
and total between 1 and 5
and invoiceid = "315"

#### 5
select * 
from tracks
where name like "All%"

#### Q6
select *
from customers 
where email like "J%gmail.com"

#### Q7
select *
from invoices
where (billingcity = "Brasília" or billingcity = "Edmonton" or billingcity= "Vancouver")
order by invoiceid desc

#### Q8
select customerid, count(invoiceid) as number_of_orders
from invoices
group by customerid 
order by customerid desc

#### Q9
select albumid, count(trackid) as number_of_tracks
from tracks
group by albumid
having number_of_tracks >= 12;