##### Exercise 1: Figure out how many tests we have running right now
##### code:
    SELECT 
      distinct parameter_value
    FROM 
      dsv1069.events 
    where 
      event_name = 'test_assignment'
      AND
      parameter_name = 'test_id'
       
      
