from django.shortcuts import render
from django.views import View
from account_module.models import User
from .forms import EditProfileModelForm


class editProfile(View):

    def get(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        print('current_user: ', current_user)
        # edit_form = EditProfileModelForm(initial={'first_name':current_user.first_name,'last_name':current_user.last_name})
        edit_form = EditProfileModelForm(instance = current_user)
        context = {'form': edit_form,'current_user':current_user}
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request):
        current_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
        context = {'form': edit_form,'current_user':current_user}
        return render(request, 'user_panel_module/edit_profile_page.html',context)
