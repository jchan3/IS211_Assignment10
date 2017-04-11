#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for Joe Chan: query_pets.py"""


import sqlite3 as lite
import sys


con = lite.connect('pets.db')


with con:

    cur = con.cursor()

    sql = "SELECT * FROM pet \
            INNER JOIN person_pet ON pet.id = person_pet.pet_id \
            WHERE person_pet.person_id=:id"

    uid = raw_input("Enter person's ID number (or -1 to quit): ")
    while uid != "-1":
        try:
            cur.execute("SELECT * FROM person WHERE id=:id",
                        {"id": uid})
            rows = cur.fetchall()
            for row in rows:
                personid = row [0]
                fname = row[1]
                lname = row[2]
                age = row[3]
                print fname, lname + ",", str(age) + " years old"
            if rows == []:
                print "Error: ID not found."

            cur.execute(sql,{"id": uid})
            rows2 = cur.fetchall()
            for row in rows2:
                petid = row [0]
                name = row[1]
                breed = row[2]
                age = row[3]
                dead = row[4]
                print fname, lname + " owned", name + ", a", breed + ", that was", str(age) + " years old"
        except:
            print "Error: ID not found."
        uid = raw_input("Enter person's ID number (or -1 to quit): ")
