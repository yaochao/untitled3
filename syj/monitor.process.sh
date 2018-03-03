#!/bin/sh

ps -ef | grep "gyj_spider" | grep -v "grep" | grep -v "tail"

if [ "$?" -eq 1 ]

then

./ZeroNet.sh

echo "process has been restarted!"

else

echo "process already started!"

fi

sleep 10