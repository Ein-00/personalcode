package main


import (
    "fmt"
)

type Animal struct{
    food string
    move string
    noise string

}

func (a Animal)EAT(){
    fmt.Println(a.food)
}
func (a Animal) MOVE(){
    fmt.Println(a.move)
}
func (a Animal) NOISE(){
    fmt.Println(a.noise)
}

func main(){
    animal := map[string] Animal{
        "cow" : {"grass","walk","moo"},
        "bird" : {"worms","fly","peep"},
        "snake" : {"mice","slither","hiss"},
    }
    
    var aniname,info string
    fmt.Println("Enter the name of the animal:")
    fmt.Scan(&aniname)
    fmt.Println("Enter the information:")
    fmt.Scan(&info)
    animals , _ := animal[aniname]
    switch info{
    case "eat":
        animals.EAT()
    case "move":
        animals.MOVE()
    case "noise":
        animals.NOISE()

    }

}
