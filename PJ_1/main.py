try:
    with open("C:/Users/a5105/Desktop/vscode_pj/python/procedure1/PJ_1/1-1-mission_computer_main.log", "r") as fr:
        lines =fr.readlines()
except FileNotFoundError:
    print("입력 파일 없음")
    line=[]
except Exception as e:
    print("입력 오류", e)
    line = []
    

lines.reverse()
target = ['explosion', 'unstable']

try:
    fw = open("C:/Users/a5105/Desktop/vscode_pj/python/procedure1/PJ_1/error.txt", "w")
except:
    print("출력 오류",e)
    
    
for line in lines:
    line = line.strip()
    for wanna_word in target:
            warning_line = line.find(wanna_word)
            if warning_line != -1:
                fw.write(line+"\n")
                
            
    print(line)
    if not line: break