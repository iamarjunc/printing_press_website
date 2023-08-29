from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import json

@csrf_exempt
def submit_feedback(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if name and email and message:
            send_feedback_email(name, email, message)
            return JsonResponse({'message': 'Feedback submitted successfully'})
        else:
            return JsonResponse({'error': 'Incomplete data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def send_feedback_email(name, email, message):
    subject = f'Feedback from {name}'
    from_email = 'iamarjunc2000@gmail.com'  # Replace with your sender email
    to_email = 'arjunchandrakumar2017@gmail.com'   # Replace with owner's email address

    send_mail(
        subject,
        message,
        from_email,
        [to_email],
        fail_silently=False,
    )
