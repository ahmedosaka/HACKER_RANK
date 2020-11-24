
#Exercise 1:
My code: 

SELECT id,\
email_address\
FROM dsv1069.users\
where deleted_at is Null;\
<a href="https://image.prntscr.com/image/cPzcLozrR8ah9K9CElX88w.png"><img src="https://image.prntscr.com/image/cPzcLozrR8ah9K9CElX88w.png" alt="Screenshot-10" border="0"></a>

#
#Exercise 2:
SELECT  count(adjective) as number_of_items, category\
FROM dsv1069.items\
Group by category;\
<a href="https://image.prntscr.com/image/DdYrDWMQSiS0e23VwrQoaw.png"><img src="https://image.prntscr.com/image/DdYrDWMQSiS0e23VwrQoaw.png" alt="Screenshot-10" border="0"></a>


#
#Exercise 3:

select * \
from  dsv1069.orders \
JOIN dsv1069.users on dsv1069.users.id = dsv1069.orders.user_id;

<a href="https://image.prntscr.com/image/QNQz3vmbSFOFroJ1wdGKIw.png"><img src="https://image.prntscr.com/image/QNQz3vmbSFOFroJ1wdGKIw.png" alt="Screenshot-10" border="0"></a>
#
#Exercise 4
SELECT\
COUNT(DISTINCT event_id) AS events\
FROM dsv1069.events\
WHERE event_name = ‘view_item’
#
#Exercise 5:
select \
COUNT(DISTINCT item_id) as item_count\
from dsv1069.orders


or : 
select \
COUNT(DISTINCT item_id) as item_count\
from dsv1069.orders\
join dsv1069.items on dsv1069.orders.item_id =dsv1069.items.id

or: 

select \
COUNT(DISTINCT item_id) as item_count\
from dsv1069.orders\
inner join dsv1069.items on dsv1069.orders.item_id =dsv1069.items.id


<a href="https://image.prntscr.com/image/rhqaQA2wSZCjDLIuDIjwbw.png"><img src="https://image.prntscr.com/image/rhqaQA2wSZCjDLIuDIjwbw.png" alt="Screenshot-10" border="0"></a>
#
#Exercise 6:

select \
users.id as user_id,\
min(orders.paid_at) as min_paid_at\
from \
dsv1069.users\
LEFT join dsv1069.orders\
on orders.user_id = users.id \
Group by \
dsv1069.users.id  

<a href="https://image.prntscr.com/image/g-w5zh3uQMO68taO4FMBLw.png"><img src="https://image.prntscr.com/image/g-w5zh3uQMO68taO4FMBLw.png" alt="Screenshot-10" border="0"></a>
#
#Exercise 7:

SELECT \
(CASE WHEN first_view IS NULL THEN false\
    ELSE true END) AS has_viewed_profile_page,\
COUNT(user_id) as users\
FROM \
  (\
  SELECT \
    users.id AS user_id,\
    MIN(event_time) as first_view\
  from \
    dsv1069.users\
  LEFT OUTER JOIN \
    dsv1069.events\
  ON \
    events.user_id = users.id \
  AND \
   event_name = 'view_user_profile'\
   GROUP BY \
    users.id\
    ) first_profile_view\
  GROUP BY \
    (CASE WHEN first_view IS NULL THEN false\
    ELSE true END)
    
<a href="https://image.prntscr.com/image/PulnDAY0RfKYL5nQFj56ZA.png"><img src="https://image.prntscr.com/image/PulnDAY0RfKYL5nQFj56ZA.png" alt="Screenshot-10" border="0"></a>
