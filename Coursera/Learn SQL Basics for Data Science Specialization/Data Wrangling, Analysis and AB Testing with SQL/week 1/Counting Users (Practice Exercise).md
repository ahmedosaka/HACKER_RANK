# Exercise 1 :
# Exercise 2: 

 
#### ⁂　We’ll be using the users table to answer the question “How many new users are
#### added each day?“. Start by making sure you understand the columns in the table.
#### ⁂　WIthout worrying about deleted user or merged users, count the number of users
#### added each day.

### code:
 SELECT  DATE(created_at) Date, COUNT(DISTINCT id) totalCOunt\
 FROM    dsv1069.users\
 GROUP   BY  DATE(created_at)
 
 <a href="https://image.prntscr.com/image/FVnYlERtQ9GhsoN-AncIKw.png"><img src="https://image.prntscr.com/image/FVnYlERtQ9GhsoN-AncIKw.png" alt="Screenshot-10" border="0"></a>

 #
 #Exercise 3:
 #### Consider the following query. Is this the right way to count merged or deleted
#### users? If all of our users were deleted tomorrow what would the result look like?

My answer : 
I don't think this is the right way to count deleted users. It should be that we count the deleted_on where deleted_on is not Null, else it will just result that we will find only the users that are still active. 
the answer for the question if the users were all deleted, it will look like the following :

<a href="https://image.prntscr.com/image/AB8aDidxT6uxGiE5U6sjAg.png"><img src="https://image.prntscr.com/image/AB8aDidxT6uxGiE5U6sjAg.png" alt="Screenshot-10" border="0"></a>

Starter Code:

SELECT\
date(created_at) AS day,\
COUNT(*) AS users\
FROM\
dsv1069.users\
WHERE\
deleted_at IS NULL\
AND\
(id <> parent_user_id OR parent_user_id IS NULL)\
GROUP BY\
date(created_at)

suggested code :

SELECT\
date(created_at) AS day,\
COUNT(*) AS users\
FROM\
dsv1069.users\
WHERE\
deleted_at IS not NULL\
AND\
(id <> parent_user_id OR parent_user_id IS NULL)\
GROUP BY\
date(created_at)

data after running my code would look like that : 
<a href="https://image.prntscr.com/image/-uNI3DsfRHGwoAmT3b_haw.png"><img src="https://image.prntscr.com/image/-uNI3DsfRHGwoAmT3b_haw.png" alt="Screenshot-10" border="0"></a>


#
# Exercise 4:
####  Count the number of users deleted each day. Then count the number of users removed due to merging in a similar way.
####Starter Code: (Use the result from #2 as a guide)

##### My code:

SELECT  DATE(created_at) Date, COUNT(DISTINCT id) totalCOunt\
FROM    dsv1069.users\
where deleted_at is not Null \
GROUP   BY  DATE(created_at)

#### You can find that i have counted the deleted users using the same code of exercise 2 and just modified that part where deleted_on is not Null
##### Result:
<a href="https://image.prntscr.com/image/sSd_RsPhRbyjJk5OxsYQcQ.png"><img src="https://image.prntscr.com/image/sSd_RsPhRbyjJk5OxsYQcQ.png" alt="Screenshot-10" border="0"></a>
#
# Exercise 5: 
#### Use the pieces you’ve built as subtables and create a table that has a column for
#### the date, the number of users created, the number of users deleted and the number of users merged that day.

code:
SELECT new.day,\
  new.new_added_users,\
  COALESCE(deleted.deleted_users, 0) AS deleted_users,\
  COALESCE(merged.merged_users, 0) AS merged_users,\
  (new.new_added_users - COALESCE(deleted.deleted_users, 0) - COALESCE(merged.merged_users, 0)) \
    AS net_added_users\
FROM (SELECT DATE(created_at) AS day,\
    COUNT(*) AS new_added_users\
  FROM dsv1069.users\
  GROUP BY day) new\
LEFT JOIN \
  (SELECT DATE(created_at) AS day,\
    COUNT(*) AS deleted_users\
  FROM dsv1069.users\
  WHERE deleted_at IS NOT NULL\
  GROUP BY day) deleted\
  ON deleted.day = new.day\
LEFT JOIN \
  (SELECT DATE(merged_at) AS day,\
    COUNT(*) AS merged_users\
  FROM dsv1069.users\
  WHERE id <> parent_user_id\
  AND parent_user_id IS NOT NULL\
  GROUP BY day) merged\
ON merged.day = new.day

<a href="https://image.prntscr.com/image/yiJMfKThS5ONoUqY7y7SIw.png"><img src="https://image.prntscr.com/image/yiJMfKThS5ONoUqY7y7SIw.png" alt="Screenshot-10" border="0"></a>
