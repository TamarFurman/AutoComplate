import psutil
from data.node_trie import Node_Trie


class Word_Trie:
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = Node_Trie("")

    def insert(self, sentence, full_sentence):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in sentence:
            if char in node.children:
                node = node.children[char]
                if len(node.sentences) < 5:
                    node.sentences.update({full_sentence: ""})
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = Node_Trie(char)
                node.children[char] = new_node
                node = new_node
                if len(node.sentences) < 5:
                    node.sentences.update({full_sentence: ""})


        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        # node.counter += 1

    def search(self, sentence):
        self.sentence = sentence
        node = self.root
        skip = False
        for char in sentence:
            if char in node.children:
                node = node.children[char]
            elif not skip:
                skip = True
                continue
            else:
                return
        return node.sentences if node.sentences else self.delete_char()

    def delete_char(self):
        node = self.root
        for i in range(len(self.sentence)):
            if self.sentence[i] in node.children:
                node = node.children[self.sentence[i]]
            else:
                for node_child in node.children.keys():
                    if self.sentence[i] in node.children[node_child].children:
                        result = self.continue_search(node.children[node_child], i + 1)
                        if result:
                            return result
                return
        return

    def replace_char(self):
        node = self.root
        for i in range(len(self.sentence)):
            if self.sentence[i] in node.children:
                node = node.children[self.sentence[i]]
            else:
                for node_child in node.children.keys():
                    result = self.continue_search(node.children[node_child], i + 1)
                    if result:
                        return result
                return
        return

    def continue_search(self, node, index):
        for i in range(index, len(self.sentence)):
            if self.sentence[i] in node.children:
                node = node.children[self.sentence[i]]
        return node.sentences
