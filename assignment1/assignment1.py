from collections import Counter

#############
# swapchars #
#############
def swapchars(str):
    if not str:
        return str
    ranked = Counter(''.join(re.split("[^a-zA-Z]*", str))).most_common()
    swaps = {
        ranked[0][0]: ranked[-1][0],
        ranked[-1][0]: ranked[0][0]
    }
    return ''.join([swaps.get(chr, chr) for chr in str])


###########
# sortcat #
###########
def sortcat(n, *args):
    if not args:
        return None
    return sorted(args, key=lambda i: -len(i))[:None if n == -1 else n]


###############################
# Blue's Clues & Blue's Booze #
###############################
state_abbreviations = {}
abbreviations_state = {}

def __load_state_info():
    if not state_abbreviations:
        with open('states.txt') as f:
            for line in f:
                full, short = line.strip().split(',')
                state_abbreviations[short] = full
                abbreviations_state[full] = short

################
# Blue's Clues #
################
def state_from_abbrev(abbrev):
    __load_state_info()
    print state_abbreviations.get(abbrev, 'Not a valid abbreviation')

################
# Blue's Booze #
################
def abbrev_from_state(state):
    __load_state_info()
    print abbreviations_state.get(state, 'Not a valid state')

# To get multiple abbreviations at one time:
#
#   >>> map(abbrev_from_state, ['California', 'Alabama', 'Texas'])
#   CA
#   AL
#   TX
