#!/usr/bin/env ruby
# Get the line from the argument
line = ARGV[0]

# Define a regular expression pattern to match the word "School"
pattern = /Feb  1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS \[SMSC:SYBASE1\] \[SVC:\] \[ACT:\] \[BINF:\] \[FID:\] \[from:([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?\] \[to:([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))] \[flags:(([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?(:([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[Ee]([+-]?\d+))?)+)\] \[msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time\.\] \[udh:0:\]/
# Find all matches in the line
matches = line.scan(pattern)

# Output each match
  puts matches.join("")
