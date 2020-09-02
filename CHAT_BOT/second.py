import nltk
nltk.download('punkt')


with open('dialogies.txt', encoding='utf-8') as f:
    content = f.read()
dialogues = []
for dialogue_text in content.split('\n\n'):
    replicas = dialogue_text.split('\n')
    if len(replicas) >= 2:
        replicas = replicas[:2]
        replicas = [replica[2:] for replica in replicas]
        replicas[0] = replicas[0].lower().strip()
        if replicas[0]:
            dialogues.append(tuple(replicas))
list(set(dialogues))

qa_dataset = {}
alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю'
for question, answer in dialogues:
    tokens = nltk.word_tokenize(question)
    words = [token for token in tokens if any(char in token for char in alphabet)]
    for word in words:
        if word not in qa_dataset:
            qa_dataset[word] = []
        qa_dataset[word].append((question, answer))


def get_generative_answer(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    words = [token for token in tokens if any(char in token for char in alphabet)]
    for word in words:
        if word in qa_dataset:
            for question, answer in qa_dataset[word]:
                if abs(len(text) - len(question)) / len(question) < 0.2:
                    distance = nltk.edit_distance(text, question)
                    if distance / len(question) < 0.2:
                        return answer


print(get_generative_answer('12345678'))
