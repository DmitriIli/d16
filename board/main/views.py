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
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.post_author = self.request.user
            instance.save()
            return HttpResponseRedirect(......)
        return render(request, 'news/create_post.html', {'form': form})

# class PostCreateView(PermissionRequiredMixin, CreateView):
#     template_name = 'news/create_post.html'
#     form_class = PostForm
#     permission_required = ('news.add_post')
#     raise_exception = True

#     # Функция для кастомной валидации полей формы модели
#     def form_valid(self, form):
#         # создаем форму, но не отправляем его в БД, пока просто держим в памяти
#         fields = form.save(commit=False)
#         # Через реквест передаем недостающую форму, которая обязательна
#         fields.post_author = Author.objects.get(author=self.request.user)
#         # Наконец сохраняем в БД
#         fields.save()
#         return super().form_valid(form)