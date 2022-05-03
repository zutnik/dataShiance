people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    return '{}'.format(person.split(' ')[0:2])


splitlambda = lambda person: '{}'.format(person.split(' ')[0:2])

print(list(map(split_title_and_name, people)))
print(list(map(splitlambda, people)))
