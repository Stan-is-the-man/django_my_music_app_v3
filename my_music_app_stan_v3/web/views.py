from django.shortcuts import render, redirect

from my_music_app_stan_v3.web.form import CreateProfileForm, BaseAlbumForm, DeleteAlbumForm, DeleteProfileForm
from my_music_app_stan_v3.web.models import Profile, Album


def profile_get():
    try:
        return Profile.objects.get()

    except:
        return None


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'profile_exists': True,
    }

    return render(request, 'home-no-profile.html', context)


def home_page(request):
    profile = profile_get()
    albums = Album.objects.all()

    if profile is None:
        return redirect('home with no profile')

    context = {
        'albums': albums,
    }
    return render(request, 'home-with-profile.html', context)


def album_add(request):
    if request.method == 'POST':
        form = BaseAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = BaseAlbumForm()
    context = {
        'form': form,
    }
    return render(request, 'album-add.html', context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }

    return render(request, 'album-details.html', context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = BaseAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = BaseAlbumForm(instance=album)

    context = {
        'form': form,
    }

    return render(request, 'album-edit.html', context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
    }

    return render(request, 'album-delete.html', context)


def profile_details(request):
    profile = profile_get()
    albums = Album.objects.all()
    count_of_albums = len(albums)
    context = {
        'profile': profile,
        'count_of_albums': count_of_albums,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = profile_get()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home with profile')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
