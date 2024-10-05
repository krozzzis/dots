#/bin/sh

if pgrep '^polybar' > /dev/null; then
  killall polybar
else
  polybar mybar &
  polybar second &
fi
