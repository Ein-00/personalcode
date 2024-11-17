package main


import(
    "fmt"
    "encoding/json"
)


func main(){
    det := make(map[string]string) 
    var name,address string
    fmt.Println("Enter your name:\n")
    fmt.Scan(&name)
    fmt.Println("Enter your address:\n")

    fmt.Scan(&address)
    //fmt.Println(a,b)
    fmt.Println(name , address)
    det["name"] = name
    det["address"] = address

    jsdet,_ := json.Marshal(det)

    fmt.Println("Byte array of json:",jsdet)
    fmt.Println("String of json :",string(jsdet))
}
