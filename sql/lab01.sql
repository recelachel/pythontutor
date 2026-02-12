#Menampilkan mahasiswa yang masuk tahun 2023
SELECT * FROM students WHERE Enrollment_Year = 2023;

#Menampilkan mahasiswa dengan major CSE
SELECT * FROM students WHERE Major = "CSE";

#Menampilkan hanya NIM dan Nama mahasiswa dari angkatan 2025
SELECT NIM, Name from students WHERE Enrollment_Year= 2025;

#Menampilkan hanya mahasiswa dengan NIM paling awal
SELECT * FROM students WHERE NIM = (select MIN(NIM) FROM students);

#Menampilkan jurusan dan jumlah mahasiswanya
SELECT Major, COUNT(*) AS jumlah_mahasiswa from students GROUP BY Major;