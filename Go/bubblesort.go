package main

import (
	"fmt"
)

func swap(a *[]int, j int) {
	(*a)[j], (*a)[j+1] = (*a)[j+1], (*a)[j]
}
func BubbleSort(a *[]int) {
	for i := 0; i < len(*a)-1; i++ {
		for j := 0; j < len(*a)-i-1; j++ {
			if (*a)[j] > (*a)[j+1] {
				swap(a, j)
			}
		}
	}
}

func main() {
	a := []int{}
	var num int
	count := 0
	for count < 10 {
		fmt.Println("Enter the ", count+1, "Element:")
		fmt.Scan(&num)
		a = append(a, num)
		count++
	}
	fmt.Println("The Unsorted array is:")
	fmt.Println(a)
	BubbleSort(&a)
	fmt.Println(a)
}
