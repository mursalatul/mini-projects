package main
import ("fmt")

func MainMenu() int {
	for true {

		fmt.Println("1. View All Task")
		fmt.Println("2. Add Task")
		fmt.Println("3. Delete Task")
		var selected_option int = -1
		fmt.Print("Option: ")
		fmt.Scan(&selected_option)
		if (selected_option != -1 && selected_option > 0 && selected_option < 4) {
			return selected_option	
		}
	}
	return -1
}

var tasks = [] string {}
var tasks_status = [] bool {}

func showAllTasks() {
	fmt.Println("Available Tasks are:")
	for i := 1; i <= len(tasks); i++ {
		if tasks_status[i] == true {
			fmt.Printf("%d. %s[Comp1leted]", i, key)
		} else {
			fmt.Printf("%d. %s[Not Completed]", i, key)
		}
		i++
	}
}

func addTasks() {
	
}

func main() {
	fmt.Println("A GoLang Based To Do App------")
	selected_option := MainMenu()
	fmt.Println(selected_option)
	if selected_option == 1 {
		showAllTasks()
	} else if selected_option == 2 {
		addTasks()
	} else if selected_option == 3 {
		// delete task
	}
}
