# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def names_args(func, *args):
    func = func.__name__.capitalize().replace('_', ' ')
    print('Function name:', func)
    print('Function args:', *args)
    print()



def open_browser(browser_name):
    names_args(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    names_args(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    names_args(find_registration_button_on_login_page, page_url, button_text)




open_browser('Chrome')
go_to_companyname_homepage('google.com')
find_registration_button_on_login_page('url', 'Sign in')