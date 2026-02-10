-- Applicant Behavior Analysis

-- Total visits per page
SELECT Page_Visited, COUNT(*) AS Total_Visits
FROM user_behavior
GROUP BY Page_Visited;

-- Exit points analysis
SELECT Page_Visited, COUNT(*) AS Exit_Count
FROM user_behavior
WHERE Exit_Page = 'Yes'
GROUP BY Page_Visited;

-- Average time spent per page
SELECT Page_Visited, AVG(Time_Spent_Seconds) AS Avg_Time_Spent
FROM user_behavior
GROUP BY Page_Visited;