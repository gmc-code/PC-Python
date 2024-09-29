import string
from collections import Counter

# Text on vertebrate classification
text = """
Vertebrates are animals belonging to the subphylum Vertebrata, a major group within the phylum Chordata. They are characterized by having a backbone or spinal column, which is a defining feature that distinguishes them from invertebrates. Vertebrates also possess a well-developed brain enclosed in a skull, a complex nervous system, and an internal skeleton made of bone or cartilage. This group includes some of the most familiar animals, such as mammals, birds, reptiles, amphibians, and fish.

Fish are the most diverse group of vertebrates, with over 30,000 species. They are primarily aquatic and can be found in both freshwater and marine environments. Fish are divided into three main classes: Agnatha (jawless fish like lampreys and hagfish), Chondrichthyes (cartilaginous fish like sharks and rays), and Osteichthyes (bony fish). Bony fish are the largest group and include species such as salmon, trout, and goldfish. Fish have gills for breathing, fins for movement, and scales covering their bodies.

Amphibians are a unique group of vertebrates that typically start their life in water and undergo metamorphosis to become terrestrial adults. This group includes frogs, toads, salamanders, and newts. Amphibians have moist, permeable skin that allows for gas exchange, and they often return to water to reproduce. Their life cycle includes an aquatic larval stage, such as a tadpole, which later transforms into an adult capable of living on land.

Reptiles are cold-blooded vertebrates that include snakes, lizards, turtles, and crocodiles. They have dry, scaly skin that prevents water loss, and they lay shelled eggs on land. Birds, on the other hand, are warm-blooded vertebrates with feathers, wings, and beaks. They are highly adapted for flight, although some species are flightless. Birds lay hard-shelled eggs and have a high metabolic rate to support their energy-intensive activities. Both reptiles and birds share a common ancestry and have evolved various adaptations to thrive in diverse environments.

Mammals are distinguished by their ability to produce milk to nourish their young, a feature unique to this group. They are warm-blooded and have hair or fur covering their bodies. Mammals are incredibly diverse, ranging from tiny shrews to massive whales. They have complex brains, and many species exhibit advanced social behaviors and high levels of parental care. Mammals are found in nearly every habitat on Earth, from the deepest oceans to the highest mountains.
"""

# Split the text into words
words = text.split()

# Convert everything to lowercase
words = [word.lower() for word in words]

# Strip off any punctuation
words = [word.strip(string.punctuation) for word in words]

# Count occurrences of each word
word_counts = Counter(words)
# print(word_counts)

# Create a sorted list of starting letters
word_letter_set_list = sorted(set(word[0] for word in words))

# Filter out non-alphabetic characters
letter_list = [char for char in word_letter_set_list if char.isalpha()]

# Dictionary comprehension to categorize words by their starting letter and count occurrences
word_dict = {letter: dict(sorted({word: count for word, count in word_counts.items() if word.startswith(letter)}.items()))
             for letter in letter_list}

for letter in letter_list:
    print(letter, word_dict[letter])
