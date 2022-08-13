import csv
from datetime import datetime, timedelta

def get_students_exam_data() -> dict:
    students = {}
    with open('start_times.csv') as start_file:
        for line in csv.reader(start_file, delimiter=';'):
            student = line[0]
            start_time = datetime.strptime(line[1], '%H:%M')
            students[student] = {
                'start_time' : start_time,
                #'start_time' : line[1],
                'stats' : {
                    'tasks' : [],
                    'points' : [],
                    'submission_times' : []
                }
            }

    with open('submissions.csv') as sub_file:
        for line in csv.reader(sub_file, delimiter=";"):
            student = line[0]
            task = int(line[1])
            point = int(line[2])
            sub_time = datetime.strptime(line[3], '%H:%M')
            students[student]['stats']['tasks'].append(task)
            students[student]['stats']['points'].append(point)
            students[student]['stats']['submission_times'].append(sub_time)
            #students[student]['stats']['submission_times'].append(line[3])

    return students

def cheaters():
    data = get_students_exam_data()
    cheaters = []
    for student, info in data.items():
        start_time = info['start_time']
        submission_times = info['stats']['submission_times']
        for time in submission_times:
            if time > (start_time + timedelta(hours=3)):
                cheaters.append(student)
                break
    return cheaters