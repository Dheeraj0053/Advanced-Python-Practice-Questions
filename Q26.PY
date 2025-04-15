class Score:
    def __init__(self, subject, marks):
        self.subject = subject
        self.marks = marks

class Student:
    def __init__(self, name, subjects, marks):
        self.name = name
        self.scores = [Score(subj, mark) for subj, mark in zip(subjects, marks)]
    
    def __str__(self):
        return f"Student {self.name} has the following scores:\n" + "\n".join(f"{s.subject}: {s.marks}" for s in self.scores)
    
    def average(self):
        return sum(s.marks for s in self.scores) / len(self.scores)

def classAverage(students):
    from collections import defaultdict
    subject_marks = defaultdict(list)
    for student in students:
        for score in student.scores:
            subject_marks[score.subject].append(score.marks)
    return [f"{subj}:{round(sum(marks)/len(marks))}" for subj, marks in subject_marks.items()]

s1 = Student('X', ['C1', 'C2', 'C3', 'C4'], [10, 20, 30, 80])
s2 = Student('Y', ['C1', 'C2'], [40, 50])
s3 = Student('Z', ['C2', 'C3'], [60, 70])

print(s1)
print(s1.average())
print(classAverage([s1, s2, s3]))