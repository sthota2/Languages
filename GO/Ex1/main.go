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
	// asinging different value to variable at fly
	var first_name, last_name = "Nanu", "Kitty"
	fmt.Printf("\nMy name is %v %v", first_name, last_name)
	var first_name1, age1 = "Nanu", 8
	fmt.Printf("\nMy name is %v and I am %d years old", first_name1, age1)

	// Short variable type
	name1 := "\nNanu"
	age2 := 8
	fmt.Print(name1, age2)

	// Zero value
	var sts string
	var i int
	fmt.Println(sts)
	fmt.Println(i)
}
