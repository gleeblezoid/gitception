# gitception

Git in git with git - git it?

##  What's this repo for?

This repo was set up to provide additional resources for folks planning to learn the basics of using version control or run a session for students wishing to do so. It was originally created for a seminar held at Oxford University intended for second year students embarking on a group project.

## Basics of using git

### Setting up git and github

The docs on github provide a fantastic [quickstart guide](https://docs.github.com/en/get-started/quickstart) which you should really check out.

A basic rundown of what's needed though is:

1. Install git on your machine - you can find it [here](https://git-scm.com/downloads) or use your favourite package manager.
1. Set up a global git username: `git config --global user.name "<your username>"`.
1. Set up a global git email: `git config --global user.email "<your email>"`.
1. Go to a repo (maybe use this one) and run a clone using HTTPS (in your command line app of choice): `git clone https://github.com/gleeblezoid/gitception.git` 
1. You'll be prompted for GitHub login details when you do this - when you're prompted for a password you should generate a PAT instead and enter that, you'll need to use [this page](https://github.com/settings/tokens) to generate one if you're not prompted to authenticate using your web browser.

> You can use <https://github.com/git-ecosystem/git-credential-manager> to help with safely storing your credentials.

### Further resources

For more information check out the resources at [skills.github.com](skills.github.com) and [git-scm.com/doc](https://git-scm.com/doc).
