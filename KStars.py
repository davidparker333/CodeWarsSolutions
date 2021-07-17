#Model and create a list of star objects. Assume there are millions of entries in this list. Write a function that, given k (the number of stars searched for), return the k closest stars to the earth

class Star:

    def __init__(self, dist_from_earth, id):
        self.id = id
        self.dist_from_earth = dist_from_earth

    def __repr__(self):
        return f'<Star Obj | {self.id} {self.dist_from_earth}>'

    def __str__(self):
        return f'<Star Obj | {self.id} {self.dist_from_earth}>'

stars = [Star(i*100000, i) for i in range(1000)]


def find_stars(star_list, k):

    i = 0
    result = []

    if len(star_list) < k:
        return -1

    while i < k:
        smallest = max(star_list, key = lambda x: x.dist_from_earth)
        for star in star_list:
            if star not in result and star.dist_from_earth < smallest.dist_from_earth:
                smallest = star
        result.append(smallest)
        i+=1
    return result


print(find_stars(stars, 10))