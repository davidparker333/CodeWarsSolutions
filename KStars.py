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

    # Initialize a result list
    result = []

    # Check to see if there's enough stars to give back k as a result
    if len(star_list) < k:
        return -1

    # Begin looping k number of times
    for i in range(k):

        # If the result list is full, quit the loop early and return result (stops us from having to loop through once we already have the result)
        if len(result) == k:
            return result

        # Set the smallest to the largest value in the list to start
        smallest = max(star_list, key = lambda x: x.dist_from_earth)

        # Begin looping through stars in the star list
        for star in star_list:

            # Check if the star has a smaller distance than the current smallest, and whether or not its in the result list already
            if star not in result and star.dist_from_earth < smallest.dist_from_earth:

                # If the star has a smaller distance and not in the result, make it the new smallest
                smallest = star

        # At the end of the loop, append the smallest star to the result
        result.append(smallest)

    return result


print(find_stars(stars, 10))