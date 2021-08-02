class Alignment:
    def __init__(self, primary, secondary):
        # Alignments have 2 parts - the faction, and purpose within it
        self.primary = primary
        self.secondary = secondary

        # Alignments are usually just abbreviated
        self.shorthand = self.primary[0] + self.secondary[0]

    def __str__(self):
        return "{primary} ({secondary})".format(primary=self.primary, secondary=self.secondary)


# Not really a nice way to handle this IMO but I can't be bothered when this works
TI = Alignment("Town", "Investigative")
TP = Alignment("Town", "Protective")
TK = Alignment("Town", "Killing")
TS = Alignment("Town", "Support")

MD = Alignment("Mafia", "Deception")
MK = Alignment("Mafia", "Killing")
MS = Alignment("Mafia", "Support")

NB = Alignment("Neutral", "Benign")
NE = Alignment("Neutral", "Evil")
NK = Alignment("Neutral", "Killing")
NC = Alignment("Neutral", "Chaos")

CE = Alignment("Coven", "Evil")