package main


import (
	"fmt"
	"strings"
)

func main(){
	var str string
	fmt.Println("Enter a string:")
	_,err := fmt.Scanf("%s",&str)


	fmt.Println(err)

	str = strings.ToLower(str)
	fmt.Println(str)
	var acheck,icheck,ncheck bool
	if str[:1] == "i"{
		icheck = true
    }else {
		icheck = false}
	if str[len(str) -1] == 'n'{
		ncheck = true
	}else {
		ncheck = false
	}	
	if strings.ContainsAny(str,"a"){
		acheck = true
	}else{
		acheck = false
	}

	if acheck==icheck==ncheck==true{
		fmt.Println("Found!")
		}else{
		fmt.Println("Not Found!")}
		
}
