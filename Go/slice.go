package main


import(
    "fmt"
    "sort"
    "strconv"
)

func main(){
    s := make([]int,0,3)
    var input string
    for{
        fmt.Println("Enter an integer. 'X' to quit ")
        fmt.Scan(&input) 
        if input == "X"||input =="x"{
            fmt.Println("Exiting")
            break
        }
        num,err := strconv.Atoi(input)
        
        if err!= nil{
            fmt.Println(err)
        }

        s = append(s,num)


        sort.Ints(s)
        fmt.Println("Slice : ",s)
    }



}
