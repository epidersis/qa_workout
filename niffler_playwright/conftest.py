import os
import pytest

@pytest.fixture(scope='session')
def base_url():
    # return "file:///" + os.path.abspath("login.html")
    return 'https://niffler.qa.guru'