package main

import "fmt"

func solve(results []int) (int, int) {
	bestBalance := 0
	bestStart := 0
	bestEnd := 0

	n := len(results)
	for start := 0; start < n; start++ {
		balance := 0
		for end := start; end < n; end++ {
			balance += results[end]
			if balance > bestBalance || (balance == bestBalance && end-start > bestEnd-bestStart) {
				bestBalance = balance
				bestStart = start + 1
				bestEnd = end + 1
			}
		}
	}
	if bestBalance > 0 {
		return bestStart, bestEnd
	}
	return 0, 0
}

func main() {
	matchs := make([][]int, 0)
	for {
		var x int
		fmt.Scanln(&x)
		if x == 0 {
			break
		}

		curr := make([]int, x)
		for i := 0; i < x; i++ {
			var n, m int
			fmt.Scanln(&n, &m)
			curr[i] = n - m
		}
		matchs = append(matchs, curr)
	}

	for i, v := range matchs {
		start, end := solve(v)
		fmt.Printf("Teste %d\n", i+1)
		if start == 0 || end == 0 {
			fmt.Println("nenhum")
			fmt.Println("")
		} else {
			fmt.Printf("%d %d\n", start, end)
			fmt.Println("")
		}
	}
}
