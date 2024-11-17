package main

import (
	"fmt"
	"sync"

	"sort"
)
var wg sync.WaitGroup
func sorting(arr []int){
	defer wg.Done()
	sort.Ints(arr)
}

func mergetwo(a , b []int)[]int {
	merged := make([]int , (len(a)+len(b)))
	i,j,k := 0,0,0
	for i< len(a) && j <len(b){
		if a[i] < b[j]{
			merged[k] = a[i]
			i++
		}else{
			merged[k] = b[j]
			j++
		}
		k++
	}
	if i <len(a){
		merged[k] = a[i]
		i++
		k++
	}
	if j < len(b){
		merged[k] = b[j]
		j++
		k++
	}
	return merged
}
func mergesort(arr ...[]int) []int{
	merged := arr[0]
	for _ , array := range arr[1:]{
		merged = mergetwo(merged , array)
	}
	return merged
}
func main(){
	fmt.Println("Enter the size of the array:")
	var size int
	fmt.Scan(&size)
	arr := make([]int , size)
	for i:= 0 ; i <size ; i++{
		fmt.Println("Enter a number:")
		fmt.Scan(&arr[i])	
	}
	fmt.Println(arr)
	s := size / 4
	wg.Add(4)
	parts := make([][]int , 4)
	for i := 0 ; i < 4 ;i++{
		start := i * s 
		end := start + 4
		if i == 3 {
			end = size
		}
		parts[i] = make([]int , end- start)
		copy(parts[i],arr[start:end] )
		go sorting(parts[i]) 
	}
	wg.Wait()
	sortedArray := mergesort(parts...)
	fmt.Println(sortedArray)
	

}
