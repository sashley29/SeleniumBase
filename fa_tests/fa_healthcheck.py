from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_home(self):
	self.open("https://www.fayetteacademy.org")           # Navigate browser to page
	title = self.get_title()
	self.assertTrue('Fayette Academy' in title)	

    def test_events(self):
   	self.open("https://events.fayetteacademy.org")
	title = self.get_title()
	self.assertTrue('Fayette Academy Events' in title)

        ####

        #######################################################################
        #
        #    ****  NOTES / USEFUL INFO  ****
        #
        # 1. By default, CSS Selectors are used to identify elements.
        #    Other options include: "LINK_TEXT", "PARTIAL_LINK_TEXT", "NAME",
        #    "CLASS_NAME", and "ID", but most of those can be expressed as CSS.
        #    Here's an example of changing the "by":
        #    [
        #        from selenium.webdriver.common.by import By
        #        ...
        #        self.click('Next', by=By.PARTIAL_LINK_TEXT)
        #    ]
        #    XPath is used by default if the arg starts with "/", "./", or "(":
        #    [
        #        self.click('/html/body/div[3]/div[4]/p[2]/a')
        #    ]
        #
        #    If you're completely new to CSS selectors, right-click on a
        #    web page and select "Inspect" to see the CSS in the html.
        #
        # 2. Most methods have the optional `timeout` argument. Ex:
        #    [
        #        self.get_text('div center', timeout=15)
        #    ]
        #    The `timeout` argument tells the method how many seconds to wait
        #    for an element to appear before raising an exception. This is
        #    useful if a web page needs additional time to load an element.
        #    If you don't specify a `timeout`, a default timeout is used.
        #    Default timeouts are configured in seleniumbase/config/settings.py
        #
        # 3. There's usually more than one way to do the same thing. Ex:
        #    [
        #        self.assert_text('free to copy', 'div center')
        #    ]
        #    Is the same as:
        #    [
        #        text = self.get_text("div center")
        #        self.assert_true("free to copy" in text)
        #    ]
        #    Or:
        #    [
        #        text = self.find_element('div center').text
        #        assert("free to copy" in text)
        #    ]
        #
        #    And the following line:
        #    [
        #        title = self.get_attribute("#comic img", "title")
        #    ]
        #    Can also be written as:
        #    [
        #        element = self.find_element("#comic img")
        #        title = element.get_attribute("title")
        #    ]
        #
        #    For backwards-compatibilty, some SeleniumBase methods that do the
        #    same thing have multiple names, kept on from previous versions.
        #    Ex: wait_for_element_visible() is the same as find_element().
        #    Both search for and return the element, and raise an exception if
        #    the element does not appear on the page within the timeout limit.
        #    And assert_element() also does this (minus returning the element).
        #
        #    (See seleniumbase/fixtures/base_case.py for the full method list.)
