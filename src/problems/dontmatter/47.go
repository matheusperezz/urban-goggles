package main

import (
	"fmt"
	"math"
)

func main() {
	var n, maxIndex int
	var maxVal float64 = -1
	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		var d, c int
		fmt.Scan(&d, &c)
		val := math.Pow(float64(d), float64(c))
		if val > maxVal {
			maxVal = val
			maxIndex = i
		}
	}

	fmt.Println(maxIndex)
}
