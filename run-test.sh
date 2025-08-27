#!/usr/bin/env bash
set -Eeuo pipefail
npm start & SERVER_PID=$!
sleep 10

# Run tests
SMOKE_USERNAME=username SMOKE_PASSWORD=password ROOT_URL=http://localhost:8333/ \
  node_modules/.bin/jest ./test/integration/footer-links.test.js -t 'click DSA requirements link'

# Kill the server after tests finish
kill -TERM $SERVER_PID
kill $(($SERVER_PID + 14))
