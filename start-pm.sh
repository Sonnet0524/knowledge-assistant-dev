#!/bin/bash
# ====================================
# PM Agent Startup Script
# ====================================

echo ""
echo "========================================"
echo "  PM Agent - Project Manager"
echo "========================================"
echo ""
echo "Working Directory: knowledge-assistant-dev"
echo ""
echo "Starting PM Agent..."
echo ""

# Check if in correct directory
if [ ! -f "opencode.json" ]; then
    echo "Error: opencode.json not found!"
    echo "Please run this script from the dev repository root."
    exit 1
fi

# Start OpenCode with PM agent
opencode --agent pm
