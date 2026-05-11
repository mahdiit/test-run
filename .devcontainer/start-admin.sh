#!/bin/sh
set -eu

if ! pgrep -f "python3 /usr/local/bin/admin-server.py" >/dev/null; then
  nohup python3 /usr/local/bin/admin-server.py >/tmp/mrh-admin.log 2>&1 &
fi
