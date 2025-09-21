import datetime

# A list to store all todos
todo_list = []

# Function to add a todo
def add_todo():
    title = input("Enter To-Do Title: ")
    date_str = input("Enter Due Date (YYYY-MM-DD): ")
    
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        todo = {"title": title, "date": date}
        todo_list.append(todo)
        print("✅ To-Do added successfully.\n")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.\n")

# Function to view all todos
def view_todos():
    if not todo_list:
        print("📭 No To-Dos found.\n")
    else:
        print("\n📋 To-Do List:")
        for idx, todo in enumerate(todo_list, 1):
            print(f"{idx}. {todo['title']} (Due: {todo['date']})")
        print()

# Function to delete a specific todo
def delete_todo():
    view_todos()
    if not todo_list:
        return
    
    try:
        index = int(input("Enter the number of the To-Do to delete: "))
        if 1 <= index <= len(todo_list):
            removed = todo_list.pop(index - 1)
            print(f"🗑️ Deleted To-Do: {removed['title']}\n")
        else:
            print("❌ Invalid number.\n")
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Function to delete all todos
def delete_all_todos():
    confirm = input("Are you sure you want to delete all To-Dos? (yes/no): ").strip().lower()
    if confirm == "yes":
        todo_list.clear()
        print("🧹 All To-Dos have been deleted.\n")
    else:
        print("❌ Operation cancelled.\n")

# Main menu loop
def main():
    while True:
        print("===== TO-DO APPLICATION =====")
        print("1. Add To-Do")
        print("2. View To-Dos")
        print("3. Delete a To-Do")
        print("4. Delete All To-Dos")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_todo()
        elif choice == '2':
            view_todos()
        elif choice == '3':
            delete_todo()
        elif choice == '4':
            delete_all_todos()
        elif choice == '5':
            print("👋 Exiting application. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select between 1-5.\n")

if __name__ == "__main__":
    main()
