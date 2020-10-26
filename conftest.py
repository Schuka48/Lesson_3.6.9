from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', \
                     help='choose browser: chrome or firefox')
    parser.addoption('--user_language', action='store', default=None, \
                     help='choose language: ru/en/es/...etc.')

@pytest.fixture(scope='function')
def browser(request):
    browser_name =request.config.getoption('browser_name')
    user_language = request.config.getoption('user_language')
    browser = None
    if browser_name == 'chrome':
        print('\nstart chrome browsser..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nstart Firefox browser for test..')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nbrowser quit..')
    browser.quit()

