# Take in a request and return a Http Response
# Might able to add action but not sure yet
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    #Creating a New Object
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    #Editing a New Object
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    # Deleting an Object
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    # What is the blueprint of your forms
    form_class = UserForm
    # Which html file are you referring to
    template_name = 'music/registration_form.html'

    # Display a blank form for new user
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Process form data to database
    def post(self, request):
        form = self.form_class(request.POST)

        # Creates an object from the form, hasn't enter info to database
        # This is just an object which store in local
        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #whenever you wanted to change users' password this is how due to hashing
            user.set_password(password)
            user.save()

            #return User object if credential are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
                    # This is how you retreive certain info of the user within the session
                    #request.user.username

        return render(request, self.template_name, {'form': form})








# def index(request):
#     # Same code as using the database API
#     # template => Referencing the template in the templates directory of the App
#     # context => Information that your templates need
#     # HttpResponse(template.render(context,request)) => take in variable context(info carrier),
#     # and the url request and spits out the corresponding template
#     # can use global or local variable as context
#     # index/ detail uses different way to pass in variable but both are the same method
#     all_albums = Album.objects.all()
#     context = {'all_albums': all_albums}
#     return render(request,'music/index.html',context)
#
# def detail(request, album_id):
#     # album = Album.objects.get(pk=album_id)
#     album = get_object_or_404(Album, pk=album_id)
#     return render(request, 'music/detail.html', {'album': album})
#
# # Example of how to build a form
# # def favorite(request, album_id):
# #     album = get_object_or_404(Album, pk=album_id)
# #     try:
# #         selected_song = album.song_set.get(pk=request.POST['song'])
# #     except(KeyError, Song.DoesNotExist):
# #         return render(request, 'music/detail.html', {
# #             'album': album,
# #             'error_message': "You did not select a valid song",
# #         })
# #     else:
# #         selected_song.is_favorite = True
# #         selected_song.save()
# #         return render(request, 'music/detail.html', {'album': album})










