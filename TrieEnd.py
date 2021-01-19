try:
    class TrieNode(object):
        """
        Our trie node implementation. Very basic.
        """

        def __init__(self, char: str):
            self.char = char
            self.children = []
            # Is it the last character of the word.`
            self.word_finished = False


    def add(root, word: str):
        """
        Adding a word in the trie.
        """
        node = root
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found it.
                    # word has it as well
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = TrieNode(char)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
        # Everything finished. Mark it as the end of a word.
        node.word_finished = True


    def dell(root, word: str):
        """
        deleting a word in the trie structure
        """
        node = root
        for char in word:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break

            # We did not find it so add a new chlid
            if not found_in_child:
                print("This word did not exist!")
                break
            node.word_finished = False

        # Everything finished.


    def find_prefix(root, prefix: str):
        """
        Check and return
        """
        node = root
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not root.children:
            return False, 0
        for char in prefix:
            char_not_found = True
            # Search through all the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found the char existing in the child.
                    char_not_found = False
                    # Assign node as the child containing the char and break
                    node = child
                    break
            # Return False anyway when we did not find a char.
            if char_not_found:
                return False
        # Well, we are here means we have found the prefix. Return true to indicate that
        # And also the counter of the last node. This indicates how many words have this
        # prefix
        if node.word_finished:
            return True
        else:
            return False
    allwords = list()
    root = TrieNode("#")
    while True:
        print("What do you want to do? \nPlease insert the relevant key and press Enter.")
        print("Q->build a Trie with file.")
        print("E->add a word to Trie.")
        print("W->check a file in Trie.")
        print("R->check a word in Trie.")
        print("T->delete a word in Trie.")
        print("Y->print all words of Trie.")
        print("U->exit.")
        x = input("")
        key = x.lower()
        if key == "q":
            # generate a tray tree
            address = "E:/sample1.txt"
            f = open(address)
            for line in f:
                line = line.replace(".", " ") #replace . with sapce
                line = line.replace(",", " ") #replace , with space
                line = line.lower() #make all word lowercase
                line = line.rstrip()#remove \n end of line
                x = line.split()#split all word  in line.
                i = 0
                for i in range(len(x)):
                    if x[i - 1] != "":
                        add(root,x[i - 1])
                        allwords.append(x[i - 1])
            mword = allwords
            allwords = list(dict.fromkeys(mword))
        if key == 'w':
            # find a file words
            address = "E:/sample1.txt"
            f = open(address)
            for xline in f:
                xline = xline.replace(".", " ")
                xline = xline.replace(",", " ")
                xline = xline.lower()
                xline = xline.rstrip()
                y = xline.split()
                i = 0
                for i in range(len(y)):
                    if y[i - 1] != "":
                        print("[", y[i - 1], "]", "is", find_prefix(root, y[i - 1]))
        if key == 'e':
            # add a word to tree
            x = input("Enter the word:")
            wordinsert = x.lower()
            add(root, wordinsert)
            allwords.append(wordinsert)
            mword=allwords
            allwords = list(dict.fromkeys(mword))
        if key == 'r':
            # find a word in tree
            x = input("Enter the word:")
            wordinsert = x.lower()
            print(find_prefix(root, wordinsert))
        if key == 't':
            # delete a word in tree
            x = input("Enter the word:")
            wordinsert = x.lower()
            dell(root, wordinsert)
            for m in range(len(allwords) - 1):
                if wordinsert == allwords[m - 1]:
                    del (allwords[m - 1])
        if key == 'y':
            print(allwords)
        if key == "u":
            break
except IOError as e:
    print("Several errors were received as %s " % e)