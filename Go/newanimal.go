
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type Animal interface {
	Eat()
	Move()
	Speak()
}

type Cow struct{}

func (c Cow) Eat() {
	fmt.Println("grass")
}

func (c Cow) Move() {
	fmt.Println("walk")
}

func (c Cow) Speak() {
	fmt.Println("moo")
}

type Bird struct{}

func (b Bird) Eat() {
	fmt.Println("worms")
}

func (b Bird) Move() {
	fmt.Println("fly")
}

func (b Bird) Speak() {
	fmt.Println("peep")
}

type Snake struct{}

func (s Snake) Eat() {
	fmt.Println("mice")
}

func (s Snake) Move() {
	fmt.Println("slither")
}

func (s Snake) Speak() {
	fmt.Println("hsss")
}

func main() {
	animals := make(map[string]Animal)
	scanner := bufio.NewScanner(os.Stdin)

	for {
		fmt.Print("> ")

		if scanner.Scan() {
			input := strings.Fields(scanner.Text())

			if len(input) < 3 {
				fmt.Println("Invalid input format. Please enter a valid command.")
				continue
			}

			command, name, info := input[0], input[1], input[2]

			switch command {
			case "newanimal":
				switch info {
				case "cow":
					animals[name] = Cow{}
				case "bird":
					animals[name] = Bird{}
				case "snake":
					animals[name] = Snake{}
				default:
					fmt.Println("Unknown animal type. Please use 'cow', 'bird', or 'snake'.")
					continue
				}
				fmt.Println("Created it!")
			case "query":
				animal, exists := animals[name]
				if !exists {
					fmt.Println("Animal not found.")
					continue
				}

				switch info {
				case "eat":
					animal.Eat()
				case "move":
					animal.Move()
				case "speak":
					animal.Speak()
				default:
					fmt.Println("Unknown information request. Please use 'eat', 'move', or 'speak'.")
				}
			default:
				fmt.Println("Unknown command. Please use 'newanimal' or 'query'.")
			}
		} else {
			fmt.Println("Error reading input.")
			break
		}
	}
}
