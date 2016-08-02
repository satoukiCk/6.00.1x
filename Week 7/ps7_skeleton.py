import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = (location[0] * 1.0, location[1] * 1.0)
    def get_number_of_species(self, animal):
        if animal in self.species_types.keys():
            return self.species_types[animal]
        else:
            return 0
    def get_location(self):
        return self.location
    def get_species_count(self):
        return self.species_types.copy()
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        if species in self.species_types.keys():
            self.species_types[species] -=1
            if self.species_types[species] <= 0:
                del self.species_types[species]




class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        return 1.0*adoption_center.get_number_of_species(self.get_desired_species())



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self,name,desired_species,considered_species):
        Adopter.__init__(self,name,desired_species)
        self.considered_species = considered_species
    def get_score(self,adoption_center):
        score = 1.0 * adoption_center.get_number_of_species(self.get_desired_species())
        other = 0
        for i in self.considered_species:
                other += adoption_center.get_number_of_species(i)
        score += 0.3 * other
        return score

class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self,name,desired_species,feared_species):
        Adopter.__init__(self,name,desired_species)
        self.feared_species = feared_species
    def get_score(self,adoption_center):
        score = 1.0 * adoption_center.get_number_of_species(self.get_desired_species())
        other = adoption_center.get_number_of_species(self.feared_species)
        score = score - 0.3 * other
        if score < 0:
            return 0.0
        return score


class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self,name,desired_species,allergic_species):
        Adopter.__init__(self,name,desired_species)
        self.allergic_species = allergic_species
    def get_score(self,adoption_center):
        for i in self.allergic_species:
            if adoption_center.get_number_of_species(i) > 0:
                return 0.0
        else:
            return 1.0 * adoption_center.get_number_of_species(self.get_desired_species())


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self,name,desired_species,allergic_species,medicine_effectiveness):
        AllergicAdopter.__init__(self,name,desired_species,allergic_species)
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        min = 1.0
        for i in self.medicine_effectiveness.keys():
            if adoption_center.get_number_of_species(i) > 0 and self.medicine_effectiveness[i] < min:
                min = self.medicine_effectiveness[i]
        return min * 1.0 * adoption_center.get_number_of_species(self.desired_species)



class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self,name,desired_species,location):
        Adopter.__init__(self,name,desired_species)
        self.location = location

    def get_linear_distance(self,to_location):
        import math
        d = math.sqrt((self.location[0] * 1.0 - to_location[0] * 1.0) ** 2 + (self.location[1] * 1.0 - to_location[1] * 1.0) ** 2 )
        return d

    def get_score(self, adoption_center):
        import random
        location = adoption_center.get_location()
        d = self.get_linear_distance(location)
        if d < 1:
            return 1.0 * adoption_center.get_number_of_species(self.desired_species)
        elif 1 <= d < 3:
            return random.uniform(0.7,0.9) * adoption_center.get_number_of_species(self.desired_species)
        elif 3 <= d < 5:
            return random.uniform(0.5, 0.7) * adoption_center.get_number_of_species(self.desired_species)
        else:
            return random.uniform(0.1, 0.5) * adoption_center.get_number_of_species(self.desired_species)

    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    # Your Code Here
    dict = []
    for center in list_of_adoption_centers:
        dict.append([center,adopter.get_score(center)])
    orderdict = sorted(dict,key = lambda t:t[0].get_name())
    orderdict = sorted(orderdict,key = lambda t:t[1],reverse=True)
    result = []
    for i in orderdict:
        result.append(i[0])
    return result


def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here
    dict = []
    for adopter in list_of_adopters:
        dict.append([adopter,adopter.get_score(adoption_center)])
    orderdict = sorted(dict, key=lambda t: t[0].get_name())
    orderdict = sorted(orderdict,key = lambda t:t[1],reverse=True)
    result = []
    for i in orderdict:
        result.append(i[0])
    if n > len(result):
        return result
    else:
        return result[:n]


adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": rand.random()})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four", "Cat", "Dog")
adopter5 = SluggishAdopter("Five", "Cat", (1, 2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat")

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1, 1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3, 5))
ac3 = AdoptionCenter("Place3", {"Cat": rand.randint(20, 50), "Dog": rand.randint(1, 10)}, (-2, 10))

# how to test get_adopters_for_advertisement
print get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
# you can print the name and score of each item in the list returned

adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat")

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
print get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])
# you can print the name and score of each item in the list returned