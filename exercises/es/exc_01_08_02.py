import spacy

nlp = spacy.load("es_core_news_sm")

text = (
    "De acuerdo con la revista global de negocios Fortune, Apple fue "
    "la empresa más admirada en el mundo entre 2008 y 2012."
)

# Procesa el texto
doc = ____

# Itera sobre las entidades predichas
for ent in ____.____:
    # Imprime en pantalla el texto de la entidad y su etiqueta
    print(ent.____, ____.____)
