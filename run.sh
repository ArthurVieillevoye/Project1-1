function finish {
  npx kill-port 8000
}

trap finish SIGINT

echo 'You are running ASLD'

cd ./ASLD
pipenv run python manage.py runserver &
cd ..

cd ./ASLD/frontend 
npm run dev