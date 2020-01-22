languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
print("""Python was created by {Python}
Ruby was created by {Ruby}
PHP was created by {PHP}""".format(**languages))