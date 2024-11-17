package main


import (
    "fmt"
    "os"
)

func main(){
    f,_ := os.Create("output.txt")
    barr := []byte{1,2,3}

    nb , _ := f.Write(barr)
    fmt.Println(nb)
    nb1, _ := f.WriteString("HI")
    fmt.Println(nb1)
}
