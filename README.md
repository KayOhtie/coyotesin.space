# Coyotes In Space website

## Cloning

```
git clone git@github.com:Ceralor/coyotesin.space.git --depth=1 --shallow-submodules --recursive
cd coyotesin.space
python -m virtualenv .venv
```

Then:
 - on Linux: `. .venv/bin/activate`
 - on Windows: `. .venv\scripts\activate.ps1`

```
pip install -r requirements.txt
npm install
```

## Dev

For working on previewing updates, `invoke clean livereload`

## Publish

To publish updated site, `invoke clean gh-pages`
