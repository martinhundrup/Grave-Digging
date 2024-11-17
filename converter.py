def remove_substrings_by_length(s: str, length: int) -> str:
    words = s.split()
    filtered_words = [word for word in words if len(word) == length]
    return ' '.join(filtered_words)

file = open('scraped_data.json', 'r')
converted = ''
outfile = open('dates.txt', 'w')

for line in file:
  if line.lstrip().startswith("\"") :
    stripped = list(line)
    stripped[0:26] = ''
    converted += ''.join(stripped)

lines = converted.split('\n')

#for i, line in enumerate(lines):
  #lines[i] = remove_substrings_by_length(line, 4)

print(lines)

for l in lines:
   outfile.write(l)
   outfile.write('\n')





