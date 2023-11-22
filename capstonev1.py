from prettytable import PrettyTable
# Data murid
list_murid = [['Adi', 30162324001, None, None, None, None, None, None],
              ['Bilal', 30162324002, None, None, None, None, None, None],
              ['Chandra', 30162324003, None, None, None, None, None, None],
              ['Doni', 30162324004, None, None, None, None, None, None],
              ['Emil', 30162324005, None, None, None, None, None, None],
              ['Gita', 30162324006, None, None, None, None, None, None],
              ['Fajar', 30162324007, None, None, None, None, None, None],
              ['Junaidi', 30162324008, None, None, None, None, None, None],
              ['Kiara', 30162324009, None, None, None, None, None, None],
              ['Lina', 30162324010, None, None, None, None, None, None],
              ['Mahmudi', 30162324011, None, None, None, None, None, None],
              ['Nanda', 30162324012, None, None, None, None, None, None],
              ['Omar', 30162324013, None, None, None, None, None, None],
              ['Puti', 30162324014, None, None, None, None, None, None],
              ['Quenn', 30162324015, None, None, None, None, None, None],
              ['Rania', 30162324016, None, None, None, None, None, None],
              ['Santika', 30162324017, None, None, None, None, None, None],
              ['Tamara', 30162324018, None, None, None, None, None, None],
              ['Umar', 30162324019, None, None, None, None, None, None],
              ['Vanya', 30162324020, None, None, None, None, None, None],
              ['Wanda', 30162324021, None, None, None, None, None, None],
              ['Xavier', 30162324022, None, None, None, None, None, None],
              ['Yugo', 30162324023, None, None, None, None, None, None],
              ['Zainal', 30162324024, None, None, None, None, None, None]]


# menampilkan daftar nilai
def daftar_nilai():
    table = PrettyTable()
    table.field_names = ['Index', 'Nama', 'NIM', 'Bahasa Indonesia', 'Matematika', 'Bahasa Inggris', 'Biologi', 'Fisika', 'Kimia', 'Jumlah Nilai', 'Rata-rata']

    for i in range(len(list_murid)):
        jumlah_nilai, rata_rata = hitung_rata_nilai(list_murid[i][2:8])
        table.add_row([i, list_murid[i][0], list_murid[i][1], format_nilai(list_murid[i][2]), format_nilai(list_murid[i][3]),
                       format_nilai(list_murid[i][4]), format_nilai(list_murid[i][5]), format_nilai(list_murid[i][6]),
                       format_nilai(list_murid[i][7]), jumlah_nilai, rata_rata])

    print('\nDaftar Murid\n')
    print(table)

# mengubah None pada nilai mapel menjadi Belum diisi
def format_nilai(nilai):
    return 'Belum diisi' if nilai is None else str(nilai).ljust(10)


# memasukkan nilai
def masukkan_nilai():
    daftar_nilai()
    try:
        index = int(input('\nMasukkan indeks murid yang ingin dimasukkan nilai: '))
        if 0 <= index < len(list_murid):
            for i in range(2, 8):
                while True:
                    nilai = float(input(f'Masukkan nilai {get_mata_pelajaran(i)} untuk {list_murid[index][0]}: '))
                    if 0 <= nilai <= 100:
                        list_murid[index][i] = nilai
                        print(f'Nilai untuk {list_murid[index][0]} berhasil dimasukkan.')
                        break
                    else:
                        print('Nilai harus berada di antara 0 dan 100. Silakan masukkan kembali.')
        else:
            print('Indeks tidak valid.')
    except ValueError:
        print('Input tidak valid. Masukkan indeks dalam bentuk angka.')


# daftar mata pelajaran
def get_mata_pelajaran(index):
    mata_pelajaran = {
        2: 'Bahasa Indonesia',
        3: 'Matematika',
        4: 'Bahasa Inggris',
        5: 'Biologi',
        6: 'Fisika',
        7: 'Kimia'
    }
    return mata_pelajaran.get(index, 'Mata Pelajaran Tidak Valid')


# menghitung jumlah dan rata-rata nilai
def hitung_rata_nilai(nilai_list):
    nilai_list = [nilai for nilai in nilai_list if nilai is not None]
    jumlah_nilai = sum(nilai_list)
    rata_rata = jumlah_nilai / len(nilai_list) if len(nilai_list) > 0 else 0
    return jumlah_nilai, rata_rata


# mengganti nilai
def ubah_nilai():
    daftar_nilai()
    try:
        index = int(input('\nMasukkan indeks murid yang ingin diubah nilai: '))
        if 0 <= index < len(list_murid):
            while True:
                mata_pelajaran = int(input('Masukkan mata pelajaran yang ingin diubah (Contoh: "Bahasa Indonesia" -> 2): '))
                if 2 <= mata_pelajaran <= 7:
                    while True:
                        nilai_baru = float(input(f'Masukkan nilai baru untuk {list_murid[index][0]} ({get_mata_pelajaran(mata_pelajaran)}): '))
                        if 0 <= nilai_baru <= 100:
                            konfirmasi = input(f'Apakah Anda yakin ingin mengubah nilai {get_mata_pelajaran(mata_pelajaran)} untuk {list_murid[index][0]} menjadi {nilai_baru}? (ya/tidak): ')
                            if konfirmasi.lower() == 'ya':
                                list_murid[index][mata_pelajaran] = nilai_baru
                                print(f'Nilai {get_mata_pelajaran(mata_pelajaran)} untuk {list_murid[index][0]} berhasil diubah: {nilai_baru}')
                                break
                            elif konfirmasi.lower() == 'tidak':
                                print(f'Perubahan nilai {get_mata_pelajaran(mata_pelajaran)} dibatalkan.')
                                break
                            else:
                                print('Jawaban tidak valid. Masukkan "ya" atau "tidak".')
                        else:
                            print('Nilai harus berada di antara 0 dan 100. Silakan masukkan kembali.')
                    break
                else:
                    print('Mata pelajaran tidak valid.')
        else:
            print('Indeks tidak valid.')
    except ValueError:
        print('Input tidak valid. Masukkan indeks dan nilai dalam bentuk angka.')


# menghapus nilai
def hapus_nilai():
    daftar_nilai()
    try:
        index = int(input('\nMasukkan indeks murid yang ingin dihapus nilai: '))
        if 0 <= index < len(list_murid):
            while True:
                mata_pelajaran = int(input('Masukkan mata pelajaran yang ingin dihapus nilai (Contoh: "Bahasa Indonesia" -> 2) (ya/tidak): '))
                if 2 <= mata_pelajaran <= 7:
                    while True:
                        jawaban = input(f'Anda yakin ingin menghapus nilai {get_mata_pelajaran(mata_pelajaran)} untuk {list_murid[index][0]}? (ya/tidak): ')
                        if jawaban.lower() == 'ya':
                            list_murid[index][mata_pelajaran] = None
                            print(f'Nilai {get_mata_pelajaran(mata_pelajaran)} untuk {list_murid[index][0]} berhasil dihapus.')
                            break
                        elif jawaban.lower() == 'tidak':
                            break
                        else:
                            print('Jawaban tidak valid. Masukkan "ya" atau "tidak".')
                    break
                else:
                    print('Mata pelajaran tidak valid.')
        else:
            print('Indeks tidak valid.')
    except ValueError:
        print('Input tidak valid. Masukkan indeks dalam bentuk angka.')


# menyortir data
def sortir_rata_rata():
    sorted_list = sorted(list_murid, key=lambda x: hitung_rata_nilai(x[2:8])[1], reverse=True)
    print('\nDaftar Murid setelah diurutkan berdasarkan rata-rata nilai\n')
    print('Index   | Nama          | NIM           | Bahasa Indonesia(2)   | Matematika(3) | Bahasa Inggris(4)  | Biologi(5) | Fisika(6) | Kimia(7) | Jumlah Nilai  | Rata-rata')
    for i in range(len(sorted_list)):
        jumlah_nilai, rata_rata = hitung_rata_nilai(sorted_list[i][2:8])
        print(f'{i}\t| {sorted_list[i][0]:<15}| {sorted_list[i][1]:<15}| {format_nilai(sorted_list[i][2])}\t| {format_nilai(sorted_list[i][3])}\t| {format_nilai(sorted_list[i][4])}\t| {format_nilai(sorted_list[i][5])}\t| {format_nilai(sorted_list[i][6])}\t| {format_nilai(sorted_list[i][7])}\t| {jumlah_nilai}\t| {rata_rata}')


# pencarian data
def cari_nama_by_nim():
    try:
        nim_cari = int(input('\nMasukkan NIM yang ingin dicari: '))
        for murid in list_murid:
            if murid[1] == nim_cari:
                table = PrettyTable()
                table.field_names = ['Mata Pelajaran', 'Nilai']

                print(f'\nData Murid dengan NIM {nim_cari}\n')
                print('Nama:', murid[0])
                for i in range(2, 8):
                    nilai = murid[i]
                    table.add_row([get_mata_pelajaran(i), format_nilai(nilai)])

                print(table)

                total_nilai = sum(nilai for nilai in murid[2:8] if nilai is not None)
                count_nilai = len([nilai for nilai in murid[2:8] if nilai is not None])

                if count_nilai > 0:
                    rata_rata = total_nilai / count_nilai
                    print(f'\nJumlah Nilai\t\t{total_nilai}\nRata-rata\t\t{rata_rata}')
                else:
                    print('\nJumlah Nilai\t\tBelum diisi\nRata-rata\t\tBelum diisi')
                return
        print(f'Tidak ditemukan murid dengan NIM {nim_cari}.')
    except ValueError:
        print('Input tidak valid. Masukkan NIM dalam bentuk angka.')


# Memanggil fungsi
while True:
    print('''
        Selamat datang di Sistem E-Rapor
        List Menu Utama:
        1. Daftar Nilai Murid
        2. Sortir Rata-rata
        3. Masukkan Nilai
        4. Ubah Nilai
        5. Hapus Nilai
        6. Keluar Program
    ''')

    pilihan_menu_utama = input('Masukkan angka menu yang Anda pilih: ')

    if pilihan_menu_utama == '1':
        while True:
            print('''
                Submenu Daftar Nilai Murid:
                1. Tampilkan Daftar Nilai
                2. Cari Nama berdasarkan NIM
                0. Kembali ke Menu Utama
            ''')
            pilihan_submenu = input('Masukkan angka submenu yang Anda pilih: ')

            if pilihan_submenu == '1':
                daftar_nilai()
            elif pilihan_submenu == '2':
                cari_nama_by_nim()
            elif pilihan_submenu == '0':
                break
            else:
                print('Submenu tidak valid. Silakan pilih angka yang sesuai.')

    elif pilihan_menu_utama == '2':
        while True:
            print('''
                Submenu Sortir Rata-rata:
                1. Tampilkan Daftar Nilai setelah diurutkan
                0. Kembali ke Menu Utama
            ''')
            pilihan_submenu = input('Masukkan angka submenu yang Anda pilih: ')

            if pilihan_submenu == '1':
                sortir_rata_rata()
            elif pilihan_submenu == '0':
                break
            else:
                print('Submenu tidak valid. Silakan pilih angka 1 atau 0.')

    elif pilihan_menu_utama == '3':
        while True:
            print('''
                Submenu Masukkan Nilai:
                1. Masukkan Nilai
                0. Kembali ke Menu Utama
            ''')
            pilihan_submenu_masukkan_nilai = input('Masukkan angka submenu yang Anda pilih: ')

            if pilihan_submenu_masukkan_nilai == '1':
                masukkan_nilai()
            elif pilihan_submenu_masukkan_nilai == '0':
                break
            else:
                print('Submenu tidak valid. Silakan pilih angka 1 atau 0.')

    elif pilihan_menu_utama == '4':
        while True:
            print('''
                Submenu Ubah Nilai:
                1. Ubah Nilai
                0. Kembali ke Menu Utama
            ''')
            pilihan_submenu_ubah_nilai = input('Masukkan angka submenu yang Anda pilih: ')

            if pilihan_submenu_ubah_nilai == '1':
                ubah_nilai()
            elif pilihan_submenu_ubah_nilai == '0':
                break
            else:
                print('Submenu tidak valid. Silakan pilih angka 1 atau 0.')

    elif pilihan_menu_utama == '5':
        while True:
            print('''
                Submenu Hapus Nilai:
                1. Hapus Nilai
                0. Kembali ke Menu Utama
            ''')
            pilihan_submenu_hapus_nilai = input('Masukkan angka submenu yang Anda pilih: ')

            if pilihan_submenu_hapus_nilai == '1':
                hapus_nilai()
            elif pilihan_submenu_hapus_nilai == '0':
                break
            else:
                print('Submenu tidak valid. Silakan pilih angka 1 atau 0.')

    elif pilihan_menu_utama == '6':
        break

    else:
        print('Menu utama tidak valid. Silakan pilih angka 1-6.')