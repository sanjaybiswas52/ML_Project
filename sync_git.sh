#!/bin/bash

set +x

git init
git add README.md
git remote add origin https://github.com/sanjaybiswas52/ML_Project.git
git branch -M main
git push -u origin main --force
