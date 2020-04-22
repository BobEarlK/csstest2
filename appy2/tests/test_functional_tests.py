import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils import timezone

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of



MAX_WAIT = 3


class FunctionalTests(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        old_page = self.browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.browser, timeout).until(
            staleness_of(old_page)
        )

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            time.sleep(1)
            try:
                return fn()
            except (WebDriverException, AssertionError) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e

class PageDisplayTest(FunctionalTests):
    def test_show_styled_css_text(self):
        self.browser.get(f'{self.live_server_url}')
        self.assertEqual(self.browser.title, 'Front Page')
        stylized_text = self.browser.find_element_by_id('id_stylized_text')
        self.assertEqual(stylized_text.text, 'bwahahahahaha')