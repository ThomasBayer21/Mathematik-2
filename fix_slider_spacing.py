#!/usr/bin/env python3
"""Fix slider spacing in all HTML files"""

import re
import glob

files_to_check = [
    '10_Hauptsatz_DiffInt.html',
    '11_Potenzreihen_Taylor.html',
    '12_Fourier_Reihen.html',
    '13_Anfangswert_Randwert.html',
    '15_3D_Funktionen_Hoehenlinien.html',
    '18_Bogenlaenge.html',
    '19_Flaechenintegral.html',
    '1_Riemann_Summen.html',
    '20_Integralfunktion.html',
    '21_Partielle_Integration.html',
    '22_Rotationskoerper_Oberflaeche.html',
    '23_Uneigentliche_Integrale.html',
    '3_Numerische_Methoden_Vergleich.html',
    '4_Substitution_Visualisierung.html',
    '5_Schwingungen_2_Ordnung.html',
    '7_Volumenintegral.html',
    '8_Flaeche_Zwischen_Funktionen.html',
    '9_Negative_Flaechen.html'
]

def fix_spacing(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix .controls gap from 15px to 30px
    content = re.sub(
        r'(\.controls\s*\{[^}]*?gap:\s*)15px',
        r'\g<1>30px',
        content,
        flags=re.DOTALL
    )

    # Ensure label has good margin-bottom (at least 8px)
    content = re.sub(
        r'(label\s*\{[^}]*?margin-bottom:\s*)5px',
        r'\g<1>10px',
        content,
        flags=re.DOTALL
    )

    # Add margin-top to input[type="range"] if not present
    # First, check if input[type="range"] exists and has margin-top
    range_pattern = r'input\[type="range"\]\s*\{[^}]*?\}'
    range_match = re.search(range_pattern, content, re.DOTALL)

    if range_match:
        range_block = range_match.group(0)
        if 'margin-top' not in range_block:
            # Add margin-top before the closing brace
            new_range_block = range_block.replace('}', '            margin-top: 8px;\n        }')
            content = content.replace(range_block, new_range_block)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Fixed: {filepath}")
        return True
    else:
        print(f"  Skipped (no changes needed): {filepath}")
        return False

fixed_count = 0
for filepath in files_to_check:
    try:
        if fix_spacing(filepath):
            fixed_count += 1
    except Exception as e:
        print(f"✗ Error in {filepath}: {e}")

print(f"\n{fixed_count} file(s) fixed!")
