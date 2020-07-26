# Spinnaker Gamification App

The following technologies will be used 

1. Django rest framework 
2. Golang 
3. React Js 
4. CI/ CD (Spinnaker, Jenkins, Github Actions)


The various features of the application

1. Integrate www.linkedin.com api 
2. Integrate https://github.com api 
3. if user supplies linkedin and github information. it will be displayed on the website and if nothing is supplied it will display a 
registration page for user to register 
4. A cron job (Golang) will run periodically and get information from github and insert into database. This will be a microservice  
5. The cron job will be able to trigger from the admin UI. Supply date and it will get information from linkedln 


Question:
1. What exact information of users should be displayed on the home page
2. We will need a wireframe of the homepage.. Just an idea, we can come up with the rest of the information.