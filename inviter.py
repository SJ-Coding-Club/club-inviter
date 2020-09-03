from github import Github
import os
import time
g = Github(os.environ.get('GITHUB_EMAIL'),os.environ.get('GITHUB_PASSWORD'))
club = g.get_organization('SJ-Coding-Club')
while True:
    for issue in club.get_repo('sj-coding-club.github.io').get_issues():
        if 'add me' in issue.title.lower():
            if issue.user.login not in [x.login for x in club.get_members()]:
                club.invite_user(user=issue.user)
            else:
                issue.edit(state='closed')
    time.sleep(15)            
