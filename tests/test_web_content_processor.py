import pytest


from web_content_processor.WebContentProcessor import WebContentProcessor


def test_is_url_skipped_youtube():
    assert (
        WebContentProcessor.is_url_skipped(
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        )
        == True
    )


def test_is_url_skipped_vimeo():
    assert WebContentProcessor.is_url_skipped("https://vimeo.com/123456789") == True


def test_is_url_skipped_not_skipped():
    assert (
        WebContentProcessor.is_url_skipped("https://www.example.com/article") == False
    )


def test_is_url_skipped_partial_match():
    assert (
        WebContentProcessor.is_url_skipped(
            "https://www.mysite.com/youtube-video-analysis"
        )
        == False
    )


import unittest
from unittest.mock import patch, MagicMock
from web_content_processor.WebContentProcessor import SocialMediaPoster, UrlLogger, ContentFetcher


class TestSocialMediaPoster(unittest.TestCase):
    @patch("socialModules.moduleRules.moduleRules")
    def test_post_to_social_media(self, mock_rules):
        # Arrange
        mock_rules_instance = MagicMock()
        mock_rules.return_value = mock_rules_instance

        mock_api_src = MagicMock()
        mock_rules_instance.readConfigDst.return_value = mock_api_src

        poster = SocialMediaPoster()

        # Act
        poster.post_to_social_media(
            "Test Title", "http://example.com", "rea", "myText", "file_name"
        )

        # Assert
        mock_rules_instance.checkRules.assert_called()
        self.assertEqual(mock_api_src.publishPost.call_count, 1)
        mock_api_src.publishPost.assert_called_with(
            "Test Title", "http://example.com", "myText\n\n"
        )


class TestUrlLogger(unittest.TestCase):
    @patch(
        "builtins.open",
        new_callable=unittest.mock.mock_open,
        read_data=b"http://existing.com	Existing Title	...",
    )
    def test_check_and_log_url_duplicate(self, mock_open):
        logger = UrlLogger()
        result = logger.check_and_log_url("http://existing.com", "rea")
        self.assertFalse(result)

    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_check_and_log_url_new(self, mock_open):
        logger = UrlLogger()
        result = logger.check_and_log_url("http://new.com", "rea", "New Title")
        self.assertTrue(result)
        mock_open().write.assert_called()


class TestContentFetcher(unittest.TestCase):
    @patch("requests.get")
    @patch("socialModules.moduleHtml.moduleHtml")
    def test_download_and_clean_content_success(self, mock_html_processor, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.url = "http://example.com"
        mock_response.text = "<html><head><title>Test Title</title></head><body><p>Content</p></body></html>"
        mock_html_processor_instance = MagicMock()
        mock_html_processor_instance.downloadUrl.return_value = (mock_response, None)
        mock_html_processor_instance.cleanDocument.return_value = (
            "<p>Cleaned Content</p>",
            "Test Title",
        )
        mock_html_processor.return_value = mock_html_processor_instance

        fetcher = ContentFetcher()

        # Act
        text_content, title, _, _, res = fetcher.download_and_clean_content(
            "http://example.com", mock_html_processor.return_value
        )

        # Assert
        self.assertEqual(title, "Test Title")
        self.assertEqual(text_content, "<p>Cleaned Content</p>")
        self.assertEqual(res, "Success")
