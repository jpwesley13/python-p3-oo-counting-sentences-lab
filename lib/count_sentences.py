#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        if self.value.endswith("."):
            return True
        return False
    
    def is_question(self):
        if self.value.endswith("?"):
            return True
        return False
    
    def is_exclamation(self):
        if self.value.endswith("!"):
            return True
        return False
    
    def count_sentences(self):
        count = 0
        sentence_enders = [".", "!", "?"]
        previous_char = ""
        
        for char in self.value:
            if char in sentence_enders:
                if previous_char not in sentence_enders:
                    count += 1
            previous_char = char 

        return count