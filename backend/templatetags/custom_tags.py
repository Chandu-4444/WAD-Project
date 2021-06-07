from django import template
from backend.models import Project

register = template.Library()

@register.filter(name='update_variable')
def update_variable(flag, arg):
    print(arg)
    user, curr_user = arg.split(" ")
    return flag

@register.simple_tag
def check_user( project_id, user, curr_user):
    print()
    print("Users = ", user,"Curr_user = ", curr_user)
    # print(type(user[0]), type(curr_user))
    project = Project.objects.get(id=project_id)
    if project.owner.user.username == curr_user.user.username:
        return "owner"
    for user_obj in user.all():
        print(user_obj.user.username, curr_user.user.username)
        if user_obj.user.username == curr_user.user.username:
            print("Matched", user_obj, user)
            return "found"
    return None