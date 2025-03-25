# Write your MySQL query statement below
Select 
      player_id,
	  min(event_date) first_login 
from Activity 
Group By player_id;