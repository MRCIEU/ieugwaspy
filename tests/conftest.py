import pytest

import ieugwaspy


def pytest_addoption(parser):
    parser.addoption(
        "--select-api", action="store", default="public", help="Provide the key to the API url"
    )


@pytest.fixture(scope="session")
def ieugwaspy_instance(request):
    i = ieugwaspy
    i.select_api(request.config.getoption("--select-api"))
    return i
