#!/usr/bin/env bash

set -x
set -e
set -u
set -o pipefail

npm start & SERVER_PID=$!
sleep 5

cd script-free-implementation
pipenv run gen
pipenv run python3 test_script/scratch_exp/point_runner_to_latest.py
pipenv run python3 -m test_script.scratch_exp.footer_links_runner.py
cd ..

kill -TERM $SERVER_PID