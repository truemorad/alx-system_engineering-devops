#!/usr/bin/env ruby
# Get the line from the argument
line = ARGV[0]

# Define a regular expression pattern to match the word "School"
pattern = /^\d{0,10}$/

# Find all matches in the line
matches = line.scan(pattern)

# Output each match
  puts matches.join("")
