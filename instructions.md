# Spinnaker Gamification App

## Intructions for setup

## 
The following technologies will be used 

1. Clone the repo 
2. Run the command ` pip install -r requirements.txt `
3. Create a file .env and add it to your project, include all your values for database and github
5. Run the command ` python manage.py makemigrations `
6. Run the command ` python manage.py migrate `
7. Run the command ` python manage.py runserver ` to start up the app. 

## Next steps 

Sample of .env file. Pls ensure you are not commiting your .env to gihub, although `.env` has been added to environment variables

ON Mac or linux machine leave it has export but on windows machine replace EXPORT with SET

```
export DATABASE_HOST=
export DATABASE_NAME=
export DATABASE_USER=
export DATABASE_PASSWORD=
export DATABASE_PORT=
export GITHUB_USER=
export GITHUB_TOKEN=
```