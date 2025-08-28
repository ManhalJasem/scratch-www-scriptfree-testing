#!/usr/bin/env bash
set -Eeuo pipefail
API_HOST=http://localhost:8080/https://api.scratch.mit.edu ASSET_HOST=http://localhost:8080/https://assets.scratch.mit.edu BACKPACK_HOST=http://localhost:8080/https://backpack.scratch.mit.edu PROJECT_HOST=http://localhost:8080/https://projects.scratch.mit.edu FALLBACK=https://scratch.mit.edu npm start & SERVER_PID=$!
sleep 20

# Run tests
SMOKE_USERNAME=username SMOKE_PASSWORD=password ROOT_URL=http://localhost:8333/ \
  node_modules/.bin/jest ./test/integration/homepage-rows.test.js -t 'Featured Studios link'

# Kill the server after tests finish
pkill -TERM node
pkill chromedriver