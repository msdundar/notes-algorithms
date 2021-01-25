package main

import (
  "fmt"
  "math/rand"
  "time"
)

func main() {
  var (
    min        = 0
    max        = 100
    tries      = 0
    seed       = rand.New(rand.NewSource(time.Now().UnixNano()))
    randNumber = seed.Intn(max)
  )

  for min <= max {
    guess := (min + max) / 2

    if guess == randNumber {
      fmt.Printf("The number have been found in %v tries and it was %v\n", tries, randNumber)
      break
    } else if guess > randNumber {
      tries++
      max = guess - 1
    } else if guess < randNumber {
      tries++
      min = guess + 1
    }
  }
}
