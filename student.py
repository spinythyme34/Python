student_scores = {}

def add_student(name, score):
    if name in student_scores:
        print(f"{name} is already in the list. Use the update function to change the score.")
    else:
        student_scores[name] = score
        print(f"Added {name} with score {score}.")

def update_score(name, new_score):
    if name in student_scores:
        student_scores[name] = new_score
        print(f"Updated {name}'s score to {new_score}.")
    else:
        print(f"{name} not found. Use the add function to add the student.")

def delete_student(name):
    if name in student_scores:
        del student_scores[name]
        print(f"Deleted {name} from the list.")
    else:
        print(f"{name} not found.")

def highest_score():
    if student_scores:
        top_student = max(student_scores, key=student_scores.get)
        print(f"The student with the highest score is {top_student} with a score of {student_scores[top_student]}.")
    else:
        print("No students found.")

add_student("Alice", 85)
add_student("Bob", 90)
add_student("Charlie", 78)

update_score("Alice", 95)

delete_student("Charlie")

highest_score()

print("\nFinal list of students and scores:")
print(student_scores)
