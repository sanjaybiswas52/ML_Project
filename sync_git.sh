#!/bin/bash

set +x

cp /Users/sanjaybiswas/Library/DBeaverData/workspace6/General/Scripts/*.sql /Users/sanjaybiswas/Documents/Pycharm/pythonProject/SQL_Script
git init
git add README.md
git remote add origin https://github.com/sanjaybiswas52/ML_Project.git
git config --global
git pull origin main
git add .
git commit -m "Your commit message"
git push -u origin main
git pull origin main

git commit -m "Initial commit"

