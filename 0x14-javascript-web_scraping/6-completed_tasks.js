#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "Please provide the API URL as an argument."
  exit 1
fi

# Make the request and process the response
request_output=$(curl -s "$1")
completed_users=()

# Loop through the tasks
while IFS= read -r task; do
  completed=$(echo "$task" | jq -r '.completed')
  if [ "$completed" = "true" ]; then
    userId=$(echo "$task" | jq -r '.userId')
    completed_users+=("$userId")
  fi
done <<< "$request_output"

# Calculate the number of completed tasks by user id
declare -A completed_counts
for user_id in "${completed_users[@]}"; do
  ((completed_counts["$user_id"]++))
done

# Print users with completed tasks
for user_id in "${!completed_counts[@]}"; do
  completed_count=${completed_counts["$user_id"]}
  echo "User $user_id completed $completed_count tasks."
done
