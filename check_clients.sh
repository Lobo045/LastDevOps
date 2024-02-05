#!/bin/bash

# Check if there are changes to commit
if git diff-index --quiet HEAD --; then
    echo "No changes to commit."
    exit 0
fi

# Commit changes to the main branch
git add .
git commit -m "Committing changes to main branch"

# Push changes to the main branch
#!/bin/bash

# Check if there are changes to commit
if git diff-index --quiet HEAD --; then
    echo "No changes to commit."
    exit 0
fi

# Commit changes to the main branch
git add .
git commit -m "Committing changes to main branch"

# Push changes to the main branch
git push origin main

echo "Changes committed and pushed to main branch successfully."

