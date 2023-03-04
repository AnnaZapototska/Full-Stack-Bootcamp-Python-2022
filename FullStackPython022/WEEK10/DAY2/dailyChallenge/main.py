#
from translate import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translations = {}

# Loop through each French word and translate 
for word in french_words:
    translator = Translator(to_lang="English")
    translation = translator.translate(word)
    translations[word] = translation

# Print the resulting dictionary
print(translations)

