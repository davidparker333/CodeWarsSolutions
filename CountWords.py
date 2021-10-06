# Kate likes to count words in text blocks. By words she means continuous sequences of English alphabetic characters (from a to z ). Here are examples:

# Hello there, little user5453 374 ())$. I’d been using my sphere as a stool. Slow-moving target 839342 was hit by OMGd-63 or K4mp. contains 
# "words" ['Hello', 'there', 'little', 'user', 'I', 'd', 'been', 'using', 'my','sphere', 'as', 'a', 'stool', 'Slow', 'moving', 'target', 'was', 'hit', 
# 'by', 'OMGd', 'or', 'K', 'mp']

# Kate doesn't like some of words and doesn't count them. Words to be excluded are "a", "the", "on", "at", "of", "upon", "in" and "as", case-insensitive.

# Today Kate's too lazy and have decided to teach her computer to count "words" for her.

# Example Input 1
str1 = 'Hello there, little user5453 374 ())$.'

# Example Output 1
# 4

# Example Input 2
str2 = 'I’d been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. My bolt had shifted \
while I’d been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed under a \
stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient fraa and his two fids were copying out books there. But \
I wondered how long it would take to stop smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must \
be deep into everything.'

# Example Output 2
# 112

str3 = 'The Mynster had a ceiling of stone, steeply vaulted. Above the vaults, a flat roof had been framed. Built upon that roof was the aerie of the Warden Fendant.\
 Its inner court, squared around the Præsidium, was roofed and walled and diced up into store-rooms and headquarters, but its periphery was an open walkway on which \
 the Fendant’s sentinels could pace a full circuit of the Mynster in a few minutes’ time, seeing to the horizon in all directions (except where blocked by a buttress, \
 pier, spire, or pinnacle). This ledge was supported by dozens of close-spaced braces that curved up and out from the walls below. The end of each brace served as a \
 perch for a gargoyle keeping eternal vigil. Half of them (the Fendant gargoyles) gazed outward, the other half (the Regulant gargoyles) bent their scaly necks and \
 aimed their pointy ears and slitted eyes into the concent spread below. Tucked between the braces, and shaded below the sentinels’ walkway, were the squat Mathic arches \
 of the Warden Regulant’s windows. Few places in the concent could not be spied on from at least one of these— and, of course, we knew them all by heart.'


def word_count(s):
    excl_words = ["a", "the", "on", "at", "of", "upon", "in", "as"]

    def clean_string(s):
        res = ''
        for char in s:
            if (char.isalpha() or char.isspace()) and char != 'æ':
                res += char
            else:
                res += ' '
        return res.split()

    return len([w for w in clean_string(s) if w.lower() not in excl_words])

print(word_count(str3))
