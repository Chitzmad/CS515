# Executing code in order of their priorities using dictionary
class TaskScheduler:
    def __init__(self):
        self.tasks = {}

# adding tasks in the dictionary
    def add_task(self, task, priority):
        if priority not in self.tasks:
            self.tasks[priority] = []
        # adding tasks 
        self.tasks[priority].append(task)

    def execute_tasks(self):
        # if dictionary empty then 
        if not self.tasks:
            print("No tasks to execute.")
            return
        # sort the tasks in order of priorities.
        priorities = sorted(self.tasks.keys(), reverse=True)
        for priority in priorities:
            for task in self.tasks[priority]:
                print("Executing task:", task, "with priority:", priority)
        self.tasks.clear()

# Creating instance of a class
scheduler = TaskScheduler()

# Taking input from user
num = int(input("Enter number of tasks: "))

# loop to take task number and thier priorities.
for i in range (num):
    task = input("Enter the task: ")
    priority = int(input("Enter the Priority of the task. "))

    # Function calling
    scheduler.add_task(task, priority)

# display
print("\nTasks in Execution. ")

# FUnction call to execute tasks.
scheduler.execute_tasks()

