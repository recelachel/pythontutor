print("MENAMPILKAN DATA NILAI")

try:
    with open("nilai_siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0], ":", data[1])
except FileNotFoundError:
    print("File nilai_siswa.txt tidak ditemukan")
    
print("SELESAI")