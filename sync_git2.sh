#!/bin/bash

set +x

cp /Users/sanjaybiswas/Library/DBeaverData/workspace6/General/Scripts/*.sql /Users/sanjaybiswas/Documents/Pycharm/pythonProject/SQL_Script
git init
git config --global sanjaybiswas52
git config --global sanjaybiswas52@gmail.com
git remote add origin https://github.com/sanjaybiswas52/ML_Project.git
git pull origin main
git add README.md
git add .
git commit -m "Initial commit"
git commit -m "Your commit message"
git push -u origin main
