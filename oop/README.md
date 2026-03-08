# Hasil Laporan Praktikum OOP
Kita akan membuat Sistem Pertarungan *Game* (*Battle System*) sederhana. Siswa diminta mengetik kode, menganalisis, dan memodifikasinya. 

## Membuat *Class Hero*
Tujuan: Memahami cara membuat *class* dan atribut *instance*. 

> Apa yang terjadi jika kamu mengubah *hero1.hp* menjadi 500 setelah baris *hero1 = Hero...*? Coba lakukan *print(hero1.hp)*<br>
> <ins>Nilai *hero1.hp* (*HP Layla*) menjadi 500.</ins>
> 
> <img width="406" height="133" alt="" src="https://github.com/user-attachments/assets/8b1f4092-dd26-4d89-a976-ebe5386f3f8e"/>

## Interaksi Antar Objek (*Method*)
Tujuan: Membuat objek saling berinteraksi (saling serang).

> Perhatikan parameter lawan pada *method* serang. Parameter tersebut menerima sebuah objek utuh, bukan hanya *string* nama. Mengapa ini penting?<br>
> <ins>Karena objek utuh dari parameter lawan diperlukan untuk menjalankan *method* "diserang".</ins>

## Pewarisan (*Inheritance*)
Tujuan: Membuat *role* khusus (*Mage* dan *Assassin*) yang mewarisi sifat *Hero* tapi punya keunikan.

> Eksperimen Fungsi *super()*: Pada *class Mage*, coba hapus (atau jadikan komentar #) baris kode *super().__init__(name, hp, attack_power)*. Kemudian jalankan programnya.
>
> <img width="905" height="204" alt="image" src="https://github.com/user-attachments/assets/efff986c-e03a-466c-9e32-cd8d3086da74" />
>
> Pertanyaan: *Error* apa yang muncul saat kamu mencoba melihat info *Eudora (eudora.info())*? Mengapa error tersebut mengatakan *Mage object has no attribute 'name'*, padahal kita sudah mengirim nama "Eudora" saat pembuatan objek?<br>
> <ins>Karena atribut nama tidak diinisiasikan dengan tidak adanya baris kode *class super().__init__*.</ins>
>
> Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke class Induk!<br>
> <ins>*super()* memanggil *method* yang terdapat dalam *class* Induk agar *class* Anak tidak perlu menulis ulang *method* tersebut.</ins>

## Enkapsulasi (Mengamankan Data *HP*)
Tujuan: Mencegah *HP* diubah sembarangan (misal jadi negatif atau di-*cheat* jadi 9999).

> Percobaan *Hacking*: Coba tambahkan baris kode berikut di bagian paling bawah (luar class): *print(f"Mencoba akses paksa: {hero1._Hero__hp}")*
>
> <img width="392" height="79" alt="image" src="https://github.com/user-attachments/assets/de9b56f2-92ad-49e3-928a-ef81501b0dd5" />
>
> Pertanyaan: Apakah nilai *HP* muncul atau *Error*? Jika muncul, diskusikan dengan temanmu mengapa *Python* masih mengizinkan akses ini (konsep *Name Mangling*) dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman yang baik.
> <ins>Fungsi dari *Name Mangling* adalah untuk mencegah adanya konflik nama antar *objek*, tetapi konsep ini tidak layak dilakukan dalam standar pemrograman karena membuat *private* atribut yang dipanggil menjadi tidak *private*.</ins>
>
> Uji Validasi: Hapus logika *if* dan *elif* di dalam *method set_hp*, sehingga isinya hanya *self.__hp = nilai_baru*. Kemudian lakukan *hero1.set_hp(-100)*.
>
> <img width="390" height="106" alt="image" src="https://github.com/user-attachments/assets/78949383-edd1-4847-b19b-29d3b1621c09" />
>
> Pertanyaan: Apa yang terjadi pada data *HP Hero*? Jelaskan mengapa keberadaan *method Setter* sangat penting untuk menjaga integritas data dalam *game*!<br>
> <ins>Data *HP Hero* menjadi -50, yang bukanlah nilai *valid* untuk *HP*. Maka dari itu, *method Setter* diperlukan untuk mencegah terjadinya hal seperti ini, dimana nilai yang tidak valid dimasukkan untuk atribut tersebut.</ins>

## *Abstraction* & *Interface* (Membuat Kontrak/Standar)
Tujuan: Memastikan semua karakter (baik *Hero* maupun *Monster*) wajib memiliki *method* serang dan info. Kita gunakan modul *abc*.

> Melanggar Kontrak: Pada *class Hero*, hapus (atau jadikan komentar #) seluruh blok *method def serang(self, target):*. Jalankan programnya.
>
> <img width="1136" height="151" alt="image" src="https://github.com/user-attachments/assets/d0c16065-2da5-4c58-bac6-f958d6464473" />
>
> Pertanyaan: *Error* apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti pesan *error Can't instantiate abstract class Hero with abstract method*...? Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di Interface?<br>
> <ins>*Can't instantiate abstract class Hero with abstract method* artinya *abstract class Hero* tidak dapat diinisiasikan tanpa menginisiasikan *abstract method* yang terdapat didalam *abstract class* tersebut, dimana pada kasus ini *abstract method* tersebut adalah *method serang*.</ins>
>
> Mencetak Cetakan: Coba aktifkan baris kode *unit = GameUnit()*.
>
> <img width="1279" height="161" alt="image" src="https://github.com/user-attachments/assets/6670dc74-85d8-4a8c-b3c4-f45c34fd6003" />
>
> Pertanyaan: Mengapa *class GameUnit* dilarang untuk dibuat menjadi objek? Apa gunanya ada *class GameUnit* jika tidak bisa dibuat menjadi objek nyata?<br>
> <ins>*Class GameUnit* digunakan sebagai *abstract class*, yang berfungsi untuk menjadi *blueprint* atau standar untuk *class* Anaknya. Ia memiliki rencana awal dari *method* yang akan digunakan, tetapi isi dari *method* tersebut harus diinisiasikan oleh *class* Anaknya.</ins>

## *Polymorphism* (Fleksibilitas Interaksi)
Tujuan: Menjalankan perintah yang sama (serang) ke berbagai jenis objek berbeda, dan hasilnya menyesuaikan masing-masing objek.

> Uji Skalabilitas (Kemudahan Menambah Fitur): Tanpa mengubah satu huruf pun pada kode *Looping* (*for pahlawan in pasukan:*), buatlah satu *class* baru bernama *Healer(Hero)*. Isi *method* serang milik *Healer* dengan: *print(f"{self.name} tidak menyerang, tapi menyembuhkan teman!")*. Masukkan objek *Healer* ke dalam list pasukan.
> 
> <img width="639" height="208" alt="image" src="https://github.com/user-attachments/assets/f4c4a19d-6f07-44d9-88c4-fd81d5aa70b3" />
>
> Pertanyaan: Apakah program berjalan lancar? Kesimpulannya, apa keuntungan *Polimorfisme* bagi seorang programmer ketika harus *mengupdate game* dengan karakter baru di masa depan?<br>
> <ins>Iya, *class Healer* tetap berjalan seperti *class Hero* yang lain. *Polymorphism* sangat membantu untuk menambahkan objek atau karakter baru karena sudah tersedianya cetakan awal dari objek atau karakter tersebut. Hal ini meningkatkan efisiensi dan kecepatan dalam menulis baris kode dalam *mengupdate* program ataupun *game*.</ins>
>
> Konsistensi Penamaan: Ubah nama *method* serang pada *class Archer* menjadi *tembak_panah*. Jalankan program.<br>
> <ins>*Class Archer* dan *methodnya* tidak terpanggil pada baris *looping*.</ins>
>
> <img width="651" height="163" alt="image" src="https://github.com/user-attachments/assets/672ea773-68e2-4c5f-8859-40ed35e15518" />
>
> Pertanyaan: Apa yang terjadi? Mengapa dalam konsep *Polimorfisme*, nama *method* antara *Parent Class* dan berbagai *Child Class* harus persis sama?<br>
> <ins> Karena *method* yang terdapat pada *class* Induk berfungsi sebagai cetakan awal untuk *class* Anak. Jika terdapat perbedaan nama *method* antar *class* Induk dan Anak, maka sama saja seperti *class* Anak menciptakan *method* baru yang berbeda dengan *method* yang telah ada dari *class* Induknya.
