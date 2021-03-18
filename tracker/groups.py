from tracker.models import Student
from tracker.models import Assessment
from tracker.models import Standard

def ResolveGroups(numbergroups, selected_standards):
    students = Student.objects.all()
    assessments = Assessment.objects.filter(standard__id__in=selected_standards)
    students_and_scores = []

    for student in students:
        scores = []
        for assessment in assessments:
            if student == assessment.student:
                scores.append(assessment.score)
        avg_score = 0
        if len(scores) > 0: 
            avg_score = sum(scores)/len(scores)
        students_and_scores.append({
            "student" : student,
            "score" : avg_score
        })

    students_and_scores.sort(
        key = lambda x:x['score']
    )

    group_size = len(students) / numbergroups
    
    ranked_student_dictionary_index = 0
    for ranked_student_dictionary in students_and_scores:
        print(f"{ranked_student_dictionary['student'].first_name} has a score of {ranked_student_dictionary['score']}")
        group_index = int(ranked_student_dictionary_index // group_size) + 1
        ranked_student_dictionary["group_id"] = group_index
        print(f" > And in Group: {group_index}")
        print(" ")
        ranked_student_dictionary_index += 1

    return students_and_scores