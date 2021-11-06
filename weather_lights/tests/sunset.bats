#!/usr/local/bin/env bats 

setup() {
  load 'test_helper/common-setup'
  _common_setup
}


teardown() {
  if [ -f TESTMODE* ]; then
    rm TESTMODE*
  fi
}


@test "sunset: sun not set" {
  mock_sunset.sh >/dev/null 2>&1
  touch TESTMODE1
  run sunset
  [ "$output" -eq 0 ]
  [ "$status" -eq 0 ]
}

@test "sunset: sunset has passed" {
  mock_sunset.sh >/dev/null 2>&1
  touch TESTMODE2
  run sunset
  [ "$output" -eq 1 ]
  [ "$status" -eq 1 ]
}

@test "sunset: sunset has passed - with offset" {
  mock_sunset.sh >/dev/null 2>&1
  touch TESTMODE1
  run sunset -1
  [ "$output" -eq 1 ]
  [ "$status" -eq 1 ]
}

@test "sunset: sun not set - with offset" {
  mock_sunset.sh >/dev/null 2>&1
  touch TESTMODE1
  run sunset 1
  [ "$output" -eq 0 ]
  [ "$status" -eq 0 ]
}

@test "sunset: invalid response from api" {
   touch TESTMODE1
   run sunset 
  [ "$output" -eq -1 ]
}
