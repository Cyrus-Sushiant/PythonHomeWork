from Task import Task
import csv

class ToDoList():
    csv_file = r"d:\Workspace\Python\HomeWork26\tasks.csv"
    tasks = []

    def __init__(self):
        self.load_tasks_from_file()

    def add_task(self, name, description, priority):
        task = Task(name, description, priority)
        self.tasks.append(task)
        self.save_to_file()

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)

        self.save_to_file()

    def show_all_tasks(self):
        return self.tasks
    
    def save_to_file(self):
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Description", "Priority"])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])

        file.close()

    def load_tasks_from_file(self):
        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            
            ingnor_header = False
            for row in reader:
                if (not ingnor_header):
                    ingnor_header = True
                    continue

                task = Task(row[0], row[1], row[2])
                self.tasks.append(task)

        file.close()