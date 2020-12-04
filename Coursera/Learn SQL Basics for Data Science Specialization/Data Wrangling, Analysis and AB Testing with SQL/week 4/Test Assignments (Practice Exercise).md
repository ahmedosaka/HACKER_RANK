##### Exercise 1: Figure out how many tests we have running right now
##### code:
    SELECT 
      COUNT(distinct parameter_value)
    FROM 
      dsv1069.events 
    where 
      event_name = 'test_assignment'
      AND
      parameter_name = 'test_id'
#### answer could be tests.
#
#### Exercise 2: Check for potential problems with test assignments. For example Make sure there
#### is no data obviously missing (This is an open ended question)
#### code:

    SELECT 
      *
    FROM 
      dsv1069.events 
    where 
      event_name = 'test_assignment'
      AND
      parameter_name = 'test_id'
 
#### I just check using Null value for both event_name and parameter_name and there seem to be no Null values so it should be okay.      
#
