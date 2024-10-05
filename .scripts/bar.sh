#/bin/sh

if pgrep '^polybar' > /dev/null; then
  exit 0
fi

polybar mybar &
polybar second &
