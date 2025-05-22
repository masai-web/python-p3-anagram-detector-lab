# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  
    
    def match(self, possible_anagrams):
        matches = []
        
        original_sorted = sorted(self.word)
        
        for candidate in possible_anagrams:
           
            if candidate.lower() == self.word:
                continue
            
            if sorted(candidate.lower()) == original_sorted:
                matches.append(candidate)
        
        return matches