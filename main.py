from polar_dictionary.pol_dict import PolarityDict
from preprocess_data.get_data import DataSet
import pprint
pp = pprint.PrettyPrinter(indent=2, width=200)


def main():
    print('Getting polarity dictionary...\n')
    polar = PolarityDict()
    polar.from_file('var/clues.tff.patched')
    print('\nGot polarity dictionary\n')

    # get dataset
    train_set = DataSet()
    train_set.from_file('var/train_set.gs')
    pp.pprint(train_set.tweets[:2])

    # with open('var/dataset_name.pred', mode='w') as out_f:
    #     out_f.write(str(train_set))


if __name__ == '__main__':
    main()
