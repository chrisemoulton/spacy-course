import spacy

nlp = spacy.blank("en")

# Processar o texto
doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)

# Iterar os tokens de um documento doc 
for token in doc:
    # Checar se o token é composto por algarismos numéricos
    if ____.____:
        # Selecionar o próximo token do documento
        next_token = ____[____]
        # Checar se o texto do proximo token é igual a "%"
        if next_token.____ == "%":
            print("Percentage found:", token.text)
