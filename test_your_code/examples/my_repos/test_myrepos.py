from myrepos import most_watched_repos
import unittest


class TestMyRepos(unittest.TestCase):

    def test_success(self):
        expected_resp = [u'https://github.com/rtnpro/django-pontoon-hook', u'https://github.com/rtnpro/askbot-devel', u'https://github.com/rtnpro/django-cms-bootstrap', u'https://github.com/rtnpro/angular.js', u'https://github.com/rtnpro/Armstrong-IDE', u'https://github.com/rtnpro/darkserver', u'https://github.com/rtnpro/django-bootstrap-toolkit', u'https://github.com/rtnpro/django-bulk', u'https://github.com/rtnpro/django-cms', u'https://github.com/rtnpro/django-filebrowser']
        resp = most_watched_repos('rtnpro', 10)
        self.assertEqual(resp, expected_resp)

