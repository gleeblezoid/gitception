# gitception

Git in git with git - git it?

Check out more information at [skills.github.com](skills.github.com) and [git-scm.com/doc](https://git-scm.com/doc
).

## Setting up your gogs repo in macOS

1. Install docker desktop and the docker command line tools.

2. Clone this repo

3. `cd` to the repo folder and run the following:

```sh
docker pull gogs/gogs
docker run -d --name=gogs -p 10070:3000 -v gog-data:/data gogs/gogs
```

4. Your container should be running now - go to `localhost:10070` to set up your server.

> I disabled SSH because it seemed pretty unecessary.

Starting gogs:

```sh
docker start gogs
```

Stopping gogs:

```sh
docker stop gogs
```

## Using the sample site

1. Create a repo in your gogs server called something useful - I used `potato`
2. `git clone` your repo to somewhere in your local filesystem
3. Copy the files from the `sample site` folder into your `potato` (or equivalent) repo folder
4. Do the `git add`,`git commit`, `git push` dance to update your gogs repo
5. Run your site with `python3 app.py`
6. Access your site on `localhost:8080`
7. Mess around with it or simply admire your local version controlled potatoes
