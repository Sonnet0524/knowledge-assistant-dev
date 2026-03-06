#!/bin/bash
# ====================================
# Template Agent Startup Script
# ====================================

echo ""
echo "========================================"
echo "  Template Agent - Template System"
echo "========================================"
echo ""
echo "Working Directory: knowledge-assistant"
echo ""
echo "Starting Template Agent..."
echo ""

# Check if we need to switch to main repo
if [ -d "../knowledge-assistant" ]; then
    echo "Switching to main repository..."
    cd ../knowledge-assistant
fi

# Check if in correct directory
if [ ! -d "scripts" ]; then
    echo "Error: Not in main repository!"
    echo "Please run this script when knowledge-assistant repo is available."
    exit 1
fi

# Start OpenCode with Template agent
opencode --agent template
