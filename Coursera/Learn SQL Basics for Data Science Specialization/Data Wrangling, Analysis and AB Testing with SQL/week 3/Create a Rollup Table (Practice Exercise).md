### Exercise 1: 
#### code:
    SELECT
        Date(created_at), count(invoice_id)
    FROM 
        dsv1069.orders
    GROUP BY 
        DATE(created_at)
    order by 
        DATE(created_at) desc
<a href="https://image.prntscr.com/image/KyrC1BfKSpmY3pSnn47b6A.png"><img src="https://image.prntscr.com/image/KyrC1BfKSpmY3pSnn47b6A.png" alt="Screenshot-10" border="0"></a>


### Exercise 2: 
#### code:
    SELECT
        date(date), orders.count_invoice_id
    FROM 
    dsv1069.dates_rollup
    JOIN 
    (SELECT
        Date(created_at) as created_at, count(invoice_id) as count_invoice_id
    FROM 
        dsv1069.orders
    GROUP BY 
        DATE(created_at)
    order by 
        DATE(created_at) desc) as orders
    ON 
        date(date) = orders.created_at
<a href="https://image.prntscr.com/image/dWa0JTzQT6iJFh1YK4UDJQ.png"><img src="https://image.prntscr.com/image/dWa0JTzQT6iJFh1YK4UDJQ.png" alt="Screenshot-10" border="0"></a>



### Exercise 3: 
#### code:
    SELECT
        date(date), orders.count_invoice_id, orders.count_users_ordered
    from 
        dsv1069.dates_rollup
    JOIN 
    (SELECT
        Date(created_at) as created_at, count(invoice_id) as count_invoice_id, COUNT(distinct orders.user_id) as count_users_ordered
    FROM 
        dsv1069.orders
    GROUP BY 
        DATE(created_at)
    order by 
        DATE(created_at) desc) as orders
    ON 
        date(date) = orders.created_at

<a href="https://image.prntscr.com/image/hpyFPhDkQz2hf1PlrXLSBg.png"><img src="https://image.prntscr.com/image/hpyFPhDkQz2hf1PlrXLSBg.png" alt="Screenshot-10" border="0"></a>


### Exercise 4: 
#### code:

     SELECT 
      extract(year from date) as year, 
      extract(week from date) as week, 
      COUNT(orders.invoice_id)
    FROM 
      dsv1069.dates_rollup
    LEFT JOIN 
      dsv1069.orders
    ON 
      extract(week from date) = extract(week from orders.created_at)
    AND 
      extract(year from date) = extract(year from orders.created_at)
    GROUP BY 
      extract(year from date), extract(week from date)
    ORDER BY year DESC, week ASC
<a href="https://image.prntscr.com/image/F15fF5tZSm2hK07S60eERA.png"><img src="https://image.prntscr.com/image/F15fF5tZSm2hK07S60eERA.png" alt="Screenshot-10" border="0"></a>

### Exercise 5: 
#### code:

    SELECT 
      extract(year from date) as year, extract(week from date) as week, COUNT(orders.invoice_id) as count_of_orders
    FROM 
      dsv1069.dates_rollup
    LEFT JOIN 
      dsv1069.orders
    ON 
      extract(week from date) = extract(week from orders.created_at)
    AND 
      extract(year from date) = extract(year from orders.created_at)
    GROUP BY 
      extract(year from date), extract(week from date)
    ORDER BY year DESC, week ASC
 
<a href="https://image.prntscr.com/image/wdhVVyDaTh6hLyA_OIvOvA.png"><img src="https://image.prntscr.com/image/wdhVVyDaTh6hLyA_OIvOvA.png" alt="Screenshot-10" border="0"></a>