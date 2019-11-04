import re
import matplotlib.pyplot as plt


def is_determiner(word):
    """ Determine if word is a determiner """

    determiners = {'the', 'The', 'and', 'And', 'of', 'Of', 'that', 'That',
                   'in', 'In', 'unto', 'Unto', 'a', 'A', 'is', 'Is', 'to', 'To',
                   'for', 'For', 'by', 'By', 'on', 'On', 'shall', 'Shall', 'from',
                   'From', 'are', 'as', 'were'}
    return word in determiners


def plot_data(sorted_data):
    """ Plot data to bar chart """

    total_words_to_plot = 10
    total_words = 0
    list_total_length = len(sorted_data)
    labels, values = [], []

    for pair in sorted_data:
        total_words += pair[1]
    for i in range(list_total_length - total_words_to_plot, list_total_length):
        current = sorted_data[i]
        labels.append(current[0])
        values.append(current[1])
    print('Total Words:', total_words)
    print('Total Words In List', sum(values))
    print('Total Words NOT In List', total_words - sum(values))

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_xlabel('Words In Bible')
    ax.set_ylabel('Count')
    ax.set_title(str(total_words_to_plot) + ' Most Used Words In Bible')
    plt.show()


def sort_data(mod_data):
    """ Sort dictionary by value """

    sorted_data = sorted(mod_data.items(), key=lambda kv: (kv[1], kv[0]))
    plot_data(sorted_data)


def modify_data(read_data):
    """ Remove all special characters. """

    modified_data = {}
    for word in read_data:
        new_word = re.sub('[^A-Za-z]+', '', word)
        if not is_determiner(new_word) and new_word:
            modified_data[new_word] = modified_data.get(new_word, 0) + 1
    sort_data(modified_data)


def main():
    """ Read words from a file"""

    with open('bible.txt', 'r') as f:
        raw_data = [word for line in f for word in line.split()]
    modify_data(raw_data)


if __name__ == '__main__':
    main()
