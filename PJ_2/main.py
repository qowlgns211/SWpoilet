
data = []

with open("1-1-mission_computer_main.log", "r") as f:
    for line in f:
        row = line.strip().split(",")  
        data.append(row)

header = data[0]
body = data[1:]
body.sort(key=lambda x: x[0], reverse=True)

result = "{\n"
for row in body:
        result += f'    "{row[0]}": "{row[2]}",\n'
result = result.rstrip(',\n')+ "\n}"

with open("misson_log.json", "w") as f:
    f.write(result)
    
word = input("단어를 입력하세요: ")
found = False
with open("misson_log.json", "r") as f:
    for line in f:
        line = line.strip()
        if word.lower() in line.lower():
            print(line)
            found = True
if found == False:
    print("해당 단어를 포함한 문자가 없습니다.")