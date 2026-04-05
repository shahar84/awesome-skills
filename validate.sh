#!/bin/bash
# Validate skills locally before pushing
# Usage:
#   ./validate.sh              # Validate all skills
#   ./validate.sh skill-name   # Validate specific skill

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$SCRIPT_DIR/skills"
VALIDATE_SCRIPT="$SCRIPT_DIR/scripts/validate_skill.py"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Skill Validation"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ ! -f "$VALIDATE_SCRIPT" ]; then
    echo -e "${RED}Error: Validation script not found at $VALIDATE_SCRIPT${NC}"
    exit 1
fi

# Validate specific skill or all skills
if [ $# -eq 1 ]; then
    # Validate single skill
    SKILL_NAME="$1"
    SKILL_PATH="$SKILLS_DIR/$SKILL_NAME"

    if [ ! -d "$SKILL_PATH" ]; then
        echo -e "${RED}Error: Skill not found: $SKILL_NAME${NC}"
        echo "Available skills:"
        ls -1 "$SKILLS_DIR"
        exit 1
    fi

    echo "Validating skill: $SKILL_NAME"
    echo ""

    if python3 "$VALIDATE_SCRIPT" "$SKILL_PATH"; then
        echo ""
        echo -e "${GREEN}✓ Validation passed!${NC}"
        exit 0
    else
        echo ""
        echo -e "${RED}✗ Validation failed${NC}"
        exit 1
    fi
else
    # Validate all skills
    echo "Validating all skills..."
    echo ""

    failed=0
    passed=0

    for skill_dir in "$SKILLS_DIR"/*/; do
        if [ -d "$skill_dir" ]; then
            if python3 "$VALIDATE_SCRIPT" "$skill_dir"; then
                ((passed++))
            else
                ((failed++))
            fi
        fi
    done

    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  Results: $passed passed, $failed failed"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

    if [ $failed -eq 0 ]; then
        echo ""
        echo -e "${GREEN}✓ All skills validated successfully!${NC}"
        exit 0
    else
        echo ""
        echo -e "${RED}✗ Some skills failed validation. Please fix the errors above.${NC}"
        exit 1
    fi
fi
