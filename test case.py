#!/usr/bin/env python
# coding: utf-8

# In[5]:


import cashier #perintah untuk impor modul cashier.py


# In[6]:


transaction_124 = cashier.Transaction() #inisiasi test case


# In[19]:


# Test Case 1 : Method Add Item
print('Test Case : Add Items')

transaction_124.add_item('Ayam Goreng', 2, 20_000)
transaction_124.add_item('Pasta Gigi', 3, 15_000) 
print('Item ditambahkan:', transaction_124.order)


# In[20]:


# Test Case 2 : Method Delete Items
print('Test Case 2 : Delete Items')

transaction_124.delete_item('Pasta Gigi')
transaction_124.check_order() 


# In[21]:


# Test Case 3 : Method Reset Transaction
print('Test Case 3: Reset Transaction')
transaction_124.reset_transaction()


# In[22]:


# Test Case 4 : Method Check Order & Grand Total
print('Test Case 4: Grand Total & Amount to be Paid')
transaction_124.add_item('Ayam Goreng', 2, 20_000)
transaction_124.add_item('Pasta Gigi', 3, 15_000) 
transaction_124.add_item('Mainan Mobil', 1, 200_000)
transaction_124.add_item('Mi Instan', 5, 3_000)
transaction_124.check_order()
transaction_124.grand_total()

