from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.utils.crypto import get_random_string
from utils.email_services import send_email
from .forms import RegisterForm, LoginForm
from .models import User
# user = get_user_model()

def register(request):
    register_form = RegisterForm(request.POST or None)
    context = {'register_form': register_form}
    if register_form.is_valid():
        print('reg form: ', register_form)
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        user = User.objects.filter(email__iexact=email).exists()
        if user:
            register_form.add_error('email', 'این کاربر از قبل وجود دارد')
            # print('user before is exists.')
        else:
            # new_user = User(username=user_email, email=user_email, email_active_code=get_random_string(72),
            #                 is_active=False)
            # new_user.set_password(user_pass)
            # new_user.save()
            # send_email('فعالسازی حساب کاربر', new_user.email, {'user': new_user}, 'emails/activate_account.html')
            # return redirect(reverse('login_page'))
            new_user = User(username=email, email=email, email_activation_code=get_random_string(6), is_active=False)
            new_user.set_password(password)
            new_user.save()
            print('new_user ', new_user.email, new_user.username)
            send_email('فعالسازی حساب کاربر', new_user.email, {'user': new_user}, 'emails/activation_account.html')
            return redirect('/')
    return render(request, 'account_module/register_page.html', context)

def loginFunction(request):
    login_form = LoginForm(request.POST or None)
    context = {'login_form': login_form}
    if login_form.is_valid():
        # print('user is: ',request.user.is_authenticated)
        print(login_form.cleaned_data)
        email = login_form.cleaned_data.get('email')
        password = login_form.cleaned_data.get('password')
        # user = authenticate(request,email=email,password=password)
        user = User.objects.filter(email=email).first()
        print('user line 50: ', user)
        # current_user = user.object.filter(email=email).exists()
        if user is not None:
            is_pass_corect = user.check_password(password)
            if is_pass_corect:
                print('user line 55: ', user)
                login(request, user)
                context['login_form'] = login_form
                return redirect('/')
        else:
            print('error')

    return render(request, 'account_module/login_page.html', context)

def activeAccount(request, activation_code):
    print('activation_code: ', activation_code)
    # user = User.objects.get(email_activation_code=activation_code)
    user: User = User.objects.filter(email_activation_code=activation_code)[0]
    print('user line 68: ', user)
    if user is not None:
        user.is_active = True
        user.save()
        return redirect('/login')
    raise Http404

def logoutFunction(request):
    if request.user.is_authenticated:
        print('user is: ',request.user.is_authenticated)
        logout(request)
        return redirect('/')
    else:
        print('error')
    return render(request, 'account_module/login_page.html')










