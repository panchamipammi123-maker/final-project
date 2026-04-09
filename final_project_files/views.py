from django.shortcuts import render, get_object_or_404
from .models import Question, Choice, Submission, Course

# Function to handle exam submission
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        selected_choices = request.POST.getlist('choices')
        submission = Submission.objects.create()
        submission.choices.set(selected_choices)
        submission.save()
        return show_exam_result(request, submission.id)
    return render(request, 'final_project_app/course_details_bootstrap.html', {'course': course})

# Function to show exam result
def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    total_questions = submission.choices.count()
    correct_answers = sum(choice.is_correct for choice in submission.choices.all())
    score = int((correct_answers / total_questions) * 100) if total_questions > 0 else 0
    context = {
        'submission': submission,
        'score': score,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'message': 'Congratulations!' if score >= 70 else 'Try Again!'
    }
    return render(request, 'final_project_app/exam_result.html', context)from django.shortcuts import render

# Create your views here.
