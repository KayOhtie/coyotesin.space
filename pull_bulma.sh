#!/bin/bash
# change next tag to current version
version="0.7.2"
# don't change
mkdir -p .git/modules/theme/source/scss/bulma/info 2>/dev/null
echo "css/*" > .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "sass/*" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "bulma.sass" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "CHANGELOG.md" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "LICENSE" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "package.json" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "README.md" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
cd theme/source/scss/bulma
git config core.sparseCheckout true
git fetch
git checkout $version
