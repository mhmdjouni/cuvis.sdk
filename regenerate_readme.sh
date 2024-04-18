#!/bin/sh

# Navigate to the repository root
cd $(git rev-parse --show-toplevel)

cat readme/logo.md > README.md
echo "# cuvis.sdk\n" >> README.md
cat readme/header.md >> README.md
echo "\n" >> README.md
cat README.in >> README.md
cat readme/footer.md >> README.md
