#!/bin/bash

# GitHub repository details
OWNER="Koh84"
REPO="ai_daily_news"

# Check if GITHUB_TOKEN is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Error: Please set the GITHUB_TOKEN environment variable."
    echo "Create a personal access token at https://github.com/settings/tokens"
    echo "Required scopes: repo, actions"
    exit 1
fi

# Get the latest workflow run ID
echo "Fetching latest workflow runs..."
WORKFLOW_RUNS=$(curl -s -H "Authorization: Bearer $GITHUB_TOKEN" \
                  -H "Accept: application/vnd.github+json" \
                  -H "X-GitHub-Api-Version: 2022-11-28" \
                  "https://api.github.com/repos/$OWNER/$REPO/actions/runs?per_page=5")

# Extract the latest run ID
LATEST_RUN_ID=$(echo "$WORKFLOW_RUNS" | jq -r '.workflow_runs[0].id')
LATEST_RUN_STATUS=$(echo "$WORKFLOW_RUNS" | jq -r '.workflow_runs[0].status')
LATEST_RUN_CONCLUSION=$(echo "$WORKFLOW_RUNS" | jq -r '.workflow_runs[0].conclusion')

if [ -z "$LATEST_RUN_ID" ] || [ "$LATEST_RUN_ID" = "null" ]; then
    echo "Error: Could not find any workflow runs. Check your repository settings."
    exit 1
fi

echo "Latest Workflow Run ID: $LATEST_RUN_ID"
echo "Status: $LATEST_RUN_STATUS"
echo "Conclusion: $LATEST_RUN_CONCLUSION"

# Download logs for the latest workflow run
echo "Downloading logs..."
curl -L \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/repos/$OWNER/$REPO/actions/runs/$LATEST_RUN_ID/logs" \
  -o workflow_run_logs.zip

if [ $? -eq 0 ]; then
    echo "Logs downloaded successfully!"
    
    # Extract the logs
    mkdir -p workflow_run_logs
    unzip -o workflow_run_logs.zip -d workflow_run_logs
    
    echo ""
    echo "=== LOGS EXTRACTED TO: workflow_run_logs/ ==="
    echo "Files extracted:"
    ls -la workflow_run_logs/
    
    # Find and display the main error file
    echo ""
    echo "=== SEARCHING FOR ERRORS ==="
    for file in workflow_run_logs/*/*.txt; do
        if [ -f "$file" ]; then
            echo ""
            echo "--- Checking $file ---"
            if grep -q "error\|Error\|ERROR" "$file"; then
                echo "Found errors in $file:"
                grep -A 5 -B 2 "error\|Error\|ERROR" "$file" | head -30
            fi
        fi
    done
    
    # Show the latest job logs
    echo ""
    echo "=== LATEST JOB LOGS ==="
    find workflow_run_logs/ -name "*.txt" -type f | sort | tail -1 | while read file; do
        if [ -f "$file" ]; then
            echo "File: $file"
            cat "$file"
        fi
    done
else
    echo "Error downloading logs. Check your token permissions."
fi
