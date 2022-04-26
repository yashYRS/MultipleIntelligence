smarts = {
        'picture': {
                'prof1': 'Architect',
                'prof2': 'Artist',
                'prof3': 'Engineer'
        },
        'word': {
                'prof1': 'Writer/Journalist',
                'prof2': 'Lawyer',
                'prof3': 'Teacher'
        },
        'logic': {
                'prof1': 'Scientist/Mathematician',
                'prof2': 'Engineer',
                'prof3': 'Accountant'
        },
        'body': {
                'prof1': 'Dancer/Actor',
                'prof2': 'Sculptor',
                'prof3': 'Builder'
        },
        'music': {
                'prof1': 'Musician',
                'prof2': 'Singer',
                'prof3': 'Music-Conductor'
        },
        'people': {
                'prof1': 'Psychologist/Counselor',
                'prof2': 'Politician',
                'prof3': 'Manager'
        },
        'self': {
                'prof1': 'Theorist',
                'prof2': 'Writer',
                'prof3': 'Philosopher'
        },
        'nature': {
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
