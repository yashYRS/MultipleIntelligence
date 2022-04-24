smarts = {
        'Visual_Spatial': {
                'prof1': 'Architect',
                'prof2': 'Artist',
                'prof3': 'Engineer'
        },
        'Linguitic-Verbal': {
                'prof1': 'Writer/Journalist',
                'prof2': 'Lawyer',
                'prof3': 'Teacher'
        },
        'Logical-Mathematical': {
                'prof1': 'Scientist/Mathematician',
                'prof2': 'Engineer',
                'prof3': 'Accountant'
        },
        'Bodily-Kinesthetic': {
                'prof1': 'Dancer/Actor',
                'prof2': 'Sculptor',
                'prof3': 'Builder'
        },
        'Musical': {
                'prof1': 'Musician',
                'prof2': 'Singer',
                'prof3': 'Music-Conductor'
        },
        'Interpersonal': {
                'prof1': 'Psychologist/Counselor',
                'prof2': 'Politician',
                'prof3': 'Manager'
        },
        'Intrapersonal': {
                'prof1': 'Theorist',
                'prof2': 'Writer',
                'prof3': 'Philosopher'
        },
        'Naturalistic': {
                'prof1': 'Biologist',
                'prof2': 'Conservationist',
                'prof3': 'Farmer'
        }

}


def get_professions(smart):
    data = smarts[smart]
    prof1 = data['prof1']
    prof2 = data['prof2']
    prof3 = data['prof3']
    return prof1, prof2, prof3
