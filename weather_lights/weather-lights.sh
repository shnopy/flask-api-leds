#!/bin/bash

. config


TEMP=`curl -s ${HOSTS[temp]}/sensor/$SENSOR |jq .value`
LEDSTATUS=`./status`

echo $TEMP
echo $LEDSTATUS

if [ $LEDSTATUS -eq 0 ]
then
    echo "turning LEDs on"
#     resp=`curl -s -X POST ${HOSTS[leds]}/on/ | jq .response | tr -d '"'`
#     echo $resp
#     if [ $resp = 'LEDs on' ]
#     then
#         echo "?error - cannot turn LEDs on"
#         exit;
#     fi
fi
