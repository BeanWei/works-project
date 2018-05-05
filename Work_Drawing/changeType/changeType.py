import os
file_path = os.path.abspath(os.path.dirname(__file__))+'/log'
out_path = os.path.abspath(os.path.dirname(os.getcwd()))+'/log/'
for file_name in os.listdir(file_path):
    with open(file_path+'/'+file_name) as f:
        fileContent = []
        for l in f.readlines():
            # line=[]
            # line.append(l.split(','))
            fileContent.append(l.split(','))
        # fileContent.append([[l] for l in f.readlines()])
        result = map(list,zip(*fileContent)) 
        with open(out_path+file_name,'a+') as fp:
            for r in result:
                fp.write((','.join(r)).replace('\n','')+'\n')
