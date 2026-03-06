#!/bin/bash
# ====================================
# Agent Test Startup Script
# ====================================

echo ""
echo "========================================"
echo "  Agent Test - Quality Assurance"
echo "========================================"
echo ""
echo "Working Directory: knowledge-assistant"
echo ""
echo "Starting Agent Test..."
echo ""

# Check if we need to switch to main repo
if [ -d "../knowledge-assistant" ]; then
    echo "Switching to main repository..."
    cd ../knowledge-assistant
fi

# Check if in correct directory
if [ ! -d "tests" ]; then
    echo "Error: Not in main repository!"
    echo "Please run this script when knowledge-assistant repo is available."
    exit 1
fi

# Start OpenCode with Agent Test
opencode --agent test
