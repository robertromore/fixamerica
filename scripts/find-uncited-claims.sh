#!/bin/bash
#
# find-uncited-claims.sh - Find statements that likely need citations
#
# Usage: ./scripts/find-uncited-claims.sh [directory]
#        Default directory is current directory
#

set -e

# Colors
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

TARGET_DIR="${1:-.}"

echo -e "${YELLOW}Citation Checker${NC}"
echo "Scanning: $TARGET_DIR"
echo "================================"
echo ""

# Function to search and display results
search_pattern() {
    local description="$1"
    local pattern="$2"
    local results

    results=$(grep -rn --include="*.md" -E "$pattern" "$TARGET_DIR" 2>/dev/null | grep -v "citation-guide.md" | grep -v "^\[" || true)

    if [ -n "$results" ]; then
        echo -e "${CYAN}$description${NC}"
        echo "$results" | head -20
        count=$(echo "$results" | wc -l | tr -d ' ')
        if [ "$count" -gt 20 ]; then
            echo "  ... and $((count - 20)) more"
        fi
        echo "  Total: $count"
        echo ""
        return "$count"
    fi
    return 0
}

total=0

echo -e "${YELLOW}=== Statistics Without Citations ===${NC}\n"

# Percentages (e.g., "72% of", "about 30%")
count=$(grep -rn --include="*.md" -E '[0-9]+%' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | wc -l | tr -d ' ')
if [ "$count" -gt 0 ]; then
    echo -e "${CYAN}Percentages:${NC}"
    grep -rn --include="*.md" -E '[0-9]+%' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | head -15
    if [ "$count" -gt 15 ]; then
        echo "  ... and $((count - 15)) more"
    fi
    echo "  Total: $count"
    echo ""
    total=$((total + count))
fi

# Dollar amounts (e.g., "$4 billion", "$2.3 million")
count=$(grep -rn --include="*.md" -E '\$[0-9]+(\.[0-9]+)?\s*(billion|million|trillion|B|M|K)' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | wc -l | tr -d ' ')
if [ "$count" -gt 0 ]; then
    echo -e "${CYAN}Dollar amounts:${NC}"
    grep -rn --include="*.md" -E '\$[0-9]+(\.[0-9]+)?\s*(billion|million|trillion|B|M|K)' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | head -15
    if [ "$count" -gt 15 ]; then
        echo "  ... and $((count - 15)) more"
    fi
    echo "  Total: $count"
    echo ""
    total=$((total + count))
fi

# Large numbers (e.g., "2,500 newspapers", "70 million")
count=$(grep -rn --include="*.md" -E '[0-9]{1,3}(,[0-9]{3})+|[0-9]+\s*(million|billion|thousand)' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | grep -v '\$' | wc -l | tr -d ' ')
if [ "$count" -gt 0 ]; then
    echo -e "${CYAN}Large numbers:${NC}"
    grep -rn --include="*.md" -E '[0-9]{1,3}(,[0-9]{3})+|[0-9]+\s*(million|billion|thousand)' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | grep -v '\$' | head -15
    if [ "$count" -gt 15 ]; then
        echo "  ... and $((count - 15)) more"
    fi
    echo "  Total: $count"
    echo ""
    total=$((total + count))
fi

echo -e "${YELLOW}=== Named Sources Without Citations ===${NC}\n"

# "According to" statements
count=$(grep -rn --include="*.md" -iE 'according to [A-Z]' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | wc -l | tr -d ' ')
if [ "$count" -gt 0 ]; then
    echo -e "${CYAN}\"According to\" statements:${NC}"
    grep -rn --include="*.md" -iE 'according to [A-Z]' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | head -10
    if [ "$count" -gt 10 ]; then
        echo "  ... and $((count - 10)) more"
    fi
    echo "  Total: $count"
    echo ""
    total=$((total + count))
fi

# Research/study references
count=$(grep -rn --include="*.md" -iE '(research|studies|study|survey|poll|data) (shows?|indicates?|found|suggests?|reveals?)' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | wc -l | tr -d ' ')
if [ "$count" -gt 0 ]; then
    echo -e "${CYAN}Research/study references:${NC}"
    grep -rn --include="*.md" -iE '(research|studies|study|survey|poll|data) (shows?|indicates?|found|suggests?|reveals?)' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | head -10
    if [ "$count" -gt 10 ]; then
        echo "  ... and $((count - 10)) more"
    fi
    echo "  Total: $count"
    echo ""
    total=$((total + count))
fi

# Named person observations (e.g., "Smith argued", "Jones observed")
count=$(grep -rn --include="*.md" -E '[A-Z][a-z]+ (argued|observed|noted|wrote|stated|claimed|found|showed|demonstrated|proposed|theorized)' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | wc -l | tr -d ' ')
if [ "$count" -gt 0 ]; then
    echo -e "${CYAN}Named person observations:${NC}"
    grep -rn --include="*.md" -E '[A-Z][a-z]+ (argued|observed|noted|wrote|stated|claimed|found|showed|demonstrated|proposed|theorized)' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | head -10
    if [ "$count" -gt 10 ]; then
        echo "  ... and $((count - 10)) more"
    fi
    echo "  Total: $count"
    echo ""
    total=$((total + count))
fi

echo -e "${YELLOW}=== Legal/Historical References ===${NC}\n"

# Court cases
count=$(grep -rn --include="*.md" -E '[A-Z][a-z]+ v\. [A-Z]' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | wc -l | tr -d ' ')
if [ "$count" -gt 0 ]; then
    echo -e "${CYAN}Court cases:${NC}"
    grep -rn --include="*.md" -E '[A-Z][a-z]+ v\. [A-Z]' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | head -10
    if [ "$count" -gt 10 ]; then
        echo "  ... and $((count - 10)) more"
    fi
    echo "  Total: $count"
    echo ""
    total=$((total + count))
fi

# Named laws/acts with years
count=$(grep -rn --include="*.md" -E '(Act|Law|Amendment|Bill) (of )?[0-9]{4}' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | wc -l | tr -d ' ')
if [ "$count" -gt 0 ]; then
    echo -e "${CYAN}Named laws/acts:${NC}"
    grep -rn --include="*.md" -E '(Act|Law|Amendment|Bill) (of )?[0-9]{4}' "$TARGET_DIR" 2>/dev/null | grep -v '\[\^' | grep -v "citation-guide" | head -10
    if [ "$count" -gt 10 ]; then
        echo "  ... and $((count - 10)) more"
    fi
    echo "  Total: $count"
    echo ""
    total=$((total + count))
fi

echo -e "${YELLOW}=== Summary ===${NC}"
echo ""
echo "Total potential uncited claims found: $total"
echo ""
echo "Note: Not all matches require citations. Review each in context."
echo "      Items in tables, headings, or already cited are filtered where possible."
echo ""
echo "To add citations, see: docs/citation-guide.md"
