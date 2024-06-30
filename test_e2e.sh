export PLAYWRIGHT_HTML_HOST=0.0.0.0
export PLAYWRIGHT_HTML_PORT=8181

(
  cd e2e && \
    npx playwright test &&
    npx playwright show-report --host $PLAYWRIGHT_HTML_HOST --port $PLAYWRIGHT_HTML_PORT
)
