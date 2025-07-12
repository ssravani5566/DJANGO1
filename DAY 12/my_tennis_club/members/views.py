from django.shortcuts import render
from .models import Member

def members(request):
    # Get all Member objects from DB
    all_members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': all_members})
