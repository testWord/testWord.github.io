#!/usr/bin/python  
#coding:gbk  
import pymysql  
from builtins import int  
  
#��MysqlHelper�ļ�������д����  
  
def  connDB():
#�������ݿ�
    conn=pymysql.connect(host="localhost",user="root",passwd="",db="student",charset='utf8mb4',);
    cur=conn.cursor();  
    return (conn,cur);
def exeUpdate(conn,cur,sql):
#���»�������
    sta=cur.execute(sql);  
    conn.commit();  
    return (sta);  
  
def exeDelete(conn,cur,IDs):
#ɾ������
    sta=0;  
    for eachID in IDs.split(' '):  
        sta+=cur.execute("delete from students where Id=%d"%(int(eachID)));  
    conn.commit();  
    return (sta);  
          
def exeQuery(cur,sql):
#���Ҳ���
    cur.execute(sql);  
    return (cur);  
      
def connClose(conn,cur):
#�ر����ӣ��ͷ���Դ
    cur.close();  
    conn.close();  
  
result=True;  
print("��ѡ�������ĸ�������1���޸ļ�¼��2�����Ӽ�¼��3����ѯ��¼��4��ɾ����¼.(��qΪ�˳�)");  
conn,cur=connDB();  
number=input();  
while(result):  
    if(number=='q'):  
        print("��������");  
        break;  
    elif(int(number)==1):  
        sql=input("�����������䣺");  
        try:  
            exeUpdate(conn, cur, sql);  
            print("���³ɹ�");  
        except Exception:  
            print("����ʧ��");  
            raise;  
    elif(int(number)==2):  
            sql=input("�������������:");  
            try:  
                exeUpdate(conn, cur, sql);  
                print("�����ɹ�");  
            except Exception:  
                print("����ʧ��");  
                raise;  
    elif(int(number)==3):  
        sql=input("�������ѯ��䣺");  
        try:  
            cur=exeQuery(cur, sql);  
            for item in cur:  
                print("Id="+str(item[0])+" name="+item[1]);  
        except Exception:  
            print("��ѯ����");  
            raise;  
    elif(int(number)==4):  
        Ids=input("������Id�����ÿո����");  
        try:  
            exeDelete(conn, cur, Ids);  
            print("ɾ���ɹ�");  
        except Exception:  
            print("ɾ��ʧ��");  
            raise;  
    else:  
        print("�Ƿ����룬����������!");  
        result=False;  
        break;  
    print("��ѡ�������ĸ�������1���޸ļ�¼��2�����Ӽ�¼��3����ѯ��¼��4��ɾ����¼.(��qΪ�˳�)");  
    number=input("��ѡ�����");  