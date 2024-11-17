package main

import (
    "fmt"
    "strings"
    "io/ioutil"
)

type Person struct{
    fname string
    lname string
}

func main(){
    fmt.Println("Enter the name of the file:")
    var filename string
    fmt .Scan(&filename)

    file , _ := ioutil.ReadFile(filename)
    var name []Person

    lines := strings.Split(string(file), "\n") 
    for _,line := range lines{
        line  =strings.TrimSpace(line)
        parts := strings.Fields(line)
        
        if len(parts) >= 2{
            n := Person{
                fname : parts[0],
                lname : parts[1],
            }
            name = append(name,n)
        }
    }
    fmt.Println(name)
}
