import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Daily Planner")

# Define the activities
activities = {
    "sleep": 8,
    "video games": 2,
    "workout": 1,
    "learning programming": 3
}

# Create variables to store the state of the checkboxes
checkbox_variables = {}
for activity in activities:
    checkbox_variables[activity] = tk.BooleanVar(value=True)

# Create a function to calculate the total time
def calculate_total():
    # Initialize the total time to 0
    total_time = 0

    # Loop through the activities
    for activity, time in activities.items():
        # Check if the checkbox for this activity is checked
        if checkbox_variables[activity].get():
            # If it is checked, add the time to the total
            total_time += time

    # Set the total time in the label
    total_label.config(text="Total: {} hours".format(total_time))

# Create a label for the total time
total_label = tk.Label(root, text="Total: 0 hours")
total_label.grid(row=len(activities), column=0, columnspan=2)

# Loop through the activities
for index, activity in enumerate(activities):
    # Create a checkbox for the activity
    checkbox = tk.Checkbutton(root, text=activity, variable=checkbox_variables[activity], command=calculate_total)
    checkbox.grid(row=index, column=0)

    # Create a label for the time
    time_label = tk.Label(root, text="{} hours".format(activities[activity]))
    time_label.grid(row=index, column=1)

# Run the main loop
root.mainloop()
