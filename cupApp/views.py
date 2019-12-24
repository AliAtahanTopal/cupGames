from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Account, Game, Category, Statistic, Comment, Score, Suggestion, Badge
from django.utils import timezone
from .forms import RegisterForm
from datetime import date


# Create your views here.
def index(request):
    games = Game.objects.filter(added_date__lte=timezone.now()).order_by('-added_date')
    scores = Score.objects.filter(score__gte=0).order_by('-score')
    games2 = Game.objects.filter(play_count__gte=0).order_by('-play_count')
    games3 = Game.objects.filter(game_name__contains="").order_by('game_name')
    categorys = Category.objects.filter(category_name__contains="").order_by('category_name')
    return render(request, 'cupApp/index.html',
                  {'games': games, 'scores': scores, 'games2': games2, 'games3': games3, 'categorys': categorys})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        accounts = Account.objects.filter(username=username, password=password)

        if accounts:
            username = request.POST['username']
            request.session['username'] = username
            request.session['success'] = True
            return redirect("index")
        else:
            return redirect("login")
    return render(request, 'cupApp/login.html', {})


def forgotPassword(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        error = ""
        account = Account.objects.filter(username=username, email=email)

        if account:
            return redirect('forgotPassword2', pk=username)
        else:
            error = "wrong"
            return render(request, 'cupApp/forgotPassword.html', {'error': error})
    return render(request, 'cupApp/forgotPassword.html', {})


def forgotPassword2(request, pk):
    if request.method == 'POST':
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']
        username = pk

        if password_1 == password_2:
            Account.objects.filter(username=username).update(password=password_1)
            return redirect('login')
        else:
            error = "wrong"
            return render(request, 'cupApp/forgotPassword2.html', {'error': error})
    return render(request, 'cupApp/forgotPassword2.html', {})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            account = form.save()
            account.refresh_from_db()
            account.username = form.cleaned_data.get('username')
            account.password = form.cleaned_data.get('password')
            account.email = form.cleaned_data.get('email')
            account.gender = form.cleaned_data.get('gender')
            account.date_of_birth = request.POST['date_of_birth']

            account.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'cupApp/register.html', {'form': form})


def logoutpage(request):
    del request.session['username']
    request.session['success'] = False
    return HttpResponseRedirect(reverse('index'))


def profile(request, pk):
    return render(request, 'cupApp/profile.html')


def leaderboards(request):
    week = date.today().isocalendar()[1]
    scores = Score.objects.filter(score__gte=0).order_by('-score')
    scores1 = Score.objects.filter(score__gte=0, score_date__month=timezone.now().month).order_by('-score')
    scores2 = Score.objects.filter(score__gte=0, score_date__week=week).order_by('-score')
    return render(request, 'cupApp/leaderboards.html', {'scores': scores, 'scores2': scores2, 'scores1': scores1})


def becomepremium(request):
    return render(request, 'cupApp/becomepremium.html')


def gamepage(request, pk):
    game = get_object_or_404(Game, pk=pk)
    categorys = Category.objects.filter(category_name__contains="").order_by('category_name')
    account = Account.objects.get(username=request.session['username'])
    scores = Score.objects.filter(score__gte=0).order_by('-score')
    comments = Comment.objects.all()
    if request.method == 'POST':
        print(request.POST)
        comment_box = request.POST.get('comment_box')
        if comment_box:
            comment = Comment.objects.create(text=comment_box, game_name=game,
                                             username=account)
            return redirect('gamepage', pk=game.game_name)

    return render(request, 'cupApp/gamepage.html', {'game': game, 'categorys': categorys, 'comments': comments,
                                                    'scores': scores})


def categorypage(request, pk):
    games = Game.objects.filter(added_date__lte=timezone.now()).order_by('-added_date')
    games2 = Game.objects.filter(play_count__gte=0).order_by('-play_count')
    games3 = Game.objects.filter(game_name__contains="").order_by('game_name')
    categorys = Category.objects.filter(category_name__contains="").order_by('category_name')
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'cupApp/categorypage.html',
                  {'category': category, 'games': games, 'games2': games2, 'games3': games3, 'categorys': categorys})


def account_new(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            return redirect('account_detail', pk=account.pk)
    else:
        form = RegisterForm()
    return render(request, 'cupApp/account_edit.html', {'form': form})


def premiumprocess(request, pk):
    accounts = get_object_or_404(Account, pk=pk)
    accounts
