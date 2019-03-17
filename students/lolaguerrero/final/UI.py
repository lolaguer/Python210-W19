# Desc: Python 210 Final - User UI
# ChangeLog: (When,Who,What)
# 03/14/19, Lola Guerrero, Created Script

import tkinter as tk
from tkinter import ttk
import DataModel as DM
import DataProcessor as DP

class IOProcessor():

    # Products table
    @staticmethod
    def sel_product(text_widget):
        products = []
        pp = DP.ProductProcessor('Python210FinalDB.db')
        sql = pp.build_sel_code()
        for row in pp.execute_sql_code(sql):
            products.append(DM.Product(row[0], row[1]))
        pp.db_con.commit()
        pp.db_con.close()

        text_widget['state'] = 'normal'
        text_widget.delete(1.0, tk.END)

        if products is None:
            text_widget.insert("No data available")
        else:
            text_widget.insert(tk.END,"ProductID,ProductName\n")
            for row in products:
                text_widget.insert(tk.END, str(row) + "\n")

        text_widget['state'] = 'disabled'

    @staticmethod
    def ins_product(product_id, product_name, update_controls=[None]):
        pp = DP.ProductProcessor('Python210FinalDB.db')
        sql = pp.build_ins_code(product_id=product_id, product_name=product_name)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_product(update_controls[0])

    @staticmethod
    def upd_product(product_id, product_name, update_controls=[None]):
        pp = DP.ProductProcessor('Python210FinalDB.db')
        sql = pp.build_upd_code(product_id=product_id, product_name=product_name)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_product(update_controls[0])

    @staticmethod
    def del_product(product_id, update_controls=[None]):
        pp = DP.ProductProcessor('Python210FinalDB.db')
        sql = pp.build_del_code(product_id=product_id)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_product(update_controls[0])

    # Inventories table
    @staticmethod
    def sel_inventory(text_widget):
        inventories = []
        pp = DP.InventoryProcessor('Python210FinalDB.db')
        sql = pp.build_sel_code()
        for row in pp.execute_sql_code(sql):
            inventories.append(DM.Inventory(row[0], row[1]))
        pp.db_con.commit()
        pp.db_con.close()

        text_widget['state'] = 'normal'
        text_widget.delete(1.0, tk.END)

        if inventories is None:
            text_widget.insert("No data available")
        else:

            text_widget.insert(tk.END,"InventoryID,InventoryDate\n")
            for row in inventories:
                text_widget.insert(tk.END, str(row) + "\n")

        text_widget['state'] = 'disabled'

    @staticmethod
    def ins_inventory(inventory_id, inventory_date, update_controls=[None]):
        pp = DP.InventoryProcessor('Python210FinalDB.db')
        sql = pp.build_ins_code(inventory_id=inventory_id, inventory_date=inventory_date)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory(update_controls[0])

    @staticmethod
    def upd_inventory(inventory_id, inventory_date, update_controls=[None]):
        pp = DP.InventoryProcessor('Python210FinalDB.db')
        sql = pp.build_upd_code(inventory_id=inventory_id, inventory_date=inventory_date)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory(update_controls[0])

    @staticmethod
    def del_inventory(inventory_id, update_controls=[None]):
        pp = DP.InventoryProcessor('Python210FinalDB.db')
        sql = pp.build_del_code(inventory_id=inventory_id)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventory(update_controls[0])


    # InventoryCounts table
    @staticmethod
    def sel_inventorycount(text_widget):
        inventorycounts = []
        pp = DP.InventoryCountProcessor('Python210FinalDB.db')
        sql = pp.build_sel_code()
        for row in pp.execute_sql_code(sql):
            inventorycounts.append(DM.InventoryCount(row[0], row[1], row[2]))
        pp.db_con.commit()
        pp.db_con.close()

        text_widget['state'] = 'normal'
        text_widget.delete(1.0, tk.END)

        if inventorycounts is None:
            text_widget.insert("No data available")
        else:
            text_widget.insert(tk.END,"InventoryID,ProductID,Counts\n")
            for row in inventorycounts:
                text_widget.insert(tk.END, str(row) + "\n")

        text_widget['state'] = 'disabled'

    @staticmethod
    def ins_inventorycount(inventory_id, product_id, count, update_controls=[None]):
        pp = DP.InventoryCountProcessor('Python210FinalDB.db')
        sql = pp.build_ins_code(inventory_id=inventory_id, product_id=product_id, count=count)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventorycount(update_controls[0])

    @staticmethod
    def upd_inventorycount(inventory_id, product_id, count, update_controls=[None]):
        pp = DP.InventoryCountProcessor('Python210FinalDB.db')
        sql = pp.build_upd_code(inventory_id=inventory_id, product_id=product_id, count=count)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventorycount(update_controls[0])

    @staticmethod
    def del_inventorycount(inventory_id, product_id,update_controls=[None]):
        pp = DP.InventoryCountProcessor('Python210FinalDB.db')
        sql = pp.build_del_code(inventory_id=inventory_id, product_id=product_id)
        pp.execute_sql_code(sql)
        pp.db_con.commit()
        pp.db_con.close()
        if update_controls is not None:
            IOProcessor.sel_inventorycount(update_controls[0])

class MainWindow():
    """
    Desc: Creates the following UI objects
     -- window_root tk.TK
       -- notebook_frame ttk.Notebook
          -- tab_products tk.Frame
             -- lbl_product_info ttk.label
             -- btn_sel_product_info ttk.button
             -- mtx_product_info ttk.text
             -- lbl_product_id ttk.label
             -- txt_product_id ttk.entry
             -- lbl_product_name ttk.label
             -- txt_product_name ttk.entry
             -- btn_ins_product_info ttk.button
             -- btn_upd_product_info ttk.button
             -- btn_del_product_info ttk.button
          -- tab_inventories tk.Frame
          -- tab_inventory_counts tk.Frame
    """
    def __init__(self):
        self.window = tk.Tk()  # creates an root node
        self.window['padx'] = 10
        self.window['pady'] = 10
        self.notebook = ttk.Notebook(self.window)
        self.configure_notebook(self.notebook)  # create and configure tab container


    def configure_notebook(self, notebook_frame):
        notebook_frame.grid(row=4, column=2, sticky=tk.W, padx=20, pady=10)
        self.products_tab(notebook_frame)
        self.inventories_tab(notebook_frame)
        self.inventory_counts_tab(notebook_frame)
        return notebook_frame


    def products_tab(self, notebook_frame):
        tab_products = tk.Frame(notebook_frame)
        notebook_frame.add(tab_products, text="Products", compound=tk.TOP)

        btn_sel_product_info = ttk.Button(tab_products, text="Select Product Info", width=20)
        btn_sel_product_info.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        btn_sel_product_info["command"] = lambda: IOProcessor.sel_product(mtx_product_info)

        mtx_product_info = tk.Text(tab_products, width=55, height=10)
        mtx_product_info.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5, columnspan=3)

        lbl_product_id = ttk.Label(tab_products, text="Product ID ", width=20, anchor=tk.E)
        lbl_product_id.grid(row=4, column=1, sticky=tk.E)
        txt_product_id = ttk.Entry(tab_products, width=50)
        txt_product_id.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

        lbl_product_Name = ttk.Label(tab_products, text="Product Name ", width=20, anchor=tk.E)
        lbl_product_Name.grid(row=5, column=1, sticky=tk.E)
        txt_product_Name = ttk.Entry(tab_products, width=50)
        txt_product_Name.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

        btn_ins_product_info = ttk.Button(tab_products, text="Insert Product Info", width=20)
        btn_ins_product_info.grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)
        btn_ins_product_info["command"] = lambda: IOProcessor.ins_product(txt_product_id.get(),
                                                                          txt_product_Name.get(),
                                                                          [mtx_product_info])

        btn_upd_product_info = ttk.Button(tab_products, text="Update Product Info", width=20)
        btn_upd_product_info.grid(row=6, column=2, sticky=tk.EW, padx=5, pady=5)
        btn_upd_product_info["command"] = lambda: IOProcessor.upd_product(txt_product_id.get(),
                                                                          txt_product_Name.get(),
                                                                          [mtx_product_info])

        btn_del_product_info = ttk.Button(tab_products, text="Delete Product Info", width=20)
        btn_del_product_info.grid(row=6, column=3, sticky=tk.W, padx=5, pady=5)
        btn_del_product_info["command"] = lambda: IOProcessor.del_product(txt_product_id.get(),
                                                                          [mtx_product_info])

    def inventories_tab(self, notebook_frame):
        tab_inventories = tk.Frame(notebook_frame)
        notebook_frame.add(tab_inventories, text="Inventories", compound=tk.TOP)

        btn_sel_inventory_info = ttk.Button(tab_inventories, text="Select Inventory Info", width=20)
        btn_sel_inventory_info.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        btn_sel_inventory_info["command"] = lambda: IOProcessor.sel_inventory(mtx_inventory_info)

        mtx_inventory_info = tk.Text(tab_inventories, width=55, height=10)
        mtx_inventory_info.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5, columnspan=3)

        lbl_inventory_id = ttk.Label(tab_inventories, text="Inventory ID ", width=20, anchor=tk.E)
        lbl_inventory_id.grid(row=4, column=1, sticky=tk.E)
        txt_inventory_id = ttk.Entry(tab_inventories, width=50)
        txt_inventory_id.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

        lbl_inventory_Date = ttk.Label(tab_inventories, text="Inventory Date ", width=20, anchor=tk.E)
        lbl_inventory_Date.grid(row=5, column=1, sticky=tk.E)
        txt_inventory_Date = ttk.Entry(tab_inventories, width=50)
        txt_inventory_Date.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

        btn_ins_inventory_info = ttk.Button(tab_inventories, text="Insert Inventory Info", width=20)
        btn_ins_inventory_info.grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)
        btn_ins_inventory_info["command"] = lambda: IOProcessor.ins_inventory(txt_inventory_id.get(),
                                                                          txt_inventory_Date.get(),
                                                                          [mtx_inventory_info])

        btn_upd_inventory_info = ttk.Button(tab_inventories, text="Update Product Info", width=20)
        btn_upd_inventory_info.grid(row=6, column=2, sticky=tk.EW, padx=5, pady=5)
        btn_upd_inventory_info["command"] = lambda: IOProcessor.upd_inventory(txt_inventory_id.get(),
                                                                          txt_inventory_Date.get(),
                                                                          [mtx_inventory_info])

        btn_del_inventory_info = ttk.Button(tab_inventories, text="Delete Product Info", width=20)
        btn_del_inventory_info.grid(row=6, column=3, sticky=tk.W, padx=5, pady=5)
        btn_del_inventory_info["command"] = lambda: IOProcessor.del_inventory(txt_inventory_id.get(),
                                                                          [mtx_inventory_info])

    def inventory_counts_tab(self, notebook_frame):
        tab_inventory_counts = tk.Frame(notebook_frame)
        notebook_frame.add(tab_inventory_counts, text="Inventory Counts", compound=tk.TOP)

        btn_sel_inventory_counts_info = ttk.Button(tab_inventory_counts, text="Select Inventory Counts Info", width=20)
        btn_sel_inventory_counts_info.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        btn_sel_inventory_counts_info["command"] = lambda: IOProcessor.sel_inventorycount(mtx_inventory_counts_info)

        mtx_inventory_counts_info = tk.Text(tab_inventory_counts, width=55, height=10)
        mtx_inventory_counts_info.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5, columnspan=3)


        lbl_inventory_id = ttk.Label(tab_inventory_counts, text="Inventory ID ", width=20, anchor=tk.E)
        lbl_inventory_id.grid(row=4, column=1, sticky=tk.E)
        txt_inventory_id = ttk.Entry(tab_inventory_counts, width=50)
        txt_inventory_id.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

        lbl_product_id = ttk.Label(tab_inventory_counts, text="Product ID ", width=20, anchor=tk.E)
        lbl_product_id.grid(row=5, column=1, sticky=tk.E)
        txt_product_id = ttk.Entry(tab_inventory_counts, width=50)
        txt_product_id.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

        lbl_count = ttk.Label(tab_inventory_counts, text="Count ", width=20, anchor=tk.E)
        lbl_count.grid(row=6, column=1, sticky=tk.E)
        txt_count = ttk.Entry(tab_inventory_counts, width=50)
        txt_count.grid(row=6, column=2, padx=5, pady=5, columnspan=2)

        btn_ins_inventory_counts_info = ttk.Button(tab_inventory_counts, text="Insert Product Info", width=20)
        btn_ins_inventory_counts_info.grid(row=7, column=1, sticky=tk.W, padx=5, pady=5)
        btn_ins_inventory_counts_info["command"] = lambda: IOProcessor.ins_inventorycount(txt_inventory_id.get(),
                                                                                          txt_product_id.get(),
                                                                                          txt_count.get(),
                                                                                          [mtx_inventory_counts_info])

        btn_upd_inventory_counts_info = ttk.Button(tab_inventory_counts, text="Update Product Info", width=20)
        btn_upd_inventory_counts_info.grid(row=7, column=2, sticky=tk.EW, padx=5, pady=5)
        btn_upd_inventory_counts_info["command"] = lambda: IOProcessor.upd_inventorycount(txt_inventory_id.get(),
                                                                                          txt_product_id.get(),
                                                                                          txt_count.get(),
                                                                                          [mtx_inventory_counts_info])

        btn_del_inventory_counts_info = ttk.Button(tab_inventory_counts, text="Delete Product Info", width=20)
        btn_del_inventory_counts_info.grid(row=7, column=3, sticky=tk.W, padx=5, pady=5)
        btn_del_inventory_counts_info["command"] = lambda: IOProcessor.del_inventorycount(txt_inventory_id.get(),
                                                                                          txt_product_id.get(),
                                                                                          [mtx_inventory_counts_info])



if __name__ == '__main__':
    mw = MainWindow()
    mw.window.mainloop()



