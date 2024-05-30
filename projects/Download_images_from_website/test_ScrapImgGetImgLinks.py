import pytest
import os
import sys
import importlib.util
from bs4 import BeautifulSoup

# Define and load the module
module_name = 'scrap-img'
module_path = os.path.join(os.path.dirname(__file__), f'{module_name}.py')
spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class Test_ScrapImgGetImgLinks:

    def test_get_img_links_for_well_formed_html(self):
        # Arrange
        well_formed_html = '<html><body><img src="link1" /><img src="link2" /></body></html>'
        expected_links = ['link1', 'link2']

        # Act
        result_links = module.get_img_links(well_formed_html)

        # Assert
        assert all(link['src'] in expected_links for link in result_links)

    def test_get_img_links_for_html_with_no_img_links(self):
        # Arrange
        no_img_links_html = '<html><body><p>No img links here</p></body></html>'

        # Act
        result_links = module.get_img_links(no_img_links_html)

        # Assert
        assert len(result_links) == 0

    def test_get_img_links_for_empty_html(self):
        # Arrange
        empty_html = ''

        # Act
        result_links = module.get_img_links(empty_html)

        # Assert
        assert len(result_links) == 0

    def test_get_img_links_for_malformed_html(self):
        # Arrange
        malformed_html = '<html><body><img src="link1" /><img src="link2" </body></html>'

        # Act
        try:
            result_links = module.get_img_links(malformed_html)
            assert isinstance(result_links, list)
        except Exception as e:
            pytest.fail(f"Test failed due to: {str(e)}")
