#!/bin/bash
# Authors: Leon, Arthur and Carlos
# Maastricht University
function finish {
  pipenv --rm
  npx kill-port 8000
}

trap finish SIGINT

echo 'You are initializing ASLD'

isPipenv=$(pip list | grep pipenv)
if [[ -z $isPipenv ]]
then
    echo 'No pipenv library. Installing pipenv.'
    pip install pipenv
fi

version=$(python -V)
echo ${version:(-6):4}
if (( "${version:(-6):4}" < "3.8" ))
then
    echo "No Python Version Supported, minimum version 3.8!" 
    exit
fi


cd ./ASLD/frontend


isNPM=$(npm -V)
if [[ -z $isNPM ]]
then
    echo 'No npm library. Please first install Node and npm.'
    exit
fi
npm install 

cd ../..

pipenv install

cd ./ASLD
pipenv run python manage.py runserver &
cd ..

cd ./ASLD/frontend 
npm run dev