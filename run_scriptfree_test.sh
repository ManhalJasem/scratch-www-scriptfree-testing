#!/usr/bin/env bash

set -x
set -e
set -u
set -o pipefail

API_HOST=http://localhost:8080/https://api.scratch.mit.edu ASSET_HOST=http://localhost:8080/https://assets.scratch.mit.edu BACKPACK_HOST=http://localhost:8080/https://backpack.scratch.mit.edu PROJECT_HOST=http://localhost:8080/https://projects.scratch.mit.edu FALLBACK=https://scratch.mit.edu npm start & SERVER_PID=$!
sleep 20

cd script-free-implementation
pipenv run gen
pipenv run python3 test_script/scratch_exp/point_runner_to_latest.py
pipenv run python3 -m test_script.scratch_exp.search_runner
cd ..

pkill -TERM node
pkill chromedriver