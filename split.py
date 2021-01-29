import sys

path_corpus=sys.argv[1]

if __name__=='__main__':
    i=0
    k=0
    sentences=[]
    with open(path_corpus,'r',encoding='utf-8') as corpus:
        for line in corpus:
            sentences.append(line)
            i+=1
            if i == 5000000:
                with open('/all_text_{}.txt'.format(k),'w',encoding='utf-8') as file:
                    for sentence in sentences:
                        file.writelines(sentence)
            i=0
            k+=1
            sentences=[]
