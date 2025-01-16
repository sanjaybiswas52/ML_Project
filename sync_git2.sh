#!/bin/bash

set +x

git init
git pull origin main
git add .
git commit -m "Your commit message"
git push -u origin main
git pull origin main

git commit -m "Initial commit"

