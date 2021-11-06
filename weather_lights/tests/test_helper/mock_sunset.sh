#!/bin/bash

RESP='{"results":{"sunrise":"5:39:10 AM","sunset":"2021-10-29T16:40:43+00:00","solar_noon":"11:43:42 AM","day_length":"12:09:04","civil_twilight_begin":"5:19:00 AM","civil_twilight_end":"6:08:24 PM","nautical_twilight_begin":"4:54:17 AM","nautical_twilight_end":"6:33:06 PM","astronomical_twilight_begin":"4:29:32 AM","astronomical_twilight_end":"6:57:51 PM"},"status":"OK"}'
echo $RESP | nc -l 4444 &