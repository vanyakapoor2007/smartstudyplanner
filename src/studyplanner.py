import datetime

# -------------------------------
# Module 1: User & Task Management
# -------------------------------

class Task:
    def __init__(self, title, category, deadline, priority, duration):
        self.title = title
        self.category = category
        self.deadline = deadline
        self.priority = priority
        self.duration = duration
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅ Completed" if self.completed else "⏳ Pending"
        return f"{self.title} | {self.category} | Deadline: {self.deadline.date()} | Priority: {self.priority} | {status}"


class StudyPlanner:
    def __init__(self):
        self.tasks = []
        self.streak = 0
        self.last_completed_date = None

    def add_task(self, title, category, deadline, priority, duration):
        task = Task(title, category, deadline, priority, duration)
        self.tasks.append(task)

    def update_task(self, index, **kwargs):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            for key, value in kwargs.items():
                setattr(task, key, value)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def show_tasks(self):
        print("\n📋 Task List:")
        if not self.tasks:
            print("No tasks yet.")
        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    # -------------------------------
    # Module 2: Study Planner & Scheduler
    # -------------------------------

    def suggest_time_slots(self):
        print("\n📅 Suggested Time Slots:")
        morning = [t for t in self.tasks if t.priority == "High" and not t.completed]
        evening = [t for t in self.tasks if t.priority != "High" and not t.completed]

        print("🌞 Morning (High Focus):")
        for task in morning:
            print(f" - {task.title} ({task.duration} mins)")

        print("🌙 Evening (Light Work):")
        for task in evening:
            print(f" - {task.title} ({task.duration} mins)")

    def daily_checklist(self):
        print("\n✅ Daily Checklist:")
        for task in self.tasks:
            status = "Done" if task.completed else "Pending"
            print(f"- {task.title}: {status}")

    def weekly_checklist(self):
        print("\n📌 Weekly Checklist:")
        week_deadline = datetime.datetime.now() + datetime.timedelta(days=7)
        for task in self.tasks:
            if task.deadline <= week_deadline:
                status = "Done" if task.completed else "Pending"
                print(f"- {task.title}: {status}")

    # -------------------------------
    # Module 3: Productivity Analytics
    # -------------------------------

    def productivity_score(self):
        completed = sum(1 for t in self.tasks if t.completed)
        total = len(self.tasks)
        score = (completed / total * 100) if total > 0 else 0
        print(f"\n📊 Daily Productivity Score: {score:.2f}%")
        return score

    def streak_tracking(self):
        today = datetime.date.today()
        if any(t.completed for t in self.tasks):
            if self.last_completed_date == today - datetime.timedelta(days=1):
                self.streak += 1
            elif self.last_completed_date != today:
                self.streak = 1
            self.last_completed_date = today
        print(f"🔥 Current Streak: {self.streak} days")

    def show_text_graphs(self):
        completed = sum(1 for t in self.tasks if t.completed)
        pending = len(self.tasks) - completed

        print("\n📊 Weekly Task Completion (Text Graph)")
        print("Completed: " + "█" * completed)
        print("Pending  : " + "█" * pending)

    def suggestions(self):
        score = self.productivity_score()
        if score < 50:
            print("💡 Suggestion: Break tasks into smaller chunks and focus on high-priority ones first.")
        else:
            print("🎉 Great job! Keep maintaining your streak and consistency.")


# -------------------------------
# Interactive Menu
# -------------------------------

def main():
    planner = StudyPlanner()

    while True:
        print("\n===== SMART STUDY PLANNER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Suggest Time Slots")
        print("6. Daily Checklist")
        print("7. Weekly Checklist")
        print("8. Productivity Analytics")
        print("9. Exit")

        choice = input("Choose an option (1-9): ")

        if choice == "1":
            title = input("Enter task title: ")
            category = input("Enter category (Study/Assignment/Revision/Exam Preparation): ")
            deadline_str = input("Enter deadline (YYYY-MM-DD): ")
            deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d")
            priority = input("Enter priority (High/Medium/Low): ")
            duration = int(input("Enter duration (minutes): "))
            planner.add_task(title, category, deadline, priority, duration)
            print("✅ Task added successfully!")

        elif choice == "2":
            planner.show_tasks()

        elif choice == "3":
            planner.show_tasks()
            index = int(input("Enter task number to mark completed: "))
            if 0 <= index < len(planner.tasks):
                planner.tasks[index].mark_completed()
                print("✅ Task marked as completed!")

        elif choice == "4":
            planner.show_tasks()
            index = int(input("Enter task number to delete: "))
            planner.delete_task(index)
            print("🗑️ Task deleted!")

        elif choice == "5":
            planner.suggest_time_slots()

        elif choice == "6":
            planner.daily_checklist()

        elif choice == "7":
            planner.weekly_checklist()

        elif choice == "8":
            planner.productivity_score()
            planner.streak_tracking()
            planner.show_text_graphs()
            planner.suggestions()

        elif choice == "9":
            print("👋 Exiting Smart Study Planner. Stay productive!")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()