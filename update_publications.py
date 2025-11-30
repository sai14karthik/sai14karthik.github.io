#!/usr/bin/env python3
"""
Script to update publications from Google Scholar BibTeX export.

How to use:
1. Go to your Google Scholar profile: https://scholar.google.com/citations?user=HtJ7Q64AAAAJ
2. Click "Export" → "BibTeX"
3. Save the file as "publications.bib" in this directory
4. Run: python3 update_publications.py
5. The script will update index.html with your publications
"""

import re
from datetime import datetime

def parse_bibtex(bibtex_file):
    """Parse BibTeX file and extract publication information."""
    publications = []
    
    with open(bibtex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by @ entries
    entries = re.split(r'@\w+\{', content)[1:]  # Skip first empty part
    
    for entry in entries:
        pub = {}
        
        # Extract entry type and key
        match = re.match(r'([^,]+),', entry)
        if match:
            pub['key'] = match.group(1).strip()
        
        # Extract title
        title_match = re.search(r'title\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE)
        if title_match:
            pub['title'] = title_match.group(1).strip()
        
        # Extract authors
        author_match = re.search(r'author\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE)
        if author_match:
            authors = author_match.group(1).strip()
            # Split by 'and'
            pub['authors'] = [a.strip() for a in authors.split(' and ')]
        
        # Extract year
        year_match = re.search(r'year\s*=\s*\{?(\d{4})\}?', entry, re.IGNORECASE)
        if year_match:
            pub['year'] = year_match.group(1)
        
        # Extract venue/journal
        venue_match = re.search(r'(?:booktitle|journal|venue)\s*=\s*\{([^}]+)\}', entry, re.IGNORECASE)
        if venue_match:
            pub['venue'] = venue_match.group(1).strip()
        
        # Determine type
        if 'inproceedings' in entry.lower() or 'conference' in entry.lower():
            pub['type'] = 'C'
        elif 'article' in entry.lower():
            pub['type'] = 'J'
        elif 'patent' in entry.lower():
            pub['type'] = 'P'
        else:
            pub['type'] = 'C'  # Default to conference
        
        if pub.get('title'):
            publications.append(pub)
    
    return publications

def generate_html(publications, your_name_variations=['Sai Karthik', 'SK Nallamothu', 'Sai Karthik Nallamothu']):
    """Generate HTML for publications section."""
    html_parts = []
    
    # Filter and sort: conferences first, then by year (newest first)
    conferences = [p for p in publications if p.get('type') == 'C']
    conferences.sort(key=lambda x: int(x.get('year', 0)), reverse=True)
    
    for idx, pub in enumerate(conferences, 1):
        title = pub.get('title', '')
        authors = pub.get('authors', [])
        year = pub.get('year', '')
        venue = pub.get('venue', '')
        
        # Highlight your name
        author_html = []
        for author in authors:
            # Check if this is your name (case-insensitive, partial match)
            is_you = any(variation.lower() in author.lower() or author.lower() in variation.lower() 
                        for variation in your_name_variations)
            
            if is_you:
                author_html.append(f'<span class="author-name">{author}</span>')
            else:
                author_html.append(f'<span class="author-other">{author}</span>')
        
        authors_str = ', '.join(author_html)
        
        html = f'''                <p>
                  <strong>[C.{idx}]</strong> <strong>{title}</strong>.<br>
                  {authors_str}.<br>
                  In <em>{venue}</em>, {year}.
                </p>'''
        
        html_parts.append(html)
    
    return '\n'.join(html_parts)

def update_index_html(html_content):
    """Update the publications section in index.html."""
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the publications section
    # Pattern: from <h2>Publications</h2> to the closing </td> of that section
    pattern = r'(<h2>Publications</h2>.*?</td>\s*</tr>\s*<tr>\s*<td[^>]*>)(.*?)(</td>\s*</tr>)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        before = match.group(1)
        after = match.group(3)
        
        new_content = before + '\n                <p style="font-size:12px;color:#666;margin-bottom:15px;"><em>C=Conference</em></p>\n' + html_content + '\n              ' + after
        
        content = content[:match.start()] + new_content + content[match.end():]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Successfully updated index.html with publications!")
    else:
        print("❌ Could not find Publications section in index.html")

if __name__ == '__main__':
    import sys
    
    bibtex_file = 'publications.bib'
    
    if len(sys.argv) > 1:
        bibtex_file = sys.argv[1]
    
    try:
        print(f"Reading BibTeX file: {bibtex_file}")
        publications = parse_bibtex(bibtex_file)
        print(f"Found {len(publications)} publications")
        
        html = generate_html(publications)
        update_index_html(html)
        
        print("\n📝 Next steps:")
        print("1. Review the updated index.html")
        print("2. Commit and push: git add index.html && git commit -m 'Update publications' && git push")
        
    except FileNotFoundError:
        print(f"❌ Error: {bibtex_file} not found!")
        print("\n📋 How to export from Google Scholar:")
        print("1. Go to: https://scholar.google.com/citations?user=HtJ7Q64AAAAJ")
        print("2. Click 'Export' button (at the top)")
        print("3. Select 'BibTeX'")
        print("4. Save the file as 'publications.bib' in this directory")
        print("5. Run this script again")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

