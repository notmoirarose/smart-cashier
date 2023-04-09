


import pandas as pd #impor panda untuk membuat tabel

class Transaction():
    ''' Class ini merupakan penampung modul transaksi dan menjalankan fungsi kasir, untuk menghasilkan tampilan yang  '''
    def __init__(self): #inisiasi kelas untuk menampung item, harga dan jumlah
        self.order = dict()
      
    def add_item(self, nama_item : str, jumlah_item : int, harga_per_item : int): #fungsi untuk menambah item
        try:
            self.order[nama_item] = [jumlah_item, harga_per_item, jumlah_item * harga_per_item]
            print(f'Item yang dipesan adalah {nama_item} sebanyak {jumlah_item} dengan harga per item Rp {harga_per_item}')
        except TypeError: #menghindari penginputan jumlah yang salah, sehingga tidak mendapat output error untuk sub total
            print('Format inputan salah') 
        except SyntaxError:
            print('Format inputan salah')
            
             
    def update_nama_item(self, nama_item, nama_item_baru): #fungsi untuk memperbaharui nama
        try:
            self.order[nama_item_baru] = self.order.pop(nama_item)
            print(f'Berhasil memperbaharui item menjadi item {nama_item_baru}')
        except KeyError:
            print('Item tidak ditemukan')
        
    def update_jumlah_item(self, nama_item, jumlah_item_baru): # fungsi untuk memperbaharui jumlah
        try:
            self.order[nama_item][0] = jumlah_item_baru
            self.order[nama_item][2] = jumlah_item_baru * self.order[nama_item][1]
            print(f'Berhasil memperbaharui jumlah {nama_item} menjadi sebanyak {harga_per_item_baru}')
        except KeyError:
            print('Item tidak ditemukan')
        
    def update_harga_item(self, nama_item, harga_per_item_baru): #fungsi untuk memperbaharui harga per item
        try:
            self.order[nama_item][1] = harga_per_item_baru
            self.order[nama_item][2] = self.order[nama_item][0] * harga_per_item_baru
        except KeyError:
            print('Item tidak ditemukan')
        
    def check_order(self): #fungsi untuk melihat daftar order sementara
        if len(self.order) == 0:
            print('Terdapat kesalahan input data')
        else:
            daftar_belanja = pd.DataFrame(self.order).T #membuat tabel. fungsi transpose untuk menyusun tabel secara horizontal
            daftar_belanja.columns = ['Jumlah', 'Harga Satuan', 'Sub-Total']
            print(daftar_belanja.to_markdown())
            print('Jika sudah benar, dapat dilanjutkan untuk melihat total pembayaran')
        
    def delete_item(self, nama_item): #fungsi untuk menghapus item
        self.nama_item = nama_item
        if nama_item == nama_item:
            try:
                self.order.pop(nama_item)
                print('Item berhasil dihapus')
            except:
                print('Item tidak ditemukan')
                
    def reset_transaction(self): #fungsi untuk menghapus semua item dalam daftar
        self.order.clear()
        print('Transaksi dihapus. Silahkan mengulangi pengisian barang atau mengakhiri program')
        
    def grand_total(self): #fungsi untuk mendapatkan total pembayaran yg harus dibayar

        grand_total = 0
        for i in self.order.values():
            grand_total += i[2]

        #eligibility untuk diskon ditentukan dengan fungsi if elif & else terhadap total belanja (grand total)
        
        if grand_total > 500000:
            grand_total *= 0.9
            print(f"Selamat! Anda mendapat diskon. Total yang harus dibayar adalah {grand_total}")
        elif grand_total > 300000:
            grand_total *= 0.92
            print(f"Selamat! Anda mendapat diskon. Total yang harus dibayar adalah {grand_total}")
        elif grand_total > 200000:
            grand_total *= 0.95
            print(f"Selamat! Anda mendapat diskon. Total yang harus dibayar adalah {grand_total}")
        elif grand_total < 200000:
            grand_total = grand_total
            print(f"Total yang harus dibayar adalah {grand_total}")
        else:
            print("Transaksi belum diinput")
        