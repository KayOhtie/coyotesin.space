#!/bin/bash
git config core.sparseCheckout true
echo "css/*" > .git/submodules/theme/source/scss/bulma/info/sparse-checkout
echo "sass/*" >> .git/submodules/theme/source/scss/bulma/info/sparse-checkout
echo "bulma.sass" >> .git/submodules/theme/source/scss/bulma/info/sparse-checkout
echo "CHANGELOG.md" >> .git/submodules/theme/source/scss/bulma/info/sparse-checkout
echo "LICENSE" >> .git/submodules/theme/source/scss/bulma/info/sparse-checkout
echo "package.json" >> .git/submodules/theme/source/scss/bulma/info/sparse-checkout
echo "README.md" >> .git/submodules/theme/source/scss/bulma/info/sparse-checkout
cd theme/source/scss/bulma
# change next tag to current version
git checkout 0.7.2