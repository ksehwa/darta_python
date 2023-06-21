import csv, re

def opencsv(filename):
    f= open(filename, 'r', encoding = 'cp949')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output


def writecsv(filename, the_list):                  # 첫 번째 변수는 파일이름, 두번째 변수는 CSV형 리스트를 저장한 객체 
    with open(filename, 'w', newline='', encoding = 'cp949') as f:     # 파일을 닫기 위해 whitt문 사용
        a = csv.writer(f, delimiter=',')
        a.writerows(the_list)


def switch(listName):                             # 예외처리로 숫자만 골라서 숫자형으로 변경하는 함수
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',','', j))
            except:
                pass
    return listName        
     
