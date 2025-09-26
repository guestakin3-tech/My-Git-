from dulwich.web import HTTPGitApplication, PubRepo
from django.conf import settings
import os

def repo_resolver(environ, start_response):
    path = environ.get('PATH_INFO','')
    parts = path.split('/')
    # expecting /git/<owner>/<repo>.git/...
    if len(parts) >= 4 and parts[1] == 'git':
        owner = parts[2]
        repo_name = parts[3]
        repo_path = os.path.join(settings.GIT_REPOS_ROOT, owner, repo_name)
        if os.path.exists(repo_path):
            return PubRepo(repo_path)
    return None

git_app = HTTPGitApplication(repo_resolver)
