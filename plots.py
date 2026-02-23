import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Data
# -----------------------------
# it help to load the data from csv file and return the charts 

def load_data():
    try:
        df = pd.read_csv("data.csv")
        print("✅ Data loaded successfully\n")
        print(df)
        return df
    except FileNotFoundError:
        print("❌ data.csv not found!")
        exit()

# -----------------------------
# Bar Chart
# -----------------------------
def bar_chart(df):
    df.plot(x='Student', kind='bar')
    plt.title("Student Marks Comparison")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

# -----------------------------
# Line Chart
# -----------------------------
def line_chart(df):
    plt.figure()

    subjects = ['Maths', 'Science', 'English']
    for subject in subjects:
        plt.plot(df['Student'], df[subject], marker='o', label=subject)

    plt.title("Marks Trend by Subject")
    plt.xlabel("Students")
    plt.ylabel("Marks")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# -----------------------------
# Pie Chart
# -----------------------------
def pie_chart(df):
    avg_marks = df[['Maths', 'Science', 'English']].mean()

    plt.figure()
    plt.pie(avg_marks, labels=avg_marks.index, autopct='%1.1f%%')
    plt.title("Average Marks Distribution")
    plt.tight_layout()
    plt.show()

# -----------------------------
# Main Menu
# -----------------------------
def main():
    df = load_data()

    while True:
        print("\n📊 Choose Visualization:")
        print("1. Bar Chart")
        print("2. Line Chart")
        print("3. Pie Chart")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            bar_chart(df)
        elif choice == '2':
            line_chart(df)
        elif choice == '3':
            pie_chart(df)
        elif choice == '4':
            print("👋 Exiting program...")
            break
        else:
            print("⚠️ Invalid choice. Try again.")
            


# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    main()