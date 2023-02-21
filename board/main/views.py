from django.shortcuts import render, redirect
from board.settings import BASE_DIR
from django.core.paginator import Paginator
from .forms import CreateForm, CreateReplyForm
from .models import Ads, Reply
from django.views.generic import UpdateView, DetailView, CreateView, UpdateView
# Create your views here.


def mainview(request):
    ads = Ads.objects.all()
    paginator = Paginator(ads, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'ads': ads, 'page_obj': page_obj, }

    print(page_obj)
    return render(request, template_name='main/main.html', context=context)


def editads(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            ads = form.save(commit=False)
            ads.author = request.user
            ads.save()
            return redirect('/')
    else:
        form = CreateForm()
    return render(request, 'main/edit.html', {'form': form},)


class DetailAds(DetailView):
    model = Ads
    template_name = 'main/detail.html'
    context_object_name = 'context'


class UpdateAds(UpdateView):
    model = Ads
    template_name = 'main/edit.html'
    fields = ['title', 'text', 'category', 'upload']


class ReplyOnAds(CreateView):
    template_name = 'main/reply.html'
    form_class = CreateReplyForm
    # permission_required = ...
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form = CreateReplyForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.ads = Ads.objects.get(pk=kwargs['pk'])
            instance.author = request.user
            instance.save()
            return redirect('/')
        return render(request, 'main/reply.html', {'form': form})