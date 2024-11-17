package main

import (
    "fmt"
)
func GenDisplaceFn( a,v,s float64) func(t float64) float64{
    return func(t float64) float64{
        return 0.5*a*t*t + v*t + s 
    }
}



func main(){

    var a,v,s,t float64
    fmt.Println("Enter the acceleration:")
    fmt.Scan(&a)

    fmt.Println("Enter the initial velocity:")
    fmt.Scan(&v)

    fmt.Println("Enter the initial displacement:")
    fmt.Scan(&s)



    fmt.Println("Enter the time:")
    fmt.Scan(&t)
    fn:= GenDisplaceFn(a,v,s)
    displ := fn(t)
    fmt.Println("The displacement ",displ,"")
    


}
