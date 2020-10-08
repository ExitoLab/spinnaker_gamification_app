# Spinnaker Gamification App

## Mission & Vision

Vision: gamify and provide extrinsic motivation for Spinnaker and CDF contributions
Mission: by building an application that tracks indivudal contributions with a leaderboard and some other select aggregate data, and correlates those contributions to configurable professional profiles

We find a lot of use in this app: https://github.com/cncf/devstats and https://spinnaker.devstats.cd.foundation/ but are looking for individualized data


## Team

- Ige Adetokunbo
- Nikema Prophet
- Rosalind Benoit 
- Kuti
- Vishal

## Stack
The following technologies will be used 

1. Django rest framework 
2. React Js 
3. CI/ CD (Spinnaker, Jenkins, Github Actions)
4. Postgres MySQL


The various features of the application:

1. Integrate www.linkedin.com api 
2. Integrate https://github.com api 
3. If user supplies linkedin and github information. it will be displayed on the website and if nothing is supplied it will display basic information from github and a link to the registration page for user to register and add data to their contribution profile. 
4. A cron job (Golang) will run periodically and get information from github and insert into database. This will be a microservice  
5. The cron job will be able to trigger from the admin UI. Supply date and it will get information from linkedln
