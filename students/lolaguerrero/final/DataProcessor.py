# Desc: Python 210 Final - Data Processor
# ChangeLog: (When,Who,What)
# 03/14/19, Lola Guerrero, Created Script

import sqlite3
from sqlite3 import Error as sqlErr
import re as rex
import datetime

class DBProcessor(object):

    def __init__(self, db_name: str=":memory:"): # Handy for testing!
        self.__db_name = db_name
        self.__db_con = self.create_connection(self.db_name)

    @property
    def db_name(self):  # Get DB Name
        return self.__db_name

    @property
    def db_con(self):  # Get Live Connection
        return self.__db_con

    # SQL Validators
    @staticmethod
    def check_for_extra_semicolon(sql_str):
        """Checks for an extra semicolon"""
        try:
            if len(sql_str.split(';')) > 2:
                raise sqlErr("Extra Semi-Colon Detected!")
        except Exception as e:
            raise e

    @staticmethod
    def check_for_or(sql_str):
        """Checks for an injected OR in tampered WHERE Clause"""
        sql_str = sql_str.lower()
        try:
            if rex.search("where", sql_str, rex.IGNORECASE):  # If it has a Where clause
                if rex.search(' or ', sql_str.split('where')[1], rex.IGNORECASE) is not None:  #  injected OR?
                    raise sqlErr("OR Detected!")
        except Exception as e:
            raise e

    @staticmethod
    def check_for_and(sql_str):
        """Checks for an injected OR in tampered WHERE Clause"""
        sql_str = sql_str.lower()
        try:
            if rex.search("where", sql_str, rex.IGNORECASE):  # If it has a Where clause
                if rex.search(' and ', sql_str.split('where')[1], rex.IGNORECASE) is not None:  #  injected AND?
                    raise sqlErr("AND Detected!")
        except Exception as e:
            raise e

    @staticmethod
    def check_for_date(date_str):
        """Checks for an valid date string"""
        try:
            if rex.match("\d\d\d\d-\d\d-\d\d", str(date_str)) is None:
                raise sqlErr("Not a Date!")
        except Exception as e:
            raise e

    @staticmethod
    def remove_multiple_spaces(name_str):
        """Remove multiple spaces in a given string"""
        return rex.sub(' +', ' ', name_str).strip()


    def create_connection(self, db_file: str):
        """ Create or connect to a SQLite database """
        try:
            con = sqlite3.connect(db_file)
        except sqlErr as se:
            raise Exception('SQL Error in create_connection(): ' + se.__str__())
        except Exception as e:
            raise Exception('General Error in create_connection(): ' + e.__str__())
        return con


    def execute_sql_code(self, sql_code: str = ''):
        """ Execute SQL code on a open connection """
        db_con = self.db_con
        try:
            if db_con is not None and sql_code != '':
                # Validate
                self.check_for_extra_semicolon(sql_code);
                self.check_for_or(sql_code);

                # Connect and Run
                with db_con:
                    csr = db_con.cursor()
                    csr.execute(sql_code)
            else:
                raise Exception('SQL Code or Connection is missing!')
        except sqlErr as se:
            #print ('SQL Error in execute_sql_code(): ' + se.__str__())
            raise Exception('SQL Error in execute_sql_code(): ' + se.__str__())
        except Exception as e:
            raise Exception('General Error in execute_sql_code(): ' + e.__str__())
        return csr

    def build_ins_code(self):
        # Validate Input
        sql = str.format("INSERT Not Implemented Yet")
        return sql

    def build_upd_code(self):
        # Validate Input
        sql = str.format("UPDATE Not Implemented Yet")
        return sql

    def build_del_code(self):
        # Validate Input
        sql = str.format("DELETE Not Implemented Yet")
        return sql

    def build_sel_code(self):
        # Validate Input
        sql = str.format("SELECT Not Implemented Yet")
        return sql



class InventoryProcessor(DBProcessor):

    def build_ins_code(self, inventory_id: int, inventory_date: datetime.date):
        DBProcessor.check_for_date(inventory_date)
        sql = str.format("INSERT INTO Inventories (InventoryID, InventoryDate) "
                         "VALUES ({id},'{date}');", id=inventory_id, date=inventory_date)
        return sql

    def build_upd_code(self, inventory_id: int, inventory_date: datetime.date):
        DBProcessor.check_for_date(inventory_date)
        sql = str.format("UPDATE Inventories SET InventoryDate = '{date}' "
                         "WHERE InventoryID = {id};", id=inventory_id, date=inventory_date)
        return sql

    def build_del_code(self, inventory_id: int):
        sql = str.format("DELETE FROM Inventories "
                         "WHERE InventoryID = {id};", id=inventory_id)
        return sql

    def build_sel_code(self, inventory_id: int = None):
        if inventory_id is not None:
            w = ' WHERE InventoryID = ' + str(inventory_id)
        else:
            w = ''
        sql = str.format("SELECT InventoryID, InventoryDate "
                         "FROM Inventories{WHERE};", WHERE=w)
        return sql



class ProductProcessor(DBProcessor):

    def build_ins_code(self, product_id: int, product_name: str):
        DBProcessor.remove_multiple_spaces(product_name)
        try:
            sql = str.format("INSERT INTO Products (ProductID, ProductName) "
                             "VALUES ({id},'{name}');", id=product_id, name=product_name)
            return sql
        except MySQLdb.Error as e:
            if str(e) == 'UNIQUE constraint failed: Products.ProductID':

    def build_upd_code(self, product_id: int, product_name: str):
        DBProcessor.remove_multiple_spaces(product_name)
        sql = str.format("UPDATE Products SET ProductName = '{name}' "
                     "WHERE ProductID = {id};", id=product_id, name=product_name)
        return sql

    def build_del_code(self, product_id: int):
        sql = str.format("DELETE FROM Products WHERE ProductID = {id};", id=product_id)
        return sql

    def build_sel_code(self, product_id: int = None):
        if product_id is not None:
            w = ' WHERE ProductID = ' + str(product_id)
        else:
            w = ''
        sql = str.format("SELECT ProductID, ProductName  "
                         "FROM Products{WHERE};", WHERE=w)
        return sql



class InventoryCountProcessor(DBProcessor):

    def build_ins_code(self, inventory_id: int, product_id: int, count: int):
        sql = str.format("INSERT INTO InventoryCounts (InventoryID, ProductID, Count) "
                         "VALUES ({id_inv},{id_prod},'{cnt}');", id_inv=inventory_id, id_prod=product_id, cnt=count)
        return sql

    def build_upd_code(self, inventory_id: int, product_id: int, count: int):
        print ('HERE')
        sql = str.format("UPDATE InventoryCounts SET Count = '{cnt}' "
                         "WHERE InventoryID = {id_inv} AND ProductID = {id_prod};", id_inv=inventory_id, id_prod=product_id, cnt=count)
        return sql

    def build_del_code(self, inventory_id: int, product_id: int):
        if inventory_id is None:
            sql = str.format("DELETE FROM InventoryCounts WHERE ProductID = {id_prod};", id_prod=product_id)
        elif product_id is None:
            sql = str.format("DELETE FROM InventoryCounts WHERE InventoryID = {id_inv};", id_inv=inventory_id)
        else:
            sql = str.format("DELETE FROM InventoryCounts WHERE InventoryID = {id_inv} AND ProductID = {id_prod};",
                             id_inv=inventory_id, id_prod=product_id)
        return sql

    def build_sel_code(self, inventory_id: int = None, product_id: int = None):

        if (inventory_id is None) and (product_id is not None):
            sql = str.format("SELECT InventoryID, ProductID, Count FROM InventoryCounts WHERE ProductID = {id_prod};", id_prod=product_id)
        elif (inventory_id is not None) and (product_id is None):
            sql = str.format("SELECT InventoryID, ProductID, Count FROM InventoryCounts WHERE InventoryID = {id_inv};", id_inv=inventory_id)
        elif(inventory_id is None) and (product_id is None):
            sql = "SELECT InventoryID, ProductID, Count FROM InventoryCounts"
        else:
            sql = str.format("SELECT InventoryID, ProductID, Count FROM InventoryCounts WHERE InventoryID = {id_inv} AND ProductID = {id_prod};", id_inv=inventory_id,  id_prod=product_id)
        return sql