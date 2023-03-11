from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy

from users.forms import SignUp, UpdateProfile, ProfileForm
from django.contrib.auth import authenticate, logout, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from firstapp.models import Category
from django.contrib.auth.models import User
from django.contrib import messages

from users.models import Profile


# registration view
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('page_404')
        # raise Http404('page not found')

    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()

            return redirect('login')

        else:
            print(form.errors)
            return render(request, 'users/register.html', {'form': form})

    return render(request, 'users/register.html')


# login view
def login_page(request):
    if request.user.is_authenticated:
        return redirect('page_404')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                return render(request, 'users/login.html', {'invalid': True})

        else:
            print('sdfasdfasdfasdfasdfasdfasdffffffffffffffff')
            print(form.errors)
            return render(request, 'users/login.html', {'invalid': True})

    return render(request, 'users/login.html')


# logout view
@login_required()
def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('login')


@login_required()
def profile(request):
    user = request.user
    form = UpdateProfile(request.POST, instance=request.user)
    profile_image = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
    p_img = Profile.objects.get(user=user)
    context = {
        'user': user,
        'form': form,
        'profile_image': profile_image,
        'p_image': p_img,

    }
    if request.method == 'POST':

        if form.is_valid() and profile_image.is_valid():
            username_check = form.cleaned_data.get('username')
            print('user check')
            if username_check == user.username:
                pass

            elif User.objects.filter(username=username_check).exists():
                print('invalid')
                return render(request, 'users/user_profile.html', {'invalid': True})

            form.save()
            profile_image.save()

            return render(request, 'users/user_profile.html', {'success_message': True, 'p_image': p_img})

        else:
            print(form.errors)
            messages.info(request, "This username already exists.")
            pass

    return render(request, 'users/user_profile.html', context)


def password_chang(request):
    form = ChangePassword(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print('secondsecondseconndsecondsecondsecondsecondsecondsecondsecondsecondsecond')
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            confirm_password = form.cleaned_data['confirm_password']
            print('---------------------------------------')
            print('3333333333333333333333333333333333333333333333333333333')
            user = User.objects.get(username=request.user.username)
            if not user.check_password(old_password):
                messages.warning(request, 'old password is not correct')
            else:
                if new_password != confirm_password:
                    messages.warning(request, 'new password not match confirm password')

                elif len(new_password) < 8 or new_password.lower() == new_password or \
                        new_password.upper() == new_password or new_password.isalnum() or \
                        not any(i.isdigit() for i in new_password):
                    messages.warning(request, 'your password is too weak!!')

                else:
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)

                    messages.success(request, 'your password has been successfuly changed')
                    return redirect('profile')

        else:
            messages.warning(request, 'sorry, all field are required')

    return render(request, 'users/password_chad.html')


@login_required()
# password change
def password_change(request):
    error_message = None
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
        else:
            print(form.errors)
            error_message = 'ERROR: please enter a correct value'
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'users/password_change.html', {'form': form, 'error_message': error_message})
