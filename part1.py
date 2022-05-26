import os

new_line = ""

with open("alice.txt") as f:
  new_line = f.readlines()

f.close()

print (new_line)

new_line[0] = "Hello\n"

print (new_line)

fwrite = open("alice.txt", "w")
for line in new_line:
  fwrite.write(line)

fwrite.close()