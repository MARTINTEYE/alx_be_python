# prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it task time-bound? (yes/no): ").lower()

#Process the task using match case for priority
match priority:
    case "high":
         reminder = f"🔴 HIGH priority task: {task}"
    case "medium":
         reminder = f"🟠 Medium priority task: {task}"
    case "low":
         reminder = f"🟢 Low priority task: {task}"
    case _:
        reminder = f"⚪ Task: {task} (Unknown priority)"
# check if the taskk is time-bound
if time_bound == "yes":
     reminder += " - that requires immediate attention today!"
print(reminder)
