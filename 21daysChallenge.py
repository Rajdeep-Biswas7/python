import json
import os
from datetime import datetime, timedelta

class HabitTracker:
    def __init__(self, filename='habits.json'):
        self.filename = filename
        self.habits = self.load_habits()
    
    def load_habits(self):
        """Load habits from file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return {}
    
    def save_habits(self):
        """Save habits to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.habits, f, indent=2)
    
    def add_habit(self, habit_name):
        """Add a new habit to track"""
        if habit_name in self.habits:
            print(f"❌ Habit '{habit_name}' already exists!")
            return
        
        self.habits[habit_name] = {
            'created_date': datetime.now().strftime('%Y-%m-%d'),
            'completed_days': []
        }
        self.save_habits()
        print(f"✅ Habit '{habit_name}' added successfully!")
    
    def check_habit(self, habit_name):
        """Mark a habit as completed for today"""
        if habit_name not in self.habits:
            print(f"❌ Habit '{habit_name}' not found!")
            return
        
        today = datetime.now().strftime('%Y-%m-%d')
        
        if today in self.habits[habit_name]['completed_days']:
            print(f"✅ '{habit_name}' already checked for today!")
            return
        
        self.habits[habit_name]['completed_days'].append(today)
        self.save_habits()
        print(f"✅ '{habit_name}' marked as completed for today!")
    
    def view_progress(self, habit_name):
        """View progress for a specific habit"""
        if habit_name not in self.habits:
            print(f"❌ Habit '{habit_name}' not found!")
            return
        
        habit = self.habits[habit_name]
        streak = self.calculate_streak(habit_name)
        completion_rate = (len(habit['completed_days']) / 21) * 100
        
        print(f"\n📊 Habit: {habit_name}")
        print(f"Created: {habit['created_date']}")
        print(f"Days Completed: {len(habit['completed_days'])}/21")
        print(f"Current Streak: {streak} days")
        print(f"Completion Rate: {completion_rate:.1f}%")
        print(f"Progress: {'█' * (len(habit['completed_days']) // 2)}{' ' * ((21 - len(habit['completed_days'])) // 2)}\n")
    
    def calculate_streak(self, habit_name):
        """Calculate current streak for a habit"""
        completed_days = sorted(self.habits[habit_name]['completed_days'])
        if not completed_days:
            return 0
        
        streak = 1
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Check if today is completed, if not start from yesterday
        if completed_days[-1] != today:
            completed_days_dt = [datetime.strptime(d, '%Y-%m-%d') for d in completed_days]
            if (datetime.now() - completed_days_dt[-1]).days > 1:
                return 0
        
        for i in range(len(completed_days) - 1, 0, -1):
            current = datetime.strptime(completed_days[i], '%Y-%m-%d')
            previous = datetime.strptime(completed_days[i-1], '%Y-%m-%d')
            
            if (current - previous).days == 1:
                streak += 1
            else:
                break
        
        return streak
    
    def view_all_habits(self):
        """Display all habits and their status"""
        if not self.habits:
            print("📭 No habits yet! Add one to get started.\n")
            return
        
        print("\n" + "="*50)
        print("🎯 YOUR 21-DAY CHALLENGE HABITS")
        print("="*50)
        
        for habit in self.habits:
            completed = len(self.habits[habit]['completed_days'])
            streak = self.calculate_streak(habit)
            status = "🎉" if completed >= 21 else "🔥" if streak >= 7 else "⏳"
            print(f"\n{status} {habit}")
            print(f"   Days: {completed}/21 | Streak: {streak} days")
        
        print("\n" + "="*50 + "\n")
    
    def delete_habit(self, habit_name):
        """Delete a habit from tracking"""
        if habit_name not in self.habits:
            print(f"❌ Habit '{habit_name}' not found!")
            return
        
        del self.habits[habit_name]
        self.save_habits()
        print(f"✅ Habit '{habit_name}' deleted!")

def main():
    tracker = HabitTracker()
    
    while True:
        print("\n" + "="*50)
        print("🎯 21 DAYS HABIT CHALLENGE TRACKER")
        print("="*50)
        print("1. Add a new habit")
        print("2. Check a habit (mark as completed today)")
        print("3. View all habits")
        print("4. View habit progress")
        print("5. Delete a habit")
        print("6. Exit")
        print("="*50)
        
        choice = input("\nChoose an option (1-6): ").strip()
        
        if choice == '1':
            habit = input("Enter habit name: ").strip()
            if habit:
                tracker.add_habit(habit)
            else:
                print("❌ Please enter a habit name!")
        
        elif choice == '2':
            habit = input("Enter habit name to check: ").strip()
            if habit:
                tracker.check_habit(habit)
            else:
                print("❌ Please enter a habit name!")
        
        elif choice == '3':
            tracker.view_all_habits()
        
        elif choice == '4':
            habit = input("Enter habit name to view progress: ").strip()
            if habit:
                tracker.view_progress(habit)
            else:
                print("❌ Please enter a habit name!")
        
        elif choice == '5':
            habit = input("Enter habit name to delete: ").strip()
            if habit:
                tracker.delete_habit(habit)
            else:
                print("❌ Please enter a habit name!")
        
        elif choice == '6':
            print("\n🎉 Keep building those habits! See you next time!\n")
            break
        
        else:
            print("❌ Invalid option! Please choose 1-6.")

if __name__ == "__main__":
    main()