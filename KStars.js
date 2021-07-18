// Model and create a list of star objects. Assume there are millions of entries in this list. Write a function that, given k (the number of stars searched for), return the k closest stars to the earth

class Star {
    constructor(dist_from_earth, id) {
        this.dist_from_earth = dist_from_earth;
        this.id = id;
    }
}

let stars = [];

for (let i=0; i<100; i++) {
    stars.push(new Star(i*10000, i));
}

let closestStars = (starList, k) => {
    let i = 0;
    let res = [];
    while (i < k) {
        var min = Math.max.apply(Math, stars.map((o) => {return o.dist_from_earth}));
        starList.forEach(star => {
            if ((star.dist_from_earth < min) & !(star.id in res.map((s) => {return s.id}))) {
                min = star;
            }
        });
        res.push(min);
        i++;
    }
    return res;
}

console.log(closestStars(stars, 10));