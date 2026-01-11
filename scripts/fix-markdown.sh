#!/bin/bash
#
# fix-markdown.sh - Automatically fix markdown linting issues
#
# Usage: ./scripts/fix-markdown.sh [directory]
#        Default directory is current directory
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default to current directory
TARGET_DIR="${1:-.}"

echo -e "${YELLOW}Markdown Lint Fixer${NC}"
echo "Target: $TARGET_DIR"
echo "================================"

# Check if markdownlint is installed
if ! command -v markdownlint &> /dev/null; then
    echo -e "${RED}Error: markdownlint-cli is not installed${NC}"
    echo "Install with: npm install -g markdownlint-cli"
    exit 1
fi

# Check if python3 is available
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: python3 is not installed${NC}"
    exit 1
fi

# Count initial errors
echo -e "\n${YELLOW}Step 1: Checking initial state...${NC}"
INITIAL_ERRORS=$(markdownlint "$TARGET_DIR/**/*.md" "$TARGET_DIR/*.md" 2>&1 | wc -l | tr -d ' ')
echo "Initial errors: $INITIAL_ERRORS"

if [ "$INITIAL_ERRORS" -eq 0 ]; then
    echo -e "${GREEN}No errors found. All files are compliant!${NC}"
    exit 0
fi

# Run Python structural fixes
echo -e "\n${YELLOW}Step 2: Running structural fixes (blank lines, code blocks)...${NC}"

python3 << 'PYTHON_SCRIPT'
import os
import re
import glob
import sys

def fix_markdown_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  Warning: Could not read {filepath}: {e}")
        return False

    original_content = content
    lines = content.split('\n')
    fixed_lines = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        prev_line = lines[i-1].strip() if i > 0 else ''
        next_line = lines[i+1].strip() if i + 1 < len(lines) else ''

        # Check if we need a blank line BEFORE this line
        need_blank_before = False

        # Heading needs blank line before (unless at start or after blank)
        if stripped.startswith('#') and prev_line and not prev_line.startswith('#'):
            need_blank_before = True

        # List item needs blank line before if previous is not blank/list/heading/bold
        if (stripped.startswith('- ') or re.match(r'^\d+\.', stripped)):
            if prev_line and not prev_line.startswith('-') and not prev_line.startswith('#') and not re.match(r'^\d+\.', prev_line) and not re.match(r'^\*\*[^*]+\*\*$', prev_line):
                need_blank_before = True

        # Table needs blank line before if previous is not blank/table/bold
        if stripped.startswith('|') and prev_line and not prev_line.startswith('|') and not re.match(r'^\*\*[^*]+\*\*$', prev_line):
            need_blank_before = True

        # Code block needs blank line before
        if stripped.startswith('```') and prev_line and not prev_line.startswith('```'):
            need_blank_before = True

        # Add blank line before if needed and not already there
        if need_blank_before and fixed_lines and fixed_lines[-1].strip():
            fixed_lines.append('')

        # Fix code blocks without language specifier
        if stripped == '```':
            # Check if this is likely an opening block (not closing)
            # by checking if there's content after it before the next ```
            is_opening = False
            for j in range(i + 1, min(i + 20, len(lines))):
                if lines[j].strip() == '```':
                    is_opening = True
                    break
                if lines[j].strip():
                    is_opening = True
            if is_opening and (not fixed_lines or not fixed_lines[-1].strip().startswith('```')):
                fixed_lines.append('```text')
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)

        # Check if we need a blank line AFTER this line
        need_blank_after = False

        # Bold label followed by list/table needs blank line
        if re.match(r'^\*\*[^*]+\*\*$', stripped):
            if next_line and (next_line.startswith('-') or next_line.startswith('|') or re.match(r'^\d+\.', next_line)):
                need_blank_after = True

        # Heading needs blank line after (if next is not blank/heading)
        if stripped.startswith('#') and next_line and not next_line.startswith('#'):
            need_blank_after = True

        if need_blank_after and next_line:
            fixed_lines.append('')

    # Remove multiple consecutive blank lines
    final = []
    prev_blank = False
    for line in fixed_lines:
        if line.strip() == '':
            if not prev_blank:
                final.append(line)
            prev_blank = True
        else:
            final.append(line)
            prev_blank = False

    new_content = '\n'.join(final)

    # Preserve trailing newline state
    if original_content.endswith('\n') and not new_content.endswith('\n'):
        new_content += '\n'
    elif not original_content.endswith('\n') and new_content.endswith('\n'):
        new_content = new_content.rstrip('\n')

    if new_content != original_content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
        except Exception as e:
            print(f"  Warning: Could not write {filepath}: {e}")
            return False
    return False

# Get target directory from environment or use current
target_dir = os.environ.get('TARGET_DIR', '.')

# Find all markdown files
patterns = [
    os.path.join(target_dir, '**', '*.md'),
    os.path.join(target_dir, '*.md')
]

files_fixed = 0
files_checked = 0

for pattern in patterns:
    for filepath in glob.glob(pattern, recursive=True):
        files_checked += 1
        if fix_markdown_file(filepath):
            files_fixed += 1
            print(f"  Fixed: {filepath}")

print(f"\nStructural fixes: {files_fixed} files modified out of {files_checked} checked")
PYTHON_SCRIPT

# Run markdownlint --fix for additional auto-fixes
echo -e "\n${YELLOW}Step 3: Running markdownlint --fix...${NC}"
markdownlint --fix "$TARGET_DIR/**/*.md" "$TARGET_DIR/*.md" 2>/dev/null || true

# Check remaining errors
echo -e "\n${YELLOW}Step 4: Checking remaining issues...${NC}"
REMAINING_ERRORS=$(markdownlint "$TARGET_DIR/**/*.md" "$TARGET_DIR/*.md" 2>&1 | wc -l | tr -d ' ')

if [ "$REMAINING_ERRORS" -eq 0 ]; then
    echo -e "${GREEN}All errors fixed! Files are now compliant.${NC}"
    echo -e "\nSummary:"
    echo "  Initial errors: $INITIAL_ERRORS"
    echo "  Remaining errors: 0"
    echo -e "  ${GREEN}All fixed!${NC}"
else
    echo -e "${YELLOW}Some errors could not be auto-fixed:${NC}"
    markdownlint "$TARGET_DIR/**/*.md" "$TARGET_DIR/*.md" 2>&1 | head -20

    if [ "$REMAINING_ERRORS" -gt 20 ]; then
        echo "... and $((REMAINING_ERRORS - 20)) more"
    fi

    echo -e "\nSummary:"
    echo "  Initial errors: $INITIAL_ERRORS"
    echo "  Remaining errors: $REMAINING_ERRORS"
    echo "  Fixed: $((INITIAL_ERRORS - REMAINING_ERRORS))"
    echo -e "\n${YELLOW}Manual fixes may be required for remaining issues.${NC}"
fi

exit 0
