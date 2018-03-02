from polar_dictionary.pol_dict import PolarityDict
import pprint
pp = pprint.PrettyPrinter(indent=2)


def main():
    print('Getting polarity dictionary...\n')
    polar = PolarityDict()
    polar.from_file('var/clues.tff.patched')
    print('\nGot polarity dictionary\n')



if __name__ == '__main__':
    main()
