from django.shortcuts import render

def main(request):
    return render(request,template_name='main.html')


def index(request):
    apps = [
         {
            "name": "StudyBuddy",
            "description": "Collaborative learning & chat platform",
            "url": "/studybuddy/",
            "login_required": True,
            "icon": "📚",
        },
        {
            "name": "Expense Tracker",
            "description": "Track daily and monthly expenses",
            "url": "/expenses/",
            "login_required": True,
            "icon": "💰",
        },
        {
            "name": "Community Chat",
            "description": "Real-time community discussions",
            "url": "/chat/",
            "login_required": False,
            "icon": "💬",
        },
    ]
    return render(request,template_name='index.html',context={"apps":apps})