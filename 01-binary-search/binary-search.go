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
			fmt.Printf("Congrats! You found the correct number in %v tries\n", tries)
			break
		} else if guess > randNumber {
			tries++
			max = guess - 1
			fmt.Printf("Choose a smaller number than %v. The number must be between %v and %v\n", guess, min, max)
		} else if guess < randNumber {
			tries++
			min = guess + 1
			fmt.Printf("Choose a bigger number than %v. The number must be between %v and %v\n", guess, min, max)
		}
	}
}
