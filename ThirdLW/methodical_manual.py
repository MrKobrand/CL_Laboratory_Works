import ufal.udpipe

#text = 'Контактный модулятор электрического тока, содержащий вибропреобразователь,выполненный на основе поляризованного электромагнитного реле, генератор переменного тока, подключенный к обмотке возбуждения вибропреобразователя, и согласующий трансформатор'
text = 'эмиттер и коллектор соединены с положительным электродом автономного источника питания усилителя сигнала'
model = ufal.udpipe.Model.load('russian-syntagrus-ud-2.4-190531.udpipe')
tokenizer = model.newTokenizer(model.DEFAULT)
tokenizer.setText(text)
error = ufal.udpipe.ProcessingError()
sentences = []
sentence = ufal.udpipe.Sentence()
while tokenizer.nextSentence(sentence, error):
    sentences.append(sentence)
    sentence = ufal.udpipe.Sentence()

subjects = []
actions = []
objects = []
for s in sentences:
    model.tag(s, model.DEFAULT)
    model.parse(s, model.DEFAULT)
    for w in s.words:
        if (w.upostag == 'VERB'):
            actions.append(w.lemma)
            if (w.head <= 0):
                subjects.append('')
            else:
                if (s.words[w.head].upostag == 'NOUN'):
                    subjects.append(s.words[w.head].lemma)
                else:
                    subjects.append('')
            obj = ' '
            for ob in s.words:
                if (ob.head == w.id and ob.upostag == 'NOUN'):
                    obj += ob.lemma + ' '
            objects.append(obj)

output_format = ufal.udpipe.OutputFormat.newOutputFormat('conllu')
output = ''
for sentence in sentences:
    output += output_format.writeSentence(sentence)
    output += output_format.finishDocument()
print(output)

for ind, word in enumerate(actions):
    print(subjects[ind], word, objects[ind])