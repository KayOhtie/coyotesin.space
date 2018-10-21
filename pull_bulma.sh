#!/bin/bash
git config core.sparseCheckout true
md -p .git/modules/theme/source/scss/bulma/info
echo "css/*" > .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "sass/*" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "bulma.sass" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "CHANGELOG.md" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "LICENSE" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "package.json" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
echo "README.md" >> .git/modules/theme/source/scss/bulma/info/sparse-checkout
cd theme/source/scss/bulma
# change next tag to current version
git checkout 0.7.2