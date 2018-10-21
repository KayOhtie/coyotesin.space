Use below for cloning

```
git clone git@coding.coyotesin.space:kay/coyotesin.space.git --depth=1 --shallow-submodules --recursive
cd coyotesin.space
./pull_bulma.sh
```

Still need to also create the py3 virtualenv

```
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

Now all set and can use `make devserver` to start the auto-updating dev server.