# gitception

Git in git with git - git it?

Setting up in your gogs folder:

```sh
docker pull gogs/gogs
mkdir gog-data
docker run -d --name=gogs -p 10070:3000 -v gog-data:/data gogs/gogs
```

Starting gogs:

```sh
docker start gogs
```

Stopping gogs:

```sh
docker stop gogs
```
