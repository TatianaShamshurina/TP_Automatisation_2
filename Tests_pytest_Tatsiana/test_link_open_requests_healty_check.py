import requests
import pytest

# avec requests == on gagne la vitesse 70 sec (sans requests) vs 8.58 sec (avec requests)


class TestPages:

    @pytest.mark.parametrize("url", open("verification_urls.txt").readlines())
    def test_open_pages(self, url):
        url = url.strip()
        response = requests.get(url)
        assert response.status_code == 200, "Page not found"