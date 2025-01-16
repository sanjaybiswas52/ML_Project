#!/bin/bash

set +x

git add .
git commit -m "Syncing Python script from VSCode"
git push origin "sanjaybiswas52/ML_Project"
git pull origin <branch>
