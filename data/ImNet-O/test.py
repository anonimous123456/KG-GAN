from nltk.corpus import wordnet as wn



def readTxt(file_name):
    class_list = list()
    wnids = open(file_name, 'rU')
    try:
        for line in wnids:
            line = line[:-1]
            class_list.append(line)
    finally:
        wnids.close()
    print(len(class_list))
    return class_list

def getnode(x):
    return wn.synset_from_pos_and_offset('n', int(x[1:]))
def getwnid(u):
    s = str(u.offset())
    return 'n' + (8 - len(s)) * '0' + s


seen_file = 'seen.txt'
unseen_file = 'unseen.txt'

seen = readTxt(seen_file)
unseen = readTxt(unseen_file)


file = 'seen_list.txt'
wr_fp = open(file, 'w')

for node in seen:
    syn = getnode(node)
    # print(node)
    syn_name = syn.lemma_names()[0]
    wr_fp.write('%s\t%s\n' % (node, syn_name))
wr_fp.close()


file = 'unseen_list.txt'
wr_fp = open(file, 'w')

for node in unseen:
    syn = getnode(node)
    # print(node)
    syn_name = syn.lemma_names()[0]
    wr_fp.write('%s\t%s\n' % (node, syn_name))
wr_fp.close()