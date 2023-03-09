# Setting up a demo git server with gogs

If you want to demonstrate version control but won't have access to the Internet when you do then this setup might work well for you. Gogs is a lightweight git server you can run in a docker container.

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
1. `git clone` your repo to somewhere in your local filesystem
1. Copy the files from the `sample site` folder into your `potato` (or equivalent) repo folder
1. Do the `git add`,`git commit`, `git push` dance to update your gogs repo
1. Run your site with `python3 app.py`
1. Access your site on `localhost:8080`
1. Mess around with it or simply admire your local version controlled potatoes
