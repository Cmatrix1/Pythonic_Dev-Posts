from collections import defaultdict

anagram_dict = defaultdict(list) # Tip:argument should be a callable
strs = ["ate", "eat", "tea", "anh", "han", "nah", "bah"]

for s in strs:
    anagram_dict[tuple(sorted(s))].append(s) 
    
print(anagram_dict.values())