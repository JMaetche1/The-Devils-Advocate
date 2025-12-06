#!/bin/bash
# Quick launch script for Mac/Linux

echo "Starting The Devil's Advocate..."
echo ""

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Launch Streamlit
streamlit run main.py


