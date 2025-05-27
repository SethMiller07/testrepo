def level_up(experience):
    if experience < 100:
        return 1
    elif experience < 200:
        return 2
    else:
        return 3
