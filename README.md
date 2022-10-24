# DTSE Full-Stack Developer assignment - work process

Project is available in 'prediction-assignment' folder.

## Work process

1. installed requirements
2. learning flask
3. set up localhost and required routes ('/' and '/api/prediction')
4. built html page with form on '/' route
5. in main.py figure out which parameters go to joblib
- studied main.py file to understand the process flow
- tested outcomes using sample output parameters
- if a parameter did not provide expected result, I removed it from the code
6. added function to '/api/prediction' that accepts data from javaScript and created dictionary
7. Added table to HTML that takes output from prediction model and adds time stamp
8. Added input validations for HTML form

# Used tools and technologies
1. javaScript
2. Python
- Flask
- Pandas
- datetime
- logging
3. Bootstrap

# Struggles during project
1. Understanding main.py outputs and which one is the predictions that should be used on the main page. This took me most of the time to figure out.
2. Using Flask for the first time. I had not an experience with this extension before.
3. Planning process at the start of project, mainly because of the above two points.

# Learnings
1. Flask extension for building REST APIs
2. Elimination process on events happening in main.py, where I had to remove code that was not needed. 
