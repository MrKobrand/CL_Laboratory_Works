import re

from typing import NoReturn
from pprint import pprint
from nltk.corpus import wordnet


def main() -> NoReturn:
    with open('superliminal_steam_review.txt', mode='r') as review:
        modified_lines = []
        for line in review.readlines():
            part_of_speech = []
            line_without_delimiters = ' '.join(w for w in re.split(r'\W', line) if w)
            for word in line_without_delimiters.split():
                try:
                    syn = wordnet.synsets(word)[0]
                    part_of_speech.append(f'({syn.pos()})')
                except IndexError:
                    part_of_speech.append('(nf)')
            words = line.split()
            for i in range(len(words)):
                if words[i][-1] in [',', '.']:
                    words[i] = f'{words[i][:-1]} {part_of_speech[i]}{words[i][-1]}'
                else:
                    words[i] = f'{words[i]} {part_of_speech[i]}'
            modified_lines.append(
                ' '.join(
                    word for word in words
                )
            )

        with open('superliminal_steam_review_with_parts_of_speech.txt', mode='w') as file:
            for sentence in modified_lines:
                file.write(f'{sentence}\n')

        pprint(modified_lines)




    # syn = wordnet.synsets('hello')[0]
    # print("Syn tag : ", syn.pos())
    #
    # syn = wordnet.synsets('doing')[0]
    # print("Syn tag : ", syn.pos())
    #
    # syn = wordnet.synsets('beautiful')[0]
    # print("Syn tag : ", syn.pos())
    #
    # syn = wordnet.synsets('quickly')[0]
    # print("Syn tag : ", syn.pos())


if __name__ == '__main__':
    main()
