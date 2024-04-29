def compare_prefixes(file1, file2):
  """
  Compares network prefixes from two text files, considering "/" as part of the prefix.

  Args:
    file1: Path to the first text file.
    file2: Path to the second text file.
  """
  # Sets to store prefixes from each file
  prefixes1 = set()
  prefixes2 = set()

  # Read prefixes from file1
  with open(file1, 'r') as f:
    for line in f:
      prefix = line.strip()  # Read the entire line
      prefixes1.add(prefix)

  # Read prefixes from file2
  with open(file2, 'r') as f:
    for line in f:
      prefix = line.strip()  # Read the entire line
      prefixes2.add(prefix)

  # Check if files are read correctly
  print("Prefixes in", file1, ":", prefixes1)
  print("Prefixes in", file2, ":", prefixes2)

  # Find prefixes only in file1
  only_in_file1 = prefixes1 - prefixes2

  # Find prefixes only in file2
  only_in_file2 = prefixes2 - prefixes1

  # Find prefixes in both files
  in_both = prefixes1.intersection(prefixes2)

  # Print results
  print("Prefixes only in", file1, ":")
  for prefix in only_in_file1:
    print(prefix)

  print("\nPrefixes only in", file2, ":")
  for prefix in only_in_file2:
    print(prefix)

  print("\nPrefixes in both files:")
  for prefix in in_both:
    print(prefix)

  compare_prefixes(file1, file2)  