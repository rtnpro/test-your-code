from myrepos import most_watched_repos, sort_response_json
import unittest
import mock


class TestMyRepos(unittest.TestCase):

    def test_success(self):
        expected_resp = [u'https://github.com/rtnpro/django-pontoon-hook', u'https://github.com/rtnpro/askbot-devel', u'https://github.com/rtnpro/django-cms-bootstrap', u'https://github.com/rtnpro/angular.js', u'https://github.com/rtnpro/Armstrong-IDE', u'https://github.com/rtnpro/darkserver', u'https://github.com/rtnpro/django-bootstrap-toolkit', u'https://github.com/rtnpro/django-bulk', u'https://github.com/rtnpro/django-cms', u'https://github.com/rtnpro/django-filebrowser']
        resp = most_watched_repos('rtnpro', 10)
        self.assertEqual(resp, expected_resp)


class TestMockedMyRepos(unittest.TestCase):

    @mock.patch('myrepos.requests.get')
    def test_success(self, mock_requests_get):
        m = mock.Mock()
        m.content = '[{"watchers": 0, "html_url": "foo"}, {"watchers": 4, "html_url": "foobar"}, {"watchers": 1, "html_url": "blah"}]'
        mock_requests_get.return_value = m
        resp = most_watched_repos('blah', 10)
        self.assertEqual(resp, ["foobar", "blah", "foo"])


class TestRefactoredMyRepos(unittest.TestCase):

    def test_success(self):
        resp_json = '[{"watchers": 0, "html_url": "foo"}, {"watchers": 4, "html_url": "foobar"}, {"watchers": 1, "html_url": "blah"}]'
        self.assertEqual(sort_response_json(resp_json, 10), ["foobar", "blah", "foo"])
