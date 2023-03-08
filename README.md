# gitception

Git in git with git - git it?

##  What's this repo for?

This repo was set up to provide additional resources for folks planning to learn the basics of using version control or run a session for students wishing to do so. It was originally created for a seminar held at Oxford University intended for second year students embarking on a group project.

## Basics of version control

### Setting up git and github

The docs on github provide a fantastic [quickstart guide](https://docs.github.com/en/get-started/quickstart) which you should really check out.

A basic rundown of what's needed though is:

1. Install git on your machine - you can find it [here](https://git-scm.com/downloads) or use your favourite package manager.
1. Set up a global git username: `git config --global user.name "<your username>"`.
1. Set up a global git email: `git config --global user.email "<your email>"`.
1. Go to a repo (maybe use this one) and run a clone using HTTPS (in your command line app of choice): `git clone https://github.com/gleeblezoid/gitception.git` 
1. You'll be prompted for GitHub login details when you do this - when you're prompted for a password you should generate a PAT instead and enter that, you'll need to use [this page](https://github.com/settings/tokens) to generate one if you're not prompted to authenticate using your web browser.

> You can use <https://github.com/git-ecosystem/git-credential-manager> to help with safely storing your credentials.

### Covering the basics in an hour

This section is intended for folks wanting a summary of the seminar contents or run their own session about version control.

#### Git Core Concepts

Some technical fundamentals that will help git make more sense.

##### Repositories and Commits

- Repositories are folders with change tracking (have a look in the `.git` folder of a local repo).
- Running `git clone` to copy down a remote repository creates a repo on your machine with git configuration.
- You can have many local repos for a given remote repo.
- Commits are changes tracked using git, git keeps a unique ID for every commit you make and you can use that to do all kinds of things.

##### Branches and HEAD

- A branch is just a reference to a specific commit and a history of other logged commits.
- Creating and working from branches protects your main codebase and makes splitting work easier.
- HEAD is just the commit you’re working from in the moment, you can check what it is locally from the HEAD text file in your .git/ folder (if you wanted to “go back in time” to a previous commit then `git reset --hard HEAD~2` would reset your branch to 2 commits ago).

> For relatively small group project a feature workflow is probably the best to use - if you've worked on a larger OSS project you might have encountered a forking workflow.



### Further resources

For more information check out the resources at [skills.github.com](skills.github.com) and [git-scm.com/doc](https://git-scm.com/doc).

If you're planning to run a locally hosted git demo check out this repo's doc on configuring a gogs server [here](https://github.com/gleeblezoid/gitception/blob/884ae2bdfb218b87331511acf3b2e0b7671bc01e/docs/setting_up_a_gogs_demo_server.md).

There's also a sample Flask site [here](https://github.com/gleeblezoid/gitception/blob/884ae2bdfb218b87331511acf3b2e0b7671bc01e/sample-site) if you want something to play around with - you'll need python3, pipenv, and pre-commit installed.
