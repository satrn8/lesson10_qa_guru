from typing import Optional
from selene import have
from selene.core.entity import Element
from selene.support.shared import browser


class Table:
    def __init__(self, row_num):
        self.row_num = row_num

    def should_have(self, *results):
        for result in results:
            browser.all('.table-responsive tbody tr')[self.row_num].all('td')[1].should(have.exact_text(result))