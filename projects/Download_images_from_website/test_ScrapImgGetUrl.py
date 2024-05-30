import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import importlib.util
import os
import sys

# Define and load the module
module_name = 'scrap-img'
module_path = os.path.join(os.path.dirname(__file__), f'{module_name}.py')
spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class Test_ScrapImgGetUrl:

    def test_get_url_valid_path_and_url(self):
        # Arrange
        valid_path = "/path/to/chromedriver"
        valid_url = "https://www.google.com"
        expected_html = "<html>...</html>"  # TODO: Replace with actual expected HTML

        # Act
        actual_html = module.get_url(valid_path, valid_url)

        # Assert
        assert actual_html == expected_html

    def test_get_url_invalid_path(self):
        # Arrange
        invalid_path = "/invalid/path"

        # Act & Assert
        with pytest.raises(WebDriverException):
            module.get_url(invalid_path, "https://www.google.com")

    def test_get_url_invalid_url(self):
        # Arrange
        valid_path = "/path/to/chromedriver"
        invalid_url = "invalid_url"

        # Act & Assert
        with pytest.raises(WebDriverException):
            module.get_url(valid_path, invalid_url)

    def test_get_url_404(self):
        # Arrange
        valid_path = "/path/to/chromedriver"
        url_404 = "http://www.thisurldoesnotexist.com"

        # Act
        html_404 = module.get_url(valid_path, url_404)

        # Assert
        assert "404" in html_404
