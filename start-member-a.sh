#!/bin/bash
# ====================================
# Agent A Startup Script
# ====================================

echo ""
echo "========================================"
echo "  Agent A - Template System Developer"
echo "========================================"
echo ""
echo "Working Directory: knowledge-assistant"
echo ""
echo "Starting Agent A..."
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

# Start OpenCode with Agent A
opencode --agent member-a
