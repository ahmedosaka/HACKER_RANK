# Exercise 1:
#### Using any methods you like determine if you can you trust this events table.

### My opinion : 
#### I believe that it can be trusted since it's matching the data on events table

SELECT \
  events_201701.event_time, \
  events_201701.event_id, \
  events.event_time, \
  events.event_id\
FROM \
  dsv1069.events_201701\
LEFT JOIN dsv1069.events on events_201701.event_time = events.event_time AND  events_201701.event_id = events.event_id

#
# Exercise 2:
#### Using any methods you like, determine if you can you trust this events table. (HINT: When did
#### we start recording events on mobile)
#### we have started recording date on mobile on : 2013-01-13 21:10:30
##### code to check the dsv1069.events_ex2 table :

SELECT \
  event_time,\
  parameter_name, \
  platform\
FROM \
  dsv1069.events_ex2\
WHERE\
  platform = 'mobile web'\
ORDER BY\
  event_time ASC
 
<a href="https://image.prntscr.com/image/5CMLohnSTVmshC3n9vew-w.png"><img src="https://image.prntscr.com/image/5CMLohnSTVmshC3n9vew-w.png" alt="Screenshot-10" border="0"></a>

 #### and by checking dsv1069.events table  using the following code : 2013-03-10 13:30:31
 
 SELECT \
  event_time,\
  parameter_name, \
  platform\
FROM \
  dsv1069.events\
WHERE\
  platform = 'mobile web'\
ORDER BY\
  event_time ASC
  
  #### you can see that the first time we started recording date on mobile was on : 
  #### which means we can't trust this table. 
  <a href="https://image.prntscr.com/image/MMQ8bJ1VSWK7q5GHvpwTPg.png"><img src="https://image.prntscr.com/image/MMQ8bJ1VSWK7q5GHvpwTPg.png" alt="Screenshot-10" border="0"></a>

#
# Exercise 3: 
### Imagine that you need to count item views by day. You found this table
### item_views_by_category_temp - should you use it to answer your questiuon?
SELECT \
  *\
from \
dsv1069.item_views_by_category_temp
<a href="https://image.prntscr.com/image/MezYuuQUR-OuGq24L2tcCQ.png"><img src="https://image.prntscr.com/image/MezYuuQUR-OuGq24L2tcCQ.png" alt="Screenshot-10" border="0"></a>
##### My opinion is not, we can't use it to count item views by day since it's missing the date column.
#



# Exercise 4:
#### Exercise 4: Using any methods you like, decide if this table is ready to be used as a source of truth.
 
 
SELECT 
*
FROM
dsv1069.raw_events
limit 100

My opinion :
there is no such table. 
<a href="https://image.prntscr.com/image/HFfCClglTLakewE02ZZjkw.png"><img src="https://image.prntscr.com/image/HFfCClglTLakewE02ZZjkw.png" alt="Screenshot-10" border="0"></a>


#
# Exercise 5:
#### Is this the right way to join orders to users? Is this the right way this join.

SELECT COUNT(*)\
FROM dsv1069.orders\
JOIN dsv1069.users\
ON orders.user_id = COALESCE(users.parent_user_id, users.id)

<a href="https://image.prntscr.com/image/8p1leyvVRly2iRXtuq7-BA.png"><img src="https://image.prntscr.com/image/8p1leyvVRly2iRXtuq7-BA.png" alt="Screenshot-10" border="0"></a>
