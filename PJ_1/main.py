with open("C:/Users/a5105/Desktop/vscode_pj/python/procedure1/PJ_1/1-1-mission_computer_main.log", "r") as fr:
    lines =fr.readlines()

lines.reverse()
target = ['explosion', 'unstable']

fw = open("C:/Users/a5105/Desktop/vscode_pj/python/error.txt", "w")

for line in lines:
    line = line.strip()
    for wanna_word in target:
            warning_line = line.find(wanna_word)
            if warning_line != -1:
                fw.write(line+"\n")
                
            
    print(line)
    if not line: break
    
fr.close()
fw.close()