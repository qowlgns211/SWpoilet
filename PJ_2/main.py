
data = []

try:
    with open("C:/Users/a5105/Desktop/vscode_pj/python/procedure1/PJ_2/1-1-mission_computer_main.log", "r") as f:
        for line in f:
            row = line.strip().split(",")  
            data.append(row)
except FileNotFoundError:
    print("입력 파일 없음")
    data=[]
except Exception as e:
    print("입력 오류", e)
    data=[]
    
header = data[0]
body = data[1:]
body.sort(key=lambda x: x[0], reverse=True)

result = "{\n"
for row in body:
        result += f'    "{row[0]}": "{row[2]}",\n'
result = result.rstrip(',\n')+ "\n}"

try:
    with open("misson_log.json", "w") as f:
        f.write(result)
except FileNotFoundError:
    print("출력력 파일 없음")
except Exception as e:
    print("기타 오류", e)
        
word = input("단어를 입력하세요: ")
found = False
try:
    with open("misson_log.json", "r") as f:
        for line in f:
            line = line.strip()
            if word.lower() in line.lower():
                print(line)
                found = True
except FileNotFoundError:
    print("출력 파일 없음")
except Exception as e:
    print("출력 에러",e)
if found == False:
    print("해당 단어를 포함한 문자가 없습니다.")