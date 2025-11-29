# GitHub Pages Deployment Guide

## How to Enable and Configure GitHub Pages

### Step-by-Step Instructions

1. **Navigate to Your Repository**
   - Go to: https://github.com/sai14karthik/sai14karthik.github.io

2. **Open Settings**
   - Click on the **"Settings"** tab (located at the top of the repository, next to "Code", "Issues", "Pull requests", etc.)

3. **Go to Pages Section**
   - In the left sidebar, scroll down and click on **"Pages"** (under "Code and automation" section)

4. **Configure Source**
   - Under the **"Source"** section, you'll see a dropdown menu
   - Click on the dropdown and select **"Deploy from a branch"**
   - This is the option you want (NOT "GitHub Actions")

5. **Select Branch and Folder**
   - After selecting "Deploy from a branch", you'll see two more dropdowns:
     - **Branch**: Select **"main"** (or "master" if that's your default branch)
     - **Folder**: Select **"/ (root)"**
   - Click **"Save"**

6. **Wait for Deployment**
   - After saving, GitHub will show a message: "Your site is ready to be published at https://sai14karthik.github.io/"
   - It may take 5-10 minutes for the site to be live
   - You can check the deployment status at the top of the Pages settings page

### Visual Guide

```
Repository → Settings → Pages
                          ↓
                    Source: [Deploy from a branch ▼]
                              ↓
                    Branch: [main ▼]
                    Folder: [/ (root) ▼]
                              ↓
                         [Save]
```

### Verification

After saving, you should see:
- ✅ A green checkmark or "Your site is live at https://sai14karthik.github.io/"
- A deployment status indicator showing the latest deployment

### Troubleshooting

**If you don't see "Deploy from a branch" option:**
- Make sure you're the repository owner or have admin access
- The repository must be public (or you need GitHub Pro for private repos)

**If the site doesn't load after 10 minutes:**
- Check the Actions tab to see if there are any build errors
- Verify that `index.html` is in the root of your repository
- Make sure the branch name matches (main vs master)

**If you see "404 Not Found":**
- Wait a few more minutes (first deployment can take longer)
- Clear your browser cache
- Try accessing in incognito/private mode

### Quick Check

To verify your Pages is configured correctly:
1. Go to: https://github.com/sai14karthik/sai14karthik.github.io/settings/pages
2. You should see:
   - Source: "Deploy from a branch"
   - Branch: "main" / "/ (root)"
   - A green checkmark or deployment status

