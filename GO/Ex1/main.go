package main

import "fmt"

// this is comment
func main() {
	/* this is mutli-line comment comment */
	fmt.Println("Hello, World!")
	fmt.Println("Hello, Nanu & Kitty")
	fmt.Print("Hello, Nanu & Kitty")
	fmt.Printf("\nHello, Nanu & Kitty")

	// Variable declaration
	var name string = "Nanu"
	fmt.Println(name)
	var age int = 8
	fmt.Println(age)
	var isCool bool = true
	fmt.Println(isCool)
	var weight float32 = 30.5
	fmt.Println(weight)

	// Formating in go is done using prinf
	fmt.Printf("My name is %v and I am %d years old", name, age)

}
