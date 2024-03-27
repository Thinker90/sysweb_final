from django.shortcuts import render


posts = [
    {
        'id': 0,
        'author': 'Володя',
        'date': '30 сентября 1659 года',
        'title': 'тут ваш заголовок 1',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'author': 'Петя',
        'date': '1 октября 1659 года',
        'title': 'тут ваш заголовок 2',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'author': 'Маша',
        'date': '25 октября 1659 года',
        'title': 'тут ваш заголовок 3',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]
def index(request):
    context = {'posts': posts}
    return render(request, 'www/index.html', context)


def category(request, category_slug):
    context = {'slug': category_slug}
    return render(request, 'www/category.html', context)


def detail(request, pk):
    context = {'post': pk}
    return render(request, 'www/detail.html', context)


def all_news(request):
    return render(request, 'www/news_all.html')
