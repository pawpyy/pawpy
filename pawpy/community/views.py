from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.db.models import Q

from .models import HashTag, DailyPost
from .forms import DailyPostForm

class DailyListVIew(generic.ListView):
    model = DailyPost
    content_object_name = 'daily_post_list'
    template_name = 'dailypost_list.html'
    paginate_by = 5 # 한 페이지당 5개의 게시글까지만 볼 수 있음
    
    @override
    def get_queryset(self):
        search_word = self.request.GET.get('keyword', '')
        daily_list = DailyPost.objects.order_by('created_date') # 생성 시간에 따라 정렬해서 보여줌
        
        # 검색어가 한 글자일 때
        if len(search_word) > 1:
            search_post_list = daily_list.filter(Q (title__icontains=search_word) | Q (content__icontains=searchword) | Q (tags__icontains=searchword))
            return search_post_list
        elif len(search_word) == 1:
            messages.error(self.request, '검색어는 2글자 이상 입력해 주세요')
        
        # 아무런 검색어가 없을 때에는 모두 보여줌
        return daily_list 
    
    # kwargs로 전달되는 인자는 dictionary의 형태이다.
    def get_context_data(self, **kwargs):
        # call the base implementation first to get the context
        context = super(DailyListView, self).get_context_data(**kwargs)
        page_numbers_range = 5
        max_index = len(paginator.page_range)
        
 
def show_daily(request, pk):
    """
    요청하면 daily post 게시글을 보여주는 함수
    """
    daily_post = DailyPost.objects.get(pk = pk)
    return render(request, 'dailypost_detail.html', {'daily' : daily_post})
    
def write_daily(request):
    """
    새로운 daily 게시글을 작성할 수 있도록 하는 함수
    """
    if not request.session.get('user'):
        return redirect('login/')
    
    if request.method == "GET":
        form = DailyPostForm()
    
    elif request.method == "POST":
        form = DailyPostForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = Users.objects.get(pk = user_id)
            new_daily_post = DailyPost(
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                writer = user,
                image = form.cleaned_data['image'],
            )
            new_daily_post.save()
            
            tag = form.cleaned_data['tag'].split(',')
            for t in tag:
                if not t:
                    continue
                else:
                    t = t.strip() # 양옆의 공백 제거 (혹시 있을 수도 있으니)
                    t_, created = HashTag.objects.get_or_create(name = t)
                    new_daily_post.tag.add(t_)
        return redirect('dailypost/list')
    return render(request, 'dailypost_write.html', {'form' : form})
            
