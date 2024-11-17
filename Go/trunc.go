package main

import (
	"fmt"
)


func main(){
	var x float64

  _,err  :=	fmt.Scanf("%f",&x)
	fmt.Println(err)
  fmt.Println(x)
	y := int(x)
	fmt.Printf("%d",y)
	
}
