from __init__ import ROOT_DIR


def main():
    with open(f'{ROOT_DIR}/ipg150106.xml', 'r') as shared_file:
        patent_count = 0
        prev_patent_index = 0
        content = shared_file.readlines()
        for i in range(len(content)):
            if patent_count >= 100:
                break

            if content[i] == '<?xml version="1.0" encoding="UTF-8"?>\n':
                patent_count += 1
                prev_patent_index = i

                with open(f'{ROOT_DIR}/XMLExamples/patent_{patent_count}.xml', 'w') as output_file:
                    output_file.writelines(content[i:content.index('<?xml version="1.0" encoding="UTF-8"?>\n', i + 1)])


if __name__ == '__main__':
    main()
