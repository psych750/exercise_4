import os
import random

def generate_trials(subj_code, prop_incongruent, num_trials=100):
    '''
    Writes a file named {subj_code_}trials.csv, one line per trial. Creates a trials subdirectory if one does not exist
    subj_code: a string corresponding to a participant's unique subject code
    prop_incongruent: float [0-1] corresponding to the proportion of trials that are incongruent
    num_trials: integer specifying total number of trials (default 100)
    '''
    separator = ","
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    num_incongruent = round(float(prop_incongruent)*int(num_trials))
    num_congruent = num_trials-num_incongruent
    if num_congruent+num_incongruent != num_trials: # just in case
        raise Exception(f"Can't get that proportion ({prop_incongruent}) *and* have that number of trials ({num_trials})")

    #create list of trial types
    trial_types = ['congruent']*num_congruent + ['incongruent']*num_incongruent

    #create list of orientations - notice that this will break for an even number of trials!
    orientations = ['upright']*round(num_trials/2) + ['upside_down']*round(num_trials/2)

    random.shuffle(trial_types) # think about why we're not assigning this to a variable
    random.shuffle(orientations)


    def make_incongruent(colors,color):
        incongruent_color = set(colors).difference(set([color]))
        return random.choice(list(incongruent_color))

    try:
        os.mkdir('trials')
        print('Trials directory did not exist. Created trials/')
    except FileExistsError:
        pass #switched it 
    f= open(f"trials/{subj_code}_trials.csv","w")
    
    trial_data = []
    for i in range(num_trials):
        cur_word = random.choice(colors)
        cur_trial_type = trial_types[i]
        if cur_trial_type == 'incongruent':
            cur_color = make_incongruent(colors,cur_word)
        else:
            cur_color = cur_word
        trial_data = map(str,[subj_code, prop_incongruent, cur_word, cur_color, cur_trial_type, orientations[i]])
        f.write(separator.join(trial_data)+'\n')

    f.close()


if __name__ == '__main__':
	generate_trials('testsubj_.5',.5)
	generate_trials('testsubj_.25',.25)
	generate_trials('testsubj_.75',.75)
