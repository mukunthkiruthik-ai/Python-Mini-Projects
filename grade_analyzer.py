"""
📊 Student Grade Analyzer
Analyze and get statistics on student grades
Author: Mukunth Kiruthik R S | B.Tech AI&DS, KPRIET
"""

def get_grade(marks):
    """Convert marks to grade"""
    if marks >= 90: return "O"
    elif marks >= 80: return "A+"
    elif marks >= 70: return "A"
    elif marks >= 60: return "B+"
    elif marks >= 50: return "B"
    else: return "RA"

def calculate_gpa(marks):
    """Convert marks to GPA (10-point scale)"""
    grade_points = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "RA": 0}
    grade = get_grade(marks)
    return grade_points[grade]

def analyze_grades(students):
    """Perform statistical analysis on grades"""
    all_marks = [marks for _, marks in students]
    
    avg = sum(all_marks) / len(all_marks)
    highest = max(all_marks)
    lowest = min(all_marks)
    sorted_marks = sorted(all_marks)
    n = len(sorted_marks)
    median = (sorted_marks[n//2] + sorted_marks[(n-1)//2]) / 2
    
    # Grade distribution
    grade_count = {"O": 0, "A+": 0, "A": 0, "B+": 0, "B": 0, "RA": 0}
    for _, marks in students:
        grade_count[get_grade(marks)] += 1
    
    return {
        "average": avg,
        "highest": highest,
        "lowest": lowest,
        "median": median,
        "total_students": len(students),
        "pass_count": sum(1 for _, m in students if m >= 50),
        "grade_distribution": grade_count
    }

def display_results(students, stats):
    """Display formatted results"""
    print("\n" + "=" * 65)
    print("📊 STUDENT GRADE ANALYSIS REPORT")
    print("=" * 65)
    
    # Individual results
    print(f"\n{'Name':<20} {'Marks':>6} {'Grade':>6} {'GPA':>5}")
    print("-" * 40)
    for name, marks in sorted(students, key=lambda x: x[1], reverse=True):
        grade = get_grade(marks)
        gpa = calculate_gpa(marks)
        emoji = "🏆" if marks == stats["highest"] else "  "
        print(f"{emoji}{name:<18} {marks:>6} {grade:>6} {gpa:>5}")
    
    # Statistics
    print(f"\n{'=' * 40}")
    print("📈 CLASS STATISTICS")
    print(f"{'=' * 40}")
    print(f"  Total Students : {stats['total_students']}")
    print(f"  Average Marks  : {stats['average']:.1f}")
    print(f"  Highest Marks  : {stats['highest']}")
    print(f"  Lowest Marks   : {stats['lowest']}")
    print(f"  Median Marks   : {stats['median']:.1f}")
    print(f"  Pass Rate      : {stats['pass_count']}/{stats['total_students']} "
          f"({stats['pass_count']/stats['total_students']*100:.1f}%)")
    
    # Grade distribution bar chart
    print(f"\n📊 Grade Distribution:")
    for grade, count in stats["grade_distribution"].items():
        bar = "█" * (count * 3)
        if count > 0:
            print(f"  {grade:>3}: {bar} ({count})")

def main():
    # Sample student data
    students = [
        ("Mukunth", 85),
        ("Varun", 78),
        ("Priya", 92),
        ("Karthik", 65),
        ("Sneha", 88),
        ("Ravi", 45),
        ("Divya", 73),
        ("Arjun", 91),
        ("Meena", 56),
        ("Surya", 82),
    ]
    
    stats = analyze_grades(students)
    display_results(students, stats)

if __name__ == "__main__":
    main()
