docker system prune -f
 
docker-compose -f docker-compose.yaml run dj python3.8 manage.py makemigrations
docker-compose -f docker-compose.yaml run dj python3.8 manage.py migrate

docker-compose up -d