#!/usr/bin/env bash

# =============================================================================
# Rite Documentation Build Script
# =============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}===========================================${NC}"
echo -e "${GREEN}  Rite Documentation Builder${NC}"
echo -e "${GREEN}===========================================${NC}"
echo ""

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
DOC_DIR="$PROJECT_ROOT/doc"
BUILD_DIR="$DOC_DIR/_build"

# Parse arguments
BUILD_TYPE="${1:-mkdocs}"
SERVE="${2:-false}"

# Function to build with MkDocs
build_mkdocs() {
    echo -e "${YELLOW}Building documentation with MkDocs...${NC}"

    cd "$PROJECT_ROOT"

    if command -v mkdocs &> /dev/null; then
        mkdocs build --clean
        echo -e "${GREEN}✓ MkDocs build complete${NC}"
        echo -e "  Output: site/"

        if [ "$SERVE" = "serve" ]; then
            echo -e "${YELLOW}Starting MkDocs server...${NC}"
            mkdocs serve
        fi
    else
        echo -e "${RED}✗ MkDocs not found${NC}"
        echo -e "  Install with: pip install -r requirements-docs.txt"
        exit 1
    fi
}

# Function to build with Sphinx
build_sphinx() {
    echo -e "${YELLOW}Building documentation with Sphinx...${NC}"

    cd "$DOC_DIR"

    if command -v sphinx-build &> /dev/null; then
        # Clean build directory
        rm -rf "$BUILD_DIR"
        mkdir -p "$BUILD_DIR"

        # Build HTML
        sphinx-build -b html . "$BUILD_DIR/html"

        echo -e "${GREEN}✓ Sphinx build complete${NC}"
        echo -e "  Output: doc/_build/html/"

        if [ "$SERVE" = "serve" ]; then
            echo -e "${YELLOW}Starting local server...${NC}"
            cd "$BUILD_DIR/html"
            python3 -m http.server 8000
        fi
    else
        echo -e "${RED}✗ Sphinx not found${NC}"
        echo -e "  Install with: pip install -r requirements-docs.txt"
        exit 1
    fi
}

# Function to build API documentation with sphinx-apidoc
build_api_docs() {
    echo -e "${YELLOW}Generating API documentation...${NC}"

    if command -v sphinx-apidoc &> /dev/null; then
        sphinx-apidoc -f -o "$DOC_DIR/api_generated" "$PROJECT_ROOT/src/rite"
        echo -e "${GREEN}✓ API documentation generated${NC}"
    else
        echo -e "${RED}✗ sphinx-apidoc not found${NC}"
        exit 1
    fi
}

# Main execution
case "$BUILD_TYPE" in
    mkdocs)
        build_mkdocs
        ;;
    sphinx)
        build_sphinx
        ;;
    api)
        build_api_docs
        ;;
    all)
        build_api_docs
        build_sphinx
        build_mkdocs
        ;;
    *)
        echo -e "${RED}Unknown build type: $BUILD_TYPE${NC}"
        echo ""
        echo "Usage: $0 [mkdocs|sphinx|api|all] [serve]"
        echo ""
        echo "Examples:"
        echo "  $0 mkdocs          # Build MkDocs documentation"
        echo "  $0 mkdocs serve    # Build and serve MkDocs"
        echo "  $0 sphinx          # Build Sphinx documentation"
        echo "  $0 sphinx serve    # Build and serve Sphinx"
        echo "  $0 api             # Generate API documentation"
        echo "  $0 all             # Build everything"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}===========================================${NC}"
echo -e "${GREEN}  Documentation build complete!${NC}"
echo -e "${GREEN}===========================================${NC}"
