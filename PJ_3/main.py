

def save_line(i, line):
    

try:
    with open("C:/Users/a5105/Desktop/vscode_pj/python/procedure1/PJ_3/1-3-Mars_Base_Inventory_List.csv", "r") as f:
        header = f.readline()
        
  

        
except FileNotFoundError:
    print("입력 파일 없음")
    data = []
except Exception as e:
    print("입력 오류",e)
    data = []
header = data[0]
body = data[1:]
body.so