# How to Auto-Update Publications from Google Scholar

## Quick Method (Recommended)

### Step 1: Export from Google Scholar

1. Go to your Google Scholar profile: https://scholar.google.com/citations?user=HtJ7Q64AAAAJ
2. Click the **"Export"** button (usually at the top right or in a menu)
3. Select **"BibTeX"** format
4. Save the file as `publications.bib` in your Portfolio folder

### Step 2: Run the Update Script

```bash
cd /Users/saikarthik/Desktop/Portfolio
python3 update_publications.py
```

### Step 3: Review and Commit

1. Check `index.html` to see the updated publications
2. Commit and push:
```bash
git add index.html
git commit -m "Update publications from Google Scholar"
git push
```

## How It Works

The script:
- ✅ Parses your BibTeX export from Google Scholar
- ✅ Automatically detects your name and highlights it (red/yellow)
- ✅ Formats other authors in blue/orange-yellowish
- ✅ Sorts publications by year (newest first)
- ✅ Updates the HTML automatically

## Your Name Variations

The script looks for these name variations:
- "Sai Karthik"
- "SK Nallamothu"  
- "Sai Karthik Nallamothu"

If you use different variations in Google Scholar, you can edit `update_publications.py` and update the `your_name_variations` list.

## Alternative: Manual Update

If you prefer to update manually:
1. Export BibTeX from Google Scholar
2. Use an online BibTeX to HTML converter
3. Copy and paste into `index.html`

## Troubleshooting

**If the script doesn't find your name:**
- Check the BibTeX file to see how your name appears
- Update the `your_name_variations` list in the script

**If publications are in wrong order:**
- The script sorts by year (newest first)
- You can manually reorder in the HTML if needed

**If some publications are missing:**
- Make sure all publications are included in the BibTeX export
- Check that the BibTeX format is correct

## Future Updates

Whenever you add a new publication to Google Scholar:
1. Export BibTeX again
2. Run the script
3. Commit and push

That's it! Your website will always be up to date! 🎉

