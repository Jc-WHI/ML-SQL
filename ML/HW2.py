import pymysql
from tkinter import *

def selectData():
    # 데이터베이스 연결 (호스트, 사용자, 비밀번호, 데이터베이스명 수정)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='5294', db='market_db', charset='utf8')
    cur = conn.cursor()

    # SELECT 쿼리 실행
    cur.execute("SELECT * FROM member")
    rows = cur.fetchall()

    # 리스트 박스 초기화
    listData1.delete(0, END)
    listData2.delete(0, END)
    listData3.delete(0, END)
    listData4.delete(0, END)

    # 조회한 데이터 리스트 박스에 추가
    for row in rows:
        listData1.insert(END, row[0])  # 사용자 ID
        listData2.insert(END, row[1])  # 사용자 이름
        listData3.insert(END, row[2])  # 사용자 이메일
        listData4.insert(END, row[3])  # 사용자 출생연도

    conn.close()

def insertData():
    # 데이터베이스 연결 (호스트, 사용자, 비밀번호, 데이터베이스명 수정)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='5294', db='market_db', charset='utf8')
    cur = conn.cursor()

    # 입력 위젯에서 데이터 가져오기
    data1 = edt1.get()
    data2 = edt2.get()
    data3 = edt3.get()
    data4 = edt4.get()

    # Insert data into the member table
    sql = "INSERT INTO member VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (data1, data2, data3, data4))
    conn.commit()

    conn.close()
    messagebox.showinfo('성공', '데이터 입력 성공')
    selectData()  # 입력 후 자동 조회

def deleteData():
    # 데이터베이스 연결 (호스트, 사용자, 비밀번호, 데이터베이스명 수정)
    conn = pymysql.connect(host='127.0.0.1', user='root', password='5294', db='market_db', charset='utf8')
    cur = conn.cursor()

    # 선택한 사용자 ID 가져오기
    selected_id = listData1.get(listData1.curselection())

    # member 테이블에서 해당 ID 데이터 삭제
    sql = "DELETE FROM member WHERE 사용자ID = %s"
    cur.execute(sql, (selected_id,))
    conn.commit()

    conn.close()
    messagebox.showinfo('성공', '데이터 삭제 성공')
    selectData()  # 삭제 후 자동 조회

# 메인 윈도우 생성
root = Tk()
root.title("Market Database Program")
root.geometry("800x600")

# 입력 위젯 생성
edt1 = Entry(root, width=10)
edt2 = Entry(root, width=10)
edt3 = Entry(root, width=10)
edt4 = Entry(root, width=10)

# 버튼 생성
btnInsert = Button(root, text="입력", command=insertData)
btnSelect = Button(root, text="조회", command=selectData)
btnDelete = Button(root, text="삭제", command=deleteData)

# 리스트 박스 생성
listData1 = Listbox(root, bg='yellow')
listData2 = Listbox(root, bg='yellow')
listData3 = Listbox(root, bg='yellow')
listData4 = Listbox(root, bg='yellow')

# 위젯 배치
edt1.pack(side=LEFT, padx=10, pady=10)
edt2.pack(side=LEFT, padx=10, pady=10)
edt3.pack(side=LEFT, padx=10, pady=10)
edt4.pack(side=LEFT, padx=10, pady=10)
btnInsert.pack(side=LEFT, padx=10, pady=10)
btnSelect.pack(side=LEFT, padx=10, pady=10)
btnDelete.pack(side=LEFT, padx=10, pady=10)
listData1.pack(fill=BOTH, expand=1)
listData2.pack(fill=BOTH, expand=1)
listData3.pack(fill=BOTH, expand=1)
listData4.pack(fill=BOTH, expand=1)
root.mainloop()