def exam_and_exercise_completed(inpt):
    space = inpt.find(" ")
    exam = int(inpt[:space])
    exercise = int(inpt[space+1:])
    return [exam, exercise]
 
def exercise_points(amount):
    return amount // 10
 
def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i
 
def mean(points):
    return sum(points) / len(points)
 
def main():
    points = []
    grades = [0] * 6
    while True:
        inpt = input("Exam points and exercises completed: ")
        if len(inpt) == 0:
            break
 
        exam_and_exercises = exam_and_exercise_completed(inpt)
        exercise_pnts = exercise_points(exam_and_exercises[1])
        total_points = exam_and_exercises[0] + exercise_pnts
 
        points.append(total_points)
        grd = grade(total_points)
        if exam_and_exercises[0] < 10:
            grd = 0
        grades[grd] += 1
 
    pass_pros = 100 * (len(points) - grades[0]) / len(points)
 
    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_pros:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")
 
main()