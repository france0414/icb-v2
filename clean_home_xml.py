import re
import os

def clean_pass2(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    original_count = len(lines)
    new_lines = []
    skip_until_banner = False
    found_wrap = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # For each file: keep lines 1-4 (t-name, t-call, t-set, div#wrap)
        # Then skip everything until the first real content section (s_carousel_wrapper or similar)
        if i < len(lines):
            # Check if this is the wrap div opening
            if 'id="wrap"' in line:
                found_wrap = True
                new_lines.append(line)
                skip_until_banner = True
                continue
            
            if skip_until_banner:
                # Look for the first real content section (carousel/banner)
                if ('s_carousel_wrapper' in line or 
                    's_custom_banner' in line or
                    (stripped.startswith('<section') and 'data-snippet="s_vertical_layout"' in line and '整頁複製' not in line and '標題' not in line and 'pt32 pb16' not in line)):
                    skip_until_banner = False
                    new_lines.append(line)
                    continue
                else:
                    continue  # Skip instruction section lines
            
            new_lines.append(line)
    
    # Clean up orphaned empty lines
    content = ''.join(new_lines)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_count = content.count('\n')
    removed = original_count - new_count
    print(f"{os.path.basename(filepath)}: {original_count} -> {new_count} lines (removed {removed})")

base = r'D:\gemini\odoo\templates'
for fname in ['home-1.xml', 'home-2.xml', 'home-3.xml', 'home-4.xml']:
    fpath = os.path.join(base, fname)
    if os.path.exists(fpath):
        clean_pass2(fpath)
