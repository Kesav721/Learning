#Q Print only subjects where marks > 85

marks = {"Math": 90, "Science": 85, "English": 88}
for subject, score in marks.items():
    if score > 85:
        print(subject)
