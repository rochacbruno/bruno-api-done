import os
import sys
import pytest

from fastapi.testclient import TestClient
from typer.testing import CliRunner

# This next line ensures tests uses its own database and settings environment
os.environ["FORCE_ENV_FOR_DYNACONF"] = "testing"  # noqa
# WARNING: Ensure imports from `bruno_api` comes after this line

from bruno_api.app import app
from bruno_api.cli import cli
from bruno_api.config import settings


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    """Ensure each test runs on its own working dir"""
    # Get the fixture dynamically by its name.
    tmpdir = request.getfixturevalue("tmpdir")
    # ensure local test created packages can be imported
    sys.path.insert(0, str(tmpdir))
    # Chdir only for the duration of the test.
    with tmpdir.as_cwd():
        yield


@pytest.fixture(scope="function", name="app")
def _app():
    return app


@pytest.fixture(scope="function", name="cli")
def _cli():
    return cli


@pytest.fixture(scope="function", name="settings")
def _settings():
    return settings


@pytest.fixture(scope="function")
def api_client():
    return TestClient(app)


@pytest.fixture(scope="function")
def cli_client():
    return CliRunner()
