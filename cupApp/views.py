from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Account, Game, Category, Statistic, Comment, Score, Suggestion, Badge, Favorite, FavCategory
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
    if 'success' in request.session:
        print("xd")
    else:
        request.session['success'] = False
    return render(request, 'cupApp/index.html',
                  {'games': games, 'scores': scores, 'games2': games2, 'games3': games3, 'categorys': categorys})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        accounts = Account.objects.filter(username=username, password=password)
        error = ""
        if accounts:
            account = accounts.get(username=username, password=password)
            if account.type == "AD":
                username = request.POST['username']
                request.session['username'] = username
                request.session['success'] = True
                request.session['playLimit'] = account.playLimit
                return redirect("adminpanel")
            else:
                username = request.POST['username']
                request.session['username'] = username
                request.session['success'] = True
                request.session['playLimit'] = account.playLimit
                return redirect("index")
        else:
            error = "wrong"
            return render(request, 'cupApp/login.html', {'error': error})
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


def changepassword(request, pk):
    if request.method == 'POST':
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        username = pk

        if password_1 == password_2:
            Account.objects.filter(username=username).update(password=password_1)
            return redirect('profile', pk=pk)
        else:
            error = "wrong"
            return render(request, 'cupApp/accountsettings.html', {'error': error})
    return render(request, 'cupApp/accountsettings.html', {})


def accountsettings(request, pk):
    account = get_object_or_404(Account, username=pk)
    return render(request, 'cupApp/accountsettings.html', {'account': account})


def changeemail(request, pk):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = pk
        Account.objects.filter(username=username).update(email=email)
        return redirect('profile', pk=pk)
    else:
        return render(request, 'cupApp/accountsettings.html', {})


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
    del request.session['playLimit']
    request.session['success'] = False
    return HttpResponseRedirect(reverse('index'))


def profile(request, pk):
    account = get_object_or_404(Account, username=pk)
    favorites = Favorite.objects.filter(username=account.username)
    game = Game.objects.all()
    favcategories = FavCategory.objects.filter(username=account.username)
    statistics = Statistic.objects.filter(username=account.username)
    badge = Badge.objects.filter(username=account.username)
    return render(request, 'cupApp/profile.html', {'account': account, 'favorites': favorites, 'game': game,
                                                   'favcategories': favcategories, 'statistics': statistics,
                                                   'badge': badge})


def searchpage(request):
    games = Game.objects.all()
    return render(request, 'cupApp/searchpage.html', {'games': games})


def leaderboards(request):
    week = date.today().isocalendar()[1]
    scores = Score.objects.filter(score__gte=0).order_by('-score')
    scores1 = Score.objects.filter(score__gte=0, score_date__month=timezone.now().month).order_by('-score')
    scores2 = Score.objects.filter(score__gte=0, score_date__week=week).order_by('-score')
    return render(request, 'cupApp/leaderboards.html', {'scores': scores, 'scores2': scores2, 'scores1': scores1})


def viewSuggestions(request):
    newSuggestions = Suggestion.objects.filter(is_checked=False, is_starred=False).order_by('-submit_time')
    checkedSuggestions = Suggestion.objects.filter(is_checked=True, is_starred=False).order_by('-last_modified')
    starredSuggestions = Suggestion.objects.filter(is_checked=True, is_starred=True).order_by('-last_modified')
    return render(request, 'cupApp/viewSuggestions.html',
                  {'newSuggestions': newSuggestions, 'checkedSuggestions': checkedSuggestions,
                   'starredSuggestions': starredSuggestions})


def suggestion(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk)
    if request.method == 'POST':
        checkCheck = False
        starCheck = False
        if request.POST.get('check'):
            checkCheck = True
        if request.POST.get('uncheck'):
            checkCheck = False
        if request.POST.get('star'):
            starCheck = True
        if request.POST.get('unstar'):
            starCheck = False
        Suggestion.objects.filter(suggestion_id=pk).update(is_checked=checkCheck, is_starred=starCheck)
        return redirect('viewSuggestions')
    return render(request, 'cupApp/suggestion.html', {'suggestion': suggestion})


def becomepremium(request, pk):
    account = get_object_or_404(Account, pk=pk)
    error = ""
    if request.method == "POST":
        if account.coins >= 20000:
            Account.objects.filter(username=pk).update(type="PU")
            Account.objects.filter(username=pk).update(coins=account.coins - 20000)
            return redirect('index')
        else:
            error = "You don't have enough coins"
    return render(request, 'cupApp/becomepremium.html', {'account': account, 'error': error})


def gamepage(request, pk):
    game = get_object_or_404(Game, pk=pk)
    categorys = Category.objects.filter(category_name__contains="").order_by('category_name')
    scores = Score.objects.filter(score__gte=0).order_by('-score')
    if request.session['success']:
        favorites = Favorite.objects.filter(game_name=game.game_name, username=request.session['username'])
        if favorites:
            favorites = Favorite.objects.filter(game_name=game.game_name, username=request.session['username'])
        else:
            favorites = "no"
    else:
        favorites = ""
    comments = Comment.objects.all()
    if request.method == 'POST':
        account = Account.objects.get(username=request.session['username'])
        comment_box = request.POST.get('comment_box')
        if comment_box:
            comment = Comment.objects.create(text=comment_box, game_name=game,
                                             username=account)
            return redirect('gamepage', pk=game.game_name)
    else:
        return render(request, 'cupApp/gamepage.html', {'game': game, 'categorys': categorys, 'comments': comments,
                                                        'scores': scores, 'favorites': favorites})


def suggestGame(request):
    if request.method == 'POST':

        game_name_input = request.POST.get('game_name_input')
        description_box = request.POST.get('description_box')
        error = "";
        if game_name_input and description_box:
            if request.session['success']:
                account = Account.objects.get(username=request.session['username'])
            else:
                account = None

            suggest_detail = description_box
            if request.POST.get('game_link_input'):
                suggest_link = request.POST.get('game_link_input')
                suggestion = Suggestion.objects.create(username=account, detail=suggest_detail,
                                                       game_link=suggest_link)
            else:
                suggestion = Suggestion.objects.create(username=account, detail=suggest_detail)

            return redirect('index')
        else:
            error = "You must fill the name and description fields"
            return render(request, 'cupApp/suggestGame.html', {'error': error})
    else:
        return render(request, 'cupApp/suggestGame.html', {})


def addfavorite(request, pk):
    game = Game.objects.get(game_name=pk)
    account = Account.objects.get(username=request.session['username'])
    favorite = Favorite.objects.create(username=account, game_name=game)
    return redirect('gamepage', pk=game.game_name)


def removefavorite(request, pk):
    game = Game.objects.get(game_name=pk)
    account = Account.objects.get(username=request.session['username'])
    favorite = Favorite.objects.filter(username=account, game_name=game).delete()
    return redirect('gamepage', pk=game.game_name)


def addfavoritecategory(request, pk):
    category = Category.objects.get(category_name=pk)
    account = Account.objects.get(username=request.session['username'])
    favorite = FavCategory.objects.create(username=account, category_name=category)
    return redirect('categorypage', pk=category.category_name)


def removefavoritecategory(request, pk):
    category = Category.objects.get(category_name=pk)
    account = Account.objects.get(username=request.session['username'])
    favorite = FavCategory.objects.filter(username=account, category_name=category.category_name).delete()
    return redirect('categorypage', pk=category.category_name)


def categorypage(request, pk):
    games = Game.objects.filter(added_date__lte=timezone.now()).order_by('-added_date')
    games2 = Game.objects.filter(play_count__gte=0).order_by('-play_count')
    games3 = Game.objects.filter(game_name__contains="").order_by('game_name')
    scores = Score.objects.filter(score__gte=0).order_by('-score')
    categorys = Category.objects.filter(category_name__contains="").order_by('category_name')
    category = get_object_or_404(Category, pk=pk)
    if request.session['success']:
        favorites = FavCategory.objects.filter(category_name=category.category_name,
                                               username=request.session['username'])
        if favorites:
            favorites = FavCategory.objects.filter(category_name=category.category_name,
                                                   username=request.session['username'])
        else:
            favorites = "no"
    else:
        favorites = ""
    return render(request, 'cupApp/categorypage.html',
                  {'category': category, 'games': games, 'games2': games2, 'games3': games3, 'categorys': categorys,
                   'favorites': favorites, 'scores': scores})


def adminpanel(request):
    return render(request, 'cupApp/adminpanel.html')
