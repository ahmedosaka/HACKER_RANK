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
#### Exercise 3: Write a query that returns a table of assignment events.Please include all of the
#### relevant parameters as columns (Hint: A previous exercise as a template)
#### code:
    SELECT 
      event_id,
      event_time,
      user_id,
      platform,
      MAX(CASE
              WHEN parameter_name = 'test_id' 
              THEN CAST(parameter_value AS INT)
              ELSE NULL
          END) AS test_id,
      MAX(CASE
          WHEN parameter_name = 'test_assignment' 
          THEN parameter_value
          ELSE NULL
        END) AS test_assignment
    FROM 
      dsv1069.events
    WHERE 
      event_name = 'test_assignment'
    GROUP BY 
      event_id,
      event_time,
      user_id,
      platform
    ORDER BY 
      event_id
    
