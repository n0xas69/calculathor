"""
calcul des calories et des maccro nutriment suivant objectif
"""
class Person:

    dicoTaux = {"1 fois par semaine ou moins" : 1.2, "2 à 3 fois par semaine" : 1.4, "4 fois par semaine" : 1.5, "5 fois ou plus par semaine" : 1.7}

    def __init__(self, sex, poids, taille, age, ta, objectif, morpho, activite):
        self.sex = sex
        self.poids = int(poids)
        self.taille = int(taille)
        self.age = int(age)
        self.ta = ta # taux d'activité
        self.objectif = objectif
        self.morpho = morpho
        self.activite = activite


    def calculTMB(self):
        tmb = 0
        if self.sex == "Une femme":
            tmb = (9.99*self.poids) + (6.25 * self.taille) - (4.92*self.age) - 161
        else:
            tmb = (9.99*self.poids) + (6.25*self.taille) - (4.92 * self.age) + 5
        return tmb

    def calculTA(self, tmb):
        cal = tmb * self.dicoTaux.get(self.ta)
        if self.activite == "Vous avez un travail sédentaire":
            cal = cal - (cal * 5) / 100
        else:
            cal = cal + (cal * 5) / 100

        if self.morpho == "Facilement":
            cal = cal - (cal * 10) / 100
        else:
            cal = cal + (cal * 10) / 100

        if self.objectif == "Prise de masse":
            cal = cal + (cal * 10) / 100
        else:
            cal = cal - (cal * 15) / 100

        return cal

    def macro(self, cal, objectif):
        cal = int(cal)
        if objectif == "Prise de masse":
            glucide = (cal / 2) / 4
            proteine = (cal * 30 / 100) / 4
            lipide = (cal * 20 / 100) / 4
        else:
            glucide = (cal / 2) / 4
            proteine = (cal * 35 / 100) / 4
            lipide = (cal * 15 / 100) / 4
        return glucide, proteine, lipide



if __name__ == "__main__":
    p = Person("Un homme", 94, 182, 24, "4 fois par semaine")
    tmb = p.calculTMB()
    calorie = p.calculTA(tmb)
    print(p.macro(calorie))
    print(calorie)