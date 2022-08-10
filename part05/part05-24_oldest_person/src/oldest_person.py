# Write your solution here
def oldest_person(people: list):
    oldest = people[0][1]
    for person in people:
        year = person[1]
        if oldest < year:
            oldest = year

    return oldest
    
def oldest_person(people: list):

    oldestName = people[0][0]
    oldestAge = people[0][1]
    
    for i in people:
        if i[1] < oldestAge:
            oldestAge = i[1]
            oldestName = i[0]

    #print(oldestAge)
    return (oldestName)

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))