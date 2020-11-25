# Exercise 1 & 2 & 3:
SELECT \
  event_id,\
  event_time,\
  user_id,\
  platform,\
  MAX(CASE when parameter_name = 'item_id'\
        then cast(parameter_value as INT)\
        else NULL END) as item_id, \
  MAX(CASE when parameter_name = 'referrer'\
        then parameter_value\
        else NULL END) as item_id\
FROM \
  dsv1069.events \
WHERE \
  event_name = 'view_item'\
  Group by \
  event_id,\
  event_time,\
  user_id,\
  platform


<a href="https://image.prntscr.com/image/DVHbN4X-Sl_3v0VqqPtMWg.png"><img src="https://image.prntscr.com/image/DVHbN4X-Sl_3v0VqqPtMWg.png" alt="Screenshot-10" border="0"></a>

