from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from dislikeapp.models import DislikeRec
from likeapp.models import LikeRec
from sosoapp.models import SosoRec


@method_decorator(login_required,'get')
class DislikeView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': self.request.GET.get('article_pk')})

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=self.request.GET.get('article_pk'))
        user = self.request.user

        dislike_rec = DislikeRec.objects.filter(user=user,
                                                   article=article)
        like_rec = LikeRec.objects.filter(user=user,
                                                article=article)
        soso_rec = SosoRec.objects.filter(user=user,
                                                article=article)
        if dislike_rec.exists():
            dislike_rec.delete()
            article.dislike -= 1
            article.save()
        else:
            if like_rec.exists():
                like_rec.delete()
                article.like -= 1
            if soso_rec.exists():
                soso_rec.delete()
                article.soso -= 1
            DislikeRec(user=user,article=article).save()
            article.dislike += 1
            article.save()
        return super(DislikeView, self).get(request, *args, **kwargs)

@method_decorator(login_required, 'get')
class DislikeListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'dislikeapp/list.html'
    paginate_by = 5

    def get_queryset(self):
        articles = DislikeRec.objects.filter(user=self.request.user).values_list('article')
        article_list = Article.objects.filter(project__in=articles)
        return article_list