# Python Project: Smart Cashier
# A. Latar Belakang
Smart Cashier adalah sebuah program untuk memudahkan konsumen dalam melakukan transaksi belanja di Supermarket. Sistem kasir ini ditujukan agar konsumen dapat melakukan self-service. Fitur utama dari Smart Cashier adalah menambah item, harga dan jumlah.  

Python Project: Smart Cashier ini juga merupakan project yang dibuat dalam mengikuti course dari Pacmann Academy.

# B. Objektif 
Objektif dari Python Project: Smart Cashier ini adalah
  1) Membuat sistem yang memudahkan konsumen dalam melakukan pemesanan di Supermarket dari awal sampai akhir journey belanja.
  2) Membuat fitur utama seperti add_item (menambah item, jumlah dan harga).
  3) Membuat fitur pendukung seperti check_order (melihat rekap item) dan grand_total (melakukan analisa untuk eligibilitas atas diskon dan menampilkan jumlah nominal yang harus dibayar).
  4) Membuat fitur pendukung lainnya seperti update nama, item dan jumlah jika diperlukan untuk memperbaharui item dan atributnya.

 # C. Module
Ada 2 modul pada laman ini, yaitu:
1) Module 'cashier.py' = menampung class Transaction yang di dalamnya terdapat fungsi untuk menjalankan sistem Smart Cashier.
2) Module 'test case.py' = memiliki fungsi-fungsi dalam menjalankan test case sesuai dengan requirements dari tim Pacmann

# D. Flowchart

![Smart Cashier Flow Chart - Pacmannai](https://user-images.githubusercontent.com/84441275/230771028-f1f19602-a732-4e27-bf5a-25e9ce0de73f.png)

# E. Attribute dan Method

1. Attribute 'order' dengan tipe Dictionary, merupakan dictionary utama untuk menyimpan seluruh item, harga dan jumlah sebagai daftar belanja.
2. Attribut 'grand_total' adalah atribut untuk menampung jumlah dari sub total item belanja.
3. Method 'add_item' adalah method untuk menambahkan item ke dalam dictionary transaksi yang berisi 'nama_item' (str), 'jumlah_item' (int) dan 'harga_per_item' (int). inputan ini akan menghasilkan 'nama_item' sebagai Key dan 'jumlah_item' dan 'harga_per_item' sebagai values dari Key tersebut.
4. Method 'update_item_name' adalah method untuk mengubah nama item yang sudah terinput dengan parameter 'nama_item' dan 'nama_item_baru'.
5. Method 'update_harga_item' adalah method untuk mengubah harga item yang sudah terinput dengan parameter 'nama_item' dan 'harga_per_item'baru'.
6. Method 'update_jumlah_item' adalah method untuk mengubah jumlah item yang sudah terinput dengan parameter 'nama_item' dan 'jumlah_item'.
7. Method 'delete_item' adalah method untuk menghapus sebuah item dari daftar belanja dengan parameter 'nama_item'
8. Method 'reset_transaction' adalah method untuk menghapus semua item dari daftar belanja, sehingga dictionary 'order' menjadi 0.
9. Method 'check_order' adalah method untuk menampilkan tabel yang berisi daftar belanja yang berasal dari seluruh inputan dan perubahannya. Terdiri dari nama item, jumlah item, harga per item dan sub-total masing-masing item.
10. Method 'grand_total' adalah method untuk menentukan eligibilitas atas diskon dan menampilkan nominal akhir yang harus dibayar. Jika belanja lebih dari Rp 200.000,-, maka mendapatkan diskon 5%, belanja lebih dari Rp 300.000,- mendapat diskon 8% dan belanja lebih dari Rp 500.000,- mendapat diskon 10%.

# F. Test Case
**Test Case 1 - Method 'add_item'**

![add item](https://user-images.githubusercontent.com/84441275/230771722-a3f74bdf-1f8e-48e6-ab28-bcea0f0c9ffd.png)

**Test Case 2 - Method 'delete_item'**

![delete items](https://user-images.githubusercontent.com/84441275/230771734-fb28afb6-895f-40df-a933-08ec009fa976.png)

**Test Case 3 - Method 'reset_transaction'**

![reset transaction](https://user-images.githubusercontent.com/84441275/230771740-472f0cf9-787d-4f2f-a836-c5d53dfd86b0.png)

**Test Case 4 - Method 'check_order' dan 'grand_total'**

![check order dan grand total](https://user-images.githubusercontent.com/84441275/230771765-ec6585bc-cb9f-4061-94b1-a19e0bfbe6fd.png)


# G. Kesimpulan & Rekomendasi 
Project Python: Smart Cashier merupakan sistem kasir _self-sercive_ yang sangat sederhana. Dalam membuat sistem ini, ada beberapa hal yang menjadi pertimbangan dan kekhawatiran:

1. Tingginya resiko bagi konsumen untuk salah ketik dalam memasukan item, harga dan jumlah yang harus mengikuti bahasa pemograman phyton. Kedepannya, fitur input dapat digunakan untuk memudahkan _customer's journey_.
2. Sistem dapat dikoneksikan dengan inventory yang juga digunakan sebagai database, agar dapat meningkatkan efisiensi penjualan maupun proses logistik supermarket.
