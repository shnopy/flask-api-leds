#!/usr/local/bin/env bats 

setup() {
  load 'test_helper/common-setup'
  _common_setup

  ./onoff

}


teardown() {
  if [ -f TESTMODE* ]; then
    rm TESTMODE*
  fi
}


@test "weather_lights: sunset and after 3 o clock - turn on lights" {
  mock_sunset.sh >/dev/null 2>&1
  touch TESTMODE2

  run weather-lights.sh
  assert_line --index 0 --partial 'hour is 16 sunset is 1 - going in...'
  run status
  [ "$status" -eq 1 ]
}


@test "weather_lights: not yet sunset and after 3 o clock - do nothing" {
  mock_sunset.sh >/dev/null 2>&1
  touch TESTMODE1

  run weather-lights.sh
  assert_output ''
  run status
  [ "$status" -eq 0 ]
}

@test "weather_lights: sunset and early morning past post midnight lights already on - turn off lights" {
  ./onoff on
  mock_sunset.sh >/dev/null 2>&1
  touch TESTMODE3

  run weather-lights.sh
  assert_output 'LEDs off'
  run status
  [ "$status" -eq 0 ]
}

@test "weather_lights: sunset and early morning past post midnight lights already off - do nothing" {
  mock_sunset.sh >/dev/null 2>&1
  touch TESTMODE3

  run weather-lights.sh
  assert_output ''
  run status
  [ "$status" -eq 0 ]
}


@test "weather_lights: on when already on" {
  ./onoff on
  mock_sunset.sh >/dev/null 2>&1
  touch TESTMODE2

  run weather-lights.sh
  assert_line --index 0 --partial 'hour is 16 sunset is 1 - going in...'
  run status
  [ "$status" -eq 1 ]
}


# @test "weather_lights: very hot" {
#   skip
# }

# @test "weather_lights: hot" {
#   skip
# }

# @test "weather_lights: normal" {
#   skip
# }

# @test "weather_lights: cold" {
#   skip
# }

# @test "weather_lights: very cold" {
#   skip
# }

# @test "weather_lights: unknown temperature" {
#   skip
# }


@test "weather_lights: handling of sunset returns -1 error" {
  touch TESTMODE2   # put into test mode but do not start mock_sunset

  run weather-lights.sh
  assert_output 'sunset error - skipping'
}

## TODO - any other script error conditions?