### Check my code <a href="https://app.mode.com/editor/ahmedosaka/reports/507f2df35d4a">here</a>
### please note that my answers could be wrong XD
### Exercise 0: Count how many users we have
### code: 
    SELECT 
      COUNT(Distinct COALESCE(parent_user_id, id))
    FROM 
      dsv1069.users
    WHERE
      merged_at is NULL 

### Exercise 1: Find out how many users have ever ordered
    SELECT 
      COUNT(distinct users.id)
    FROM 
      dsv1069.orders
    INNER JOIN 
      dsv1069.users
    ON 
      orders.user_id = users.id
OR YOU CAN USER THE FOLLOWING CODE FOR THE SAME RESULT:

    SELECT 
      COUNT(distinct orders.user_id)
    FROM 
      dsv1069.orders
    INNER JOIN 
      dsv1069.users
    ON 
      orders.user_id = users.id
      
### Exercise 2:
####    --Goal find how many users have reordered the same item
    SELECT 
    COUNT(distinct user_id) as users_who_reordered
    FROM
      (
      SELECT 
        user_id, 
        item_id, 
        count(Distinct line_item_id) as times_user_ordered
      FROM 
        dsv1069.orders
      GROUP BY
        user_id, item_id
      ) AS user_level_orders
    WHERE
      times_user_ordered >1
      
### Exercise 3:
#### --Do users even order more than once?
    SELECT 
      count(distinct user_id)
    FROM 
      (
      SELECT 
        user_id, 
        count(Distinct invoice_id) as count_invoice_id
      FROM 
        dsv1069.orders
      GROUP BY
        user_id
      ) as invoice_count
    WHERE
     count_invoice_id>1

### Exercise 4:
#### --Orders per item

    SELECT 
      item_id,
      count(line_item_id)
    FROM 
      dsv1069.orders
    GROUP BY
      item_id
    order BY
      item_id


### Exercise 5:
##### --Orders per category

    SELECT 
     item_category,
     COUNT(line_item_id)
    FROM 
     dsv1069.orders
    GROUP BY 
      item_category

### Exercise 6:
##### --Goal: Do user order multiple things from the same category?
    -- Do user order multiple things from the same category?
    
    SELECT 
     user_id,
     item_category,
     count(line_item_id) as time_ordered
    FROM 
     dsv1069.orders
    GROUP BY
       item_category, user_id
    ORDER BY 
      user_id