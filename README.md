# YPclutter
remake of yanPython folder

放置一些小型项目的笔记/优化版本



使用Twitter的

<table>
  <tr>
  <td align="center">
        <a href="https://github.com/yanfd/YPclutter/blob/main/twitter_new.py">
            <sub><b>Twitter_new</b></sub>
        </a>
</td>
  </tr>
</table>

```
git filter-branch --env-filter '
OLD_EMAIL=<旧邮箱地址>
CORRECT_NAME=<正确用户名>
CORRECT_EMAIL=<正确邮箱地址>
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_COMMITTER_NAME="$CORRECT_NAME"
export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_AUTHOR_NAME="$CORRECT_NAME"
export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi' --tag-name-filter cat -- --branches --tags
```

```
git config --global user.name yanfd
git config --global user.email 2453317080@qq.com
```

```
git filter-branch --env-filter '
OLD_EMAIL=202322430614
CORRECT_NAME=yanfd
CORRECT_EMAIL=2453317080@qq.com
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_COMMITTER_NAME="$CORRECT_NAME"
export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_AUTHOR_NAME="$CORRECT_NAME"
export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi' --tag-name-filter cat -- --branches --tags
```

