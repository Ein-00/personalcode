package main


import (
    "fmt"
    "sync"
)

var count int
var wg sync.WaitGroup
var mut sync.Mutex
func increment(){
	mut.Lock()
    defer wg.Done()
    for i :=0 ;i <  1000;i++ {

        value := count
        value ++
        count = value
    }
	mut.Unlock()
    
}
func main(){
    wg.Add(2)
    go increment()
    go increment()
    wg.Wait()
    fmt.Println("Final counter value : ",count)
}
/*


*/
