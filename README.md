Use below for cloning

```
git git@github.com:Ceralor/coyotesin.space.git --depth=1 --shallow-submodules --recursive
cd coyotesin.space
./pull_bulma.sh
```

Still need to also create the py3 virtualenv

```
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

~~Now all set and can use `make devserver` to start the auto-updating dev server.~~ Scratch, mid-upgrade to newest Pelican build.

Also a lot of this is now out of date.