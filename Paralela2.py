#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors

con = pymysql.connect(host='192.168.56.101',
                      user='admin',
                      password='admin123',
                      db='Contatos',
                      charset='utf8',
                      cursorclass=pymysql.cursors.DictCursor)

with con:
    reiniciar = 0
    while reiniciar == 0:
        cur = con.cursor()

        #__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#

        print("Adicionar Contato ?")
        x = input()

        if x == "sim" or x == "Sim" or x == "S" or x=="s":
            nome = input()
            sobrenome = input()
            dataDia = input()
            dataMes = input()
            dataAno = input()
            telefone = input()
            cur.execute("INSERT INTO Contatos.Lista(`Nome`, `Sobrenome`, `Data`, `Telefone`) VALUES('", nome ,"' ,'", sobrenome, "' ,'", data, "' ,'" ,telefone, "')")
            cur.execute("SELECT * FROM Contatos")

        #__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#

        print("Atualizar Contato?")


        m = input()
        if m == "sim" or m == "Sim" or m == "S" or m == "s":
            print("qual contato(id)?")
            q = int(input())
            nome = input()
            sobrenome = input()
            data = input()
            telefone = input()
            cur.execute("UPDATE Lista SET `Nome` = '",nome,"', `Sobrenome` = '",Sobrenome,"', `Data` = '",data,"', `Telefone` = '",telefone,"', WHERE =",id,";")

        #___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#

        print("Ordenar por Nome?")


        m = input()
        if m == "sim" or m == "Sim" or m == "S" or m == "s":
          cur.execute("Select * From Lista Where `Nome` LIKE "A%" Order By `Nome` ASC;")

        #___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#
        
        print("Ordenar por Sobrenome?")


        m = input()
        if m == "sim" or m == "Sim" or m == "S" or m == "s":
          cur.execute("Select * From `Lista` Where `Sobrenome` LIKE "A%" Order By `Sobrenome` ASC;")

        #___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#

        print("Ordenar por Data de Nascimento?")
        y = input()
        if y == "sim" or y == "Sim" or y == "S" or y == "s":
          cur.execute("Select * From `Lista` Where `Data` LIKE "A%" Order By `Data` ASC;")

        #______________________________________________________________________________________________________________________________________________#
        
        print("Excluir Contato ?")
        y = input()
        if y == "sim" or y == "Sim" or y == "S" or y == "s":
            print("Qual(selecione o id)?")
            n = input()
            cur.execute("DELETE FROM `Lista` WHERE `id` = ", n ,";")

        #______________________________________________________________________________________________________________________________________________#

        rows = cur.fetchall()


        for row in rows:
            print(row["Nome"], row["Sobrenome"], row["DataDia"],'/',row["DataMes"],'/',row["DataAno"], row["Telefone"], row["id"])

        #______________________________________________________________________________________________________________________________________________#

        print("Fechar programa?")
        z = input()
        if z == "sim" or z == "Sim" or z == "S" or z == "s":
            reiniciar = 1
