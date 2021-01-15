load harness

@test "custom-1" {
  check '5 - -6' '11'
}

@test "custom-2" {
  check '-2 + 8 * 1 * 2 -6' '8'
}

@test "custom-3" {
  check '-5 - 5 * 2 + 8' '-7'
}

@test "custom-4" {
  check '0 * 1 + -5 * -4' '20'
}

@test "custom-5" {
  check '5 + 5 * 2 - 6 - 2' '7'
}