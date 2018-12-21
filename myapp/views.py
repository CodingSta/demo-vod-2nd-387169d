from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, TemplateView, RedirectView
from .models import Post


post_list = ListView.as_view(model=Post)


post_detail = DetailView.as_view(model=Post)


# def myview(request):
#     context = {
#         'hello': 'world',
#         'ip': request.META['REMOTE_ADDR'],
#     }
#     return render(request, 'myapp/myview.html', context)


class MyTemplateView(TemplateView):
    template_name = 'myapp/myview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'hello': 'world',
            'ip': self.request.META['REMOTE_ADDR'],
        })
        return context

myview = MyTemplateView.as_view()


# def myview2(request):
#     return redirect('https://m.naver.com')

myview2 = RedirectView.as_view(url='https://m.naver.com')
