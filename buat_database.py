import json
import random

# --- 1. GENERATOR SOAL MATEMATIKA (30 Soal Unik Dinamis) ---
def generate_mtk():
    soal_mtk = []
    
    # Tipe 1: Aljabar (10 soal)
    for i in range(10):
        a = random.randint(2, 9)
        x = random.randint(2, 10)
        c = random.randint(5, 20)
        hasil = (a * x) - c
        q = {
            "id": i+1,
            "q": f"Tentukan nilai x dari persamaan: {a}x - {c} = {hasil}",
            "options": [str(x), str(x+2), str(x-1), str(x+5)],
            "answer": str(x),
            "rationale": f"{a}x = {hasil} + {c} -> {a}x = {hasil+c} -> x = {x}"
        }
        random.shuffle(q["options"]) # ACAK OPSI LANGSUNG
        soal_mtk.append(q)

    # Tipe 2: Aritmatika Sosial (10 soal)
    for i in range(10):
        harga = random.randint(10, 50) * 10000
        diskon = random.choice([10, 20, 25, 50])
        potongan = int(harga * (diskon/100))
        bayar = harga - potongan
        q = {
            "id": i+11,
            "q": f"Harga Rp {harga:,} didiskon {diskon}%. Bayar berapa?",
            "options": [f"Rp {bayar:,}", f"Rp {bayar+5000:,}", f"Rp {potongan:,}", f"Rp {harga-5000:,}"],
            "answer": f"Rp {bayar:,}",
            "rationale": f"Diskon {diskon}% = {potongan:,}. Bayar = {harga:,} - {potongan:,} = {bayar:,}"
        }
        random.shuffle(q["options"]) # ACAK OPSI LANGSUNG
        soal_mtk.append(q)

    # Tipe 3: Deret Angka (10 soal)
    for i in range(10):
        start = random.randint(1, 10)
        diff = random.randint(2, 6)
        seq = [start + diff*j for j in range(4)]
        next_val = seq[-1] + diff
        seq_str = ", ".join(map(str, seq))
        q = {
            "id": i+21,
            "q": f"Lanjutkan pola: {seq_str}, ...",
            "options": [str(next_val), str(next_val+1), str(next_val-2), str(next_val*2)],
            "answer": str(next_val),
            "rationale": f"Polanya ditambah {diff}. Jadi {seq[-1]} + {diff} = {next_val}."
        }
        random.shuffle(q["options"]) # ACAK OPSI LANGSUNG
        soal_mtk.append(q)
        
    return soal_mtk

# --- 2. BANK SOAL STATIC (30 SOAL UNIK PER MAPEL) ---
master_data = {
    "IPA": [
        {"q": "Planet terbesar di tata surya adalah...", "a": "Jupiter", "opts": ["Jupiter", "Saturnus", "Mars", "Bumi"], "r": "Jupiter adalah planet gas raksasa terbesar."},
        {"q": "Hewan pemakan daging disebut...", "a": "Karnivora", "opts": ["Karnivora", "Herbivora", "Omnivora", "Insektivora"], "r": "Karnivora berasal dari kata carne (daging)."},
        {"q": "Rumus kimia air adalah...", "a": "H2O", "opts": ["H2O", "O2", "CO2", "H2SO4"], "r": "Air terdiri dari 2 Hidrogen dan 1 Oksigen."},
        {"q": "Bagian tumbuhan yang menyerap air dari tanah...", "a": "Akar", "opts": ["Akar", "Batang", "Daun", "Bunga"], "r": "Akar memiliki rambut akar untuk osmosis air."},
        {"q": "Perubahan padat ke cair disebut...", "a": "Mencair", "opts": ["Mencair", "Membeku", "Menguap", "Menyublim"], "r": "Contohnya es batu yang ditaruh di suhu ruang."},
        {"q": "Satuan kuat arus listrik adalah...", "a": "Ampere", "opts": ["Ampere", "Volt", "Watt", "Ohm"], "r": "Ampere adalah satuan SI untuk arus listrik."},
        {"q": "Reptil bernapas menggunakan...", "a": "Paru-paru", "opts": ["Paru-paru", "Insang", "Kulit", "Trakea"], "r": "Semua reptil (termasuk buaya/penyu) bernapas dengan paru-paru."},
        {"q": "Tulang rusuk melindungi organ vital yaitu...", "a": "Jantung dan Paru-paru", "opts": ["Jantung dan Paru-paru", "Otak", "Lambung", "Ginjal"], "r": "Rongga dada dilindungi tulang rusuk."},
        {"q": "Zat hijau daun disebut...", "a": "Klorofil", "opts": ["Klorofil", "Stomata", "Xilem", "Floem"], "r": "Klorofil berperan dalam fotosintesis."},
        {"q": "Simbiosis di mana satu untung dan satu rugi disebut...", "a": "Parasitisme", "opts": ["Parasitisme", "Mutualisme", "Komensalisme", "Amensalisme"], "r": "Contoh: Nyamuk menggigit manusia."},
        {"q": "Logam yang cair pada suhu ruangan adalah...", "a": "Raksa (Merkuri)", "opts": ["Raksa (Merkuri)", "Besi", "Emas", "Aluminium"], "r": "Raksa digunakan dalam termometer."},
        {"q": "Lapisan bumi paling luar disebut...", "a": "Kerak Bumi", "opts": ["Kerak Bumi", "Mantel", "Inti Luar", "Inti Dalam"], "r": "Tempat kita tinggal adalah kerak bumi."},
        {"q": "Proses tumbuhan memasak makanan dengan cahaya disebut...", "a": "Fotosintesis", "opts": ["Fotosintesis", "Respirasi", "Transpirasi", "Adaptasi"], "r": "Foto = cahaya, Sintesis = pembentukan."},
        {"q": "Hewan yang mengalami metamorfosis sempurna...", "a": "Kupu-kupu", "opts": ["Kupu-kupu", "Belalang", "Kecoa", "Ayam"], "r": "Telur -> Ulat -> Kepompong -> Kupu-kupu."},
        {"q": "Sumber energi terbesar di bumi adalah...", "a": "Matahari", "opts": ["Matahari", "Batu Bara", "Air", "Angin"], "r": "Matahari adalah pusat energi tata surya."},
        {"q": "Alat pengukur gempa bumi adalah...", "a": "Seismograf", "opts": ["Seismograf", "Barometer", "Termometer", "Anemometer"], "r": "Seismograf mencatat getaran tanah."},
        {"q": "Pencernaan kimiawi di mulut dibantu enzim...", "a": "Ptialin", "opts": ["Ptialin", "Pepsin", "Renin", "Lipase"], "r": "Ptialin mengubah amilum menjadi gula."},
        {"q": "Benda yang dapat ditarik magnet disebut...", "a": "Ferromagnetik", "opts": ["Ferromagnetik", "Paramagnetik", "Diamagnetik", "Nonmagnetik"], "r": "Contoh: Besi, Baja, Nikel."},
        {"q": "Planet Merah adalah julukan untuk...", "a": "Mars", "opts": ["Mars", "Venus", "Jupiter", "Saturnus"], "r": "Warna merah berasal dari oksida besi di permukaannya."},
        {"q": "Gerhana bulan terjadi saat posisi...", "a": "Matahari-Bumi-Bulan", "opts": ["Matahari-Bumi-Bulan", "Matahari-Bulan-Bumi", "Bumi-Matahari-Bulan", "Bulan-Matahari-Bumi"], "r": "Bumi menghalangi cahaya matahari ke bulan."},
        {"q": "Satuan frekuensi bunyi adalah...", "a": "Hertz", "opts": ["Hertz", "Decibel", "Watt", "Joule"], "r": "Hertz (Hz) adalah jumlah getaran per detik."},
        {"q": "Bagian sel yang mengatur seluruh kegiatan sel...", "a": "Inti Sel (Nukleus)", "opts": ["Inti Sel (Nukleus)", "Sitoplasma", "Mitokondria", "Ribosom"], "r": "Nukleus adalah otak dari sel."},
        {"q": "Bunyi pantul yang terdengar setelah bunyi asli...", "a": "Gema", "opts": ["Gema", "Gaung", "Desah", "Nada"], "r": "Gema terjadi di tebing atau gua."},
        {"q": "Penyakit kekurangan sel darah merah disebut...", "a": "Anemia", "opts": ["Anemia", "Leukimia", "Hipertensi", "Hemofilia"], "r": "Anemia menyebabkan tubuh lemas dan pucat."},
        {"q": "Gas yang kita hirup saat bernapas adalah...", "a": "Oksigen", "opts": ["Oksigen", "Karbondioksida", "Nitrogen", "Helium"], "r": "Oksigen dibutuhkan untuk metabolisme."},
        {"q": "Lensa pada kacamata rabun jauh (miopi) adalah...", "a": "Cekung", "opts": ["Cekung", "Cembung", "Silindris", "Datar"], "r": "Lensa cekung menyebarkan cahaya agar jatuh tepat di retina."},
        {"q": "Perkembangbiakan vegetatif buatan contohnya...", "a": "Mencangkok", "opts": ["Mencangkok", "Tunas", "Rhizoma", "Spora"], "r": "Mencangkok dilakukan manusia."},
        {"q": "Hewan mamalia yang bisa terbang adalah...", "a": "Kelelawar", "opts": ["Kelelawar", "Burung Elang", "Ayam", "Penguin"], "r": "Kelelawar adalah satu-satunya mamalia yang terbang."},
        {"q": "Jantung manusia memiliki berapa ruang?", "a": "4 Ruang", "opts": ["4 Ruang", "2 Ruang", "3 Ruang", "5 Ruang"], "r": "Serambi Kanan/Kiri dan Bilik Kanan/Kiri."},
        {"q": "Fungsi utama kulit adalah...", "a": "Pelindung tubuh & Indra peraba", "opts": ["Pelindung tubuh & Indra peraba", "Pencernaan", "Pernapasan utama", "Penyokong tubuh"], "r": "Kulit melindungi jaringan di bawahnya."}
    ],
    "IPS": [
        {"q": "Ibukota Indonesia yang baru bernama...", "a": "Nusantara", "opts": ["Nusantara", "Jakarta", "Balikpapan", "Penajam"], "r": "IKN Nusantara di Kalimantan Timur."},
        {"q": "Negara ASEAN yang tidak pernah dijajah...", "a": "Thailand", "opts": ["Thailand", "Malaysia", "Indonesia", "Filipina"], "r": "Thailand artinya Tanah Kebebasan."},
        {"q": "Patahan bumi penyebab gempa disebut...", "a": "Sesar", "opts": ["Sesar", "Lipatan", "Vulkanik", "Tektonik"], "r": "Pergeseran sesar memicu gempa."},
        {"q": "Organisasi PBB urusan kesehatan...", "a": "WHO", "opts": ["WHO", "UNICEF", "UNESCO", "ILO"], "r": "World Health Organization."},
        {"q": "Kerajaan Hindu tertua di Indonesia...", "a": "Kutai", "opts": ["Kutai", "Tarumanegara", "Majapahit", "Singasari"], "r": "Prasasti Yupa di Kaltim buktinya."},
        {"q": "Mata uang negara Jepang...", "a": "Yen", "opts": ["Yen", "Won", "Yuan", "Dollar"], "r": "Yen adalah mata uang resmi Jepang."},
        {"q": "Benua terluas di dunia...", "a": "Asia", "opts": ["Asia", "Afrika", "Amerika", "Eropa"], "r": "Asia menempati 30% daratan bumi."},
        {"q": "Tanggal Kemerdekaan RI...", "a": "17 Agustus 1945", "opts": ["17 Agustus 1945", "18 Agustus 1945", "28 Oktober 1928", "20 Mei 1908"], "r": "Proklamasi dibacakan Soekarno-Hatta."},
        {"q": "Candi Buddha terbesar di dunia...", "a": "Borobudur", "opts": ["Borobudur", "Prambanan", "Mendut", "Angkor Wat"], "r": "Terletak di Magelang, Jawa Tengah."},
        {"q": "Angin pembawa musim hujan di Indonesia...", "a": "Muson Barat", "opts": ["Muson Barat", "Muson Timur", "Angin Pasat", "Angin Laut"], "r": "Bertiup Oktober-April membawa uap air."},
        {"q": "Koperasi berlandaskan asas...", "a": "Kekeluargaan", "opts": ["Kekeluargaan", "Keuntungan", "Persaingan", "Individualis"], "r": "Sesuai UUD 1945 pasal 33."},
        {"q": "Penemu Benua Amerika...", "a": "Christopher Columbus", "opts": ["Christopher Columbus", "Vasco da Gama", "Magelhaens", "Cornelis de Houtman"], "r": "Tahun 1492 mendarat di Amerika."},
        {"q": "Provinsi termuda di Indonesia (2024) ada di pulau...", "a": "Papua", "opts": ["Papua", "Kalimantan", "Sumatera", "Jawa"], "r": "Pemekaran Papua Barat Daya, Papua Tengah, dll."},
        {"q": "Selat antara Jawa dan Sumatera...", "a": "Selat Sunda", "opts": ["Selat Sunda", "Selat Bali", "Selat Malaka", "Selat Makassar"], "r": "Menghubungkan Laut Jawa dan Samudra Hindia."},
        {"q": "Julukan Kota Pahlawan adalah...", "a": "Surabaya", "opts": ["Surabaya", "Semarang", "Bandung", "Medan"], "r": "Peristiwa 10 November 1945."},
        {"q": "Manusia purba yang ditemukan di Sangiran...", "a": "Meganthropus Paleojavanicus", "opts": ["Meganthropus Paleojavanicus", "Homo Sapiens", "Pithecanthropus Erectus", "Homo Soloensis"], "r": "Manusia raksasa tertua dari Jawa."},
        {"q": "Teks Sumpah Pemuda dibacakan tahun...", "a": "1928", "opts": ["1928", "1908", "1945", "1966"], "r": "28 Oktober 1928."},
        {"q": "Garis khayal pembagi waktu dunia (GMT)...", "a": "Greenwich", "opts": ["Greenwich", "Khatulistiwa", "Lintang", "Bujur"], "r": "Kota di London, Inggris."},
        {"q": "Negara Tirai Bambu adalah...", "a": "China", "opts": ["China", "Jepang", "Korea", "Vietnam"], "r": "Julukan untuk Tiongkok."},
        {"q": "Danau terbesar di Indonesia...", "a": "Danau Toba", "opts": ["Danau Toba", "Danau Singkarak", "Danau Poso", "Danau Towuti"], "r": "Danau vulkanik di Sumatera Utara."},
        {"q": "Rumah adat Sumatera Barat...", "a": "Gadang", "opts": ["Gadang", "Joglo", "Honai", "Tongkonan"], "r": "Atapnya runcing seperti tanduk kerbau."},
        {"q": "Menteri Pendidikan pertama RI...", "a": "Ki Hajar Dewantara", "opts": ["Ki Hajar Dewantara", "Soepomo", "Moh. Yamin", "Sutan Syahrir"], "r": "Bapak Pendidikan Nasional."},
        {"q": "Gunung tertinggi di Pulau Jawa...", "a": "Semeru", "opts": ["Semeru", "Kerinci", "Rinjani", "Slamet"], "r": "Puncaknya Mahameru (3676 mdpl)."},
        {"q": "ASEAN didirikan pada tanggal...", "a": "8 Agustus 1967", "opts": ["8 Agustus 1967", "17 Agustus 1945", "18 Agustus 1967", "8 Agustus 1957"], "r": "Deklarasi Bangkok."},
        {"q": "Perjanjian Renville dilakukan di atas...", "a": "Kapal Perang AS", "opts": ["Kapal Perang AS", "Gedung", "Hotel", "Istana"], "r": "USS Renville milik Amerika Serikat."},
        {"q": "Mata pencaharian utama penduduk Indonesia...", "a": "Petani", "opts": ["Petani", "Nelayan", "Pedagang", "Buruh"], "r": "Indonesia negara agraris."},
        {"q": "Samudra terluas di dunia...", "a": "Pasifik", "opts": ["Pasifik", "Atlantik", "Hindia", "Arktik"], "r": "Mencakup sepertiga permukaan bumi."},
        {"q": "Kitab Sutasoma dikarang oleh...", "a": "Mpu Tantular", "opts": ["Mpu Tantular", "Mpu Prapanca", "Mpu Gandring", "Mpu Sindok"], "r": "Asal mula semboyan Bhinneka Tunggal Ika."},
        {"q": "Organisasi Budi Utomo berdiri tahun...", "a": "1908", "opts": ["1908", "1928", "1945", "1905"], "r": "Hari Kebangkitan Nasional."},
        {"q": "Pusat pemerintahan Kerajaan Sriwijaya...", "a": "Palembang", "opts": ["Palembang", "Jambi", "Riau", "Medan"], "r": "Kerajaan Maritim terbesar."}
    ],
    "Bahasa Inggris": [
        {"q": "Past tense of 'Go'...", "a": "Went", "opts": ["Went", "Gone", "Goes", "Going"], "r": "Go (V1) -> Went (V2)."},
        {"q": "Antonym of 'Big'...", "a": "Small", "opts": ["Small", "Huge", "Large", "Giant"], "r": "Big = Besar, Small = Kecil."},
        {"q": "She ... reading a book now.", "a": "is", "opts": ["is", "am", "are", "were"], "r": "She (tunggal) + is + V-ing."},
        {"q": "Plural of 'Child'...", "a": "Children", "opts": ["Children", "Childs", "Childes", "Kid"], "r": "Irregular plural noun."},
        {"q": "Translate: 'Saya lapar'", "a": "I am hungry", "opts": ["I am hungry", "I am thirsty", "I am angry", "I am full"], "r": "Hungry = Lapar."},
        {"q": "Day after Monday...", "a": "Tuesday", "opts": ["Tuesday", "Wednesday", "Sunday", "Thursday"], "r": "Senin -> Selasa."},
        {"q": "An elephant is ... than a mouse.", "a": "Bigger", "opts": ["Bigger", "Big", "Biggest", "More big"], "r": "Comparative: Big + er."},
        {"q": "Verb 3 of 'Eat'...", "a": "Eaten", "opts": ["Eaten", "Ate", "Eat", "Eating"], "r": "Eat - Ate - Eaten."},
        {"q": "Synonym of 'Smart'...", "a": "Clever", "opts": ["Clever", "Stupid", "Lazy", "Slow"], "r": "Smart/Clever = Pintar."},
        {"q": "I ... breakfast every morning.", "a": "eat", "opts": ["eat", "eating", "eats", "ate"], "r": "Habitual action (Present Tense)."},
        {"q": "Sun rises in the...", "a": "East", "opts": ["East", "West", "North", "South"], "r": "Matahari terbit di Timur."},
        {"q": "My father's wife is my...", "a": "Mother", "opts": ["Mother", "Sister", "Aunt", "Grandma"], "r": "Istri ayahku adalah ibuku."},
        {"q": "We use an umbrella when it is...", "a": "Raining", "opts": ["Raining", "Sunny", "Windy", "Snowing"], "r": "Payung untuk hujan."},
        {"q": "He ... football yesterday.", "a": "played", "opts": ["played", "play", "plays", "playing"], "r": "Yesterday = Past Tense (V2)."},
        {"q": "What time is 07.30?", "a": "Half past seven", "opts": ["Half past seven", "Half to seven", "Seven thirty", "Seven o'clock"], "r": "Lewat 30 menit = Half past."},
        {"q": "Color of the sky...", "a": "Blue", "opts": ["Blue", "Green", "Red", "Yellow"], "r": "Langit berwarna biru."},
        {"q": "They ... happy.", "a": "are", "opts": ["are", "is", "am", "was"], "r": "They + are."},
        {"q": "Opposite of 'Hot'...", "a": "Cold", "opts": ["Cold", "Warm", "Cool", "Dry"], "r": "Panas >< Dingin."},
        {"q": "How many legs does a spider have?", "a": "Eight", "opts": ["Eight", "Six", "Four", "Ten"], "r": "Laba-laba berkaki 8."},
        {"q": "She writes with a...", "a": "Pen", "opts": ["Pen", "Pan", "Pin", "Fan"], "r": "Alat tulis = Pen."},
        {"q": "Meaning of 'Library'...", "a": "Perpustakaan", "opts": ["Perpustakaan", "Toko Buku", "Laboratorium", "Kantor"], "r": "Tempat meminjam buku."},
        {"q": "Translate: 'Good Night'", "a": "Selamat Tidur", "opts": ["Selamat Tidur", "Selamat Malam (Sapaan)", "Selamat Sore", "Selamat Pagi"], "r": "Good night diucapkan saat berpisah tidur."},
        {"q": "A chef works in a...", "a": "Kitchen", "opts": ["Kitchen", "Garden", "Garage", "Hospital"], "r": "Koki bekerja di dapur."},
        {"q": "To be for 'I'...", "a": "Am", "opts": ["Am", "Is", "Are", "Were"], "r": "I am."},
        {"q": "Seventh month of the year...", "a": "July", "opts": ["July", "June", "August", "May"], "r": "Bulan ke-7 adalah Juli."},
        {"q": "A place to see animals...", "a": "Zoo", "opts": ["Zoo", "Park", "School", "Mall"], "r": "Kebun binatang."},
        {"q": "Translate: 'Jangan malas'", "a": "Don't be lazy", "opts": ["Don't be lazy", "Don't be crazy", "Don't be shy", "Don't be angry"], "r": "Lazy = Malas."},
        {"q": "Subject pronoun for 'Budi and I'...", "a": "We", "opts": ["We", "They", "You", "He"], "r": "Orang lain + Saya = Kita (We)."},
        {"q": "Simple Present of 'Study' (He)...", "a": "Studies", "opts": ["Studies", "Study", "Studying", "Studied"], "r": "He/She/It + V1(s/es)."},
        {"q": "Meaning of 'Delicious'...", "a": "Lezat", "opts": ["Lezat", "Pahit", "Asam", "Pedas"], "r": "Enak/Lezat."}
    ],
    "Bahasa Indonesia": [
        {"q": "Gagasan utama paragraf...", "a": "Ide Pokok", "opts": ["Ide Pokok", "Kalimat Penjelas", "Kesimpulan", "Tema"], "r": "Inti dari paragraf."},
        {"q": "Persamaan bunyi akhir pantun...", "a": "Rima", "opts": ["Rima", "Irama", "Bait", "Larik"], "r": "Contoh: a-b-a-b."},
        {"q": "Majas melebih-lebihkan...", "a": "Hiperbola", "opts": ["Hiperbola", "Personifikasi", "Metafora", "Litotes"], "r": "Contoh: Suaranya membelah angkasa."},
        {"q": "Lawan kata 'Absen'...", "a": "Hadir", "opts": ["Hadir", "Bolos", "Izin", "Sakit"], "r": "Absen = Tidak hadir."},
        {"q": "Imbuhan me- pada 'Tulis'...", "a": "Menulis", "opts": ["Menulis", "Mentulis", "Metulis", "Menyulis"], "r": "Huruf T luluh."},
        {"q": "Cerita rakyat asal usul tempat...", "a": "Legenda", "opts": ["Legenda", "Mite", "Fabel", "Sage"], "r": "Contoh: Tangkuban Perahu."},
        {"q": "Tokoh baik dalam drama...", "a": "Protagonis", "opts": ["Protagonis", "Antagonis", "Tritagonis", "Figuran"], "r": "Proto = Pertama/Utama."},
        {"q": "Kata baku...", "a": "Apotek", "opts": ["Apotek", "Apotik", "Aphotek", "Aphotik"], "r": "Sesuai KBBI."},
        {"q": "Sinonim 'Surai'...", "a": "Rambut", "opts": ["Rambut", "Bubar", "Mata", "Tangan"], "r": "Surai biasa dipakai untuk rambut singa/kuda."},
        {"q": "Tempat kejadian cerita...", "a": "Latar", "opts": ["Latar", "Alur", "Tema", "Amanat"], "r": "Latar tempat, waktu, suasana."},
        {"q": "Percakapan dalam drama...", "a": "Dialog", "opts": ["Dialog", "Monolog", "Prolog", "Epilog"], "r": "Percakapan antar tokoh."},
        {"q": "Pesan moral cerita...", "a": "Amanat", "opts": ["Amanat", "Tema", "Alur", "Sudut Pandang"], "r": "Pesan yang ingin disampaikan penulis."},
        {"q": "Kalimat perintah diakhiri tanda...", "a": "Seru (!)", "opts": ["Seru (!)", "Tanya (?)", "Titik (.)", "Koma (,)"], "r": "Contoh: Pergi sana!"},
        {"q": "Buah tangan artinya...", "a": "Oleh-oleh", "opts": ["Oleh-oleh", "Karya", "Anak", "Makanan"], "r": "Ungkapan/Idiom."},
        {"q": "Dongeng hewan disebut...", "a": "Fabel", "opts": ["Fabel", "Legenda", "Mite", "Hikayat"], "r": "Tokohnya binatang."},
        {"q": "Kata depan 'di' yang benar...", "a": "Di pasar", "opts": ["Di pasar", "Dipasar", "Dimakan", "Dibuang"], "r": "Kata depan (tempat) dipisah."},
        {"q": "Paragraf yang kalimat utamanya di awal...", "a": "Deduktif", "opts": ["Deduktif", "Induktif", "Campuran", "Ineratif"], "r": "Deduktif (Depan)."},
        {"q": "Sinonim 'Laris'...", "a": "Laku", "opts": ["Laku", "Sepi", "Mahal", "Murah"], "r": "Banyak pembeli."},
        {"q": "Imbuhan pe- pada 'Sapu'...", "a": "Penyapu", "opts": ["Penyapu", "Pesapu", "Pensapu", "Pemsapu"], "r": "S luluh menjadi Ny."},
        {"q": "Biografi ditulis oleh...", "a": "Orang lain", "opts": ["Orang lain", "Diri sendiri", "Teman", "Keluarga"], "r": "Kalau diri sendiri namanya Autobiografi."},
        {"q": "Kata ganti orang pertama tunggal...", "a": "Saya", "opts": ["Saya", "Kami", "Kamu", "Dia"], "r": "Aku/Saya."},
        {"q": "Kalimat tanya menanyakan waktu...", "a": "Kapan", "opts": ["Kapan", "Dimana", "Siapa", "Mengapa"], "r": "Kapan kejadiannya?"},
        {"q": "Majas benda mati dianggap hidup...", "a": "Personifikasi", "opts": ["Personifikasi", "Metafora", "Hiperbola", "Ironi"], "r": "Contoh: Angin berbisik."},
        {"q": "Penulisan gelar sarjana...", "a": "S.Pd.", "opts": ["S.Pd.", "S.pd", "s.Pd", "SPD"], "r": "Diakhiri titik."},
        {"q": "Ringkasan cerita disebut...", "a": "Sinopsis", "opts": ["Sinopsis", "Resensi", "Kritik", "Esai"], "r": "Ringkasan pendek isi buku/film."},
        {"q": "Antonim 'Gagal'...", "a": "Berhasil", "opts": ["Berhasil", "Kalah", "Rugi", "Jatuh"], "r": "Sukses/Berhasil."},
        {"q": "Bunyi vokal akhir baris puisi...", "a": "Rima", "opts": ["Rima", "Bait", "Larik", "Diksi"], "r": "Persajakan."},
        {"q": "Kata hubung perlawanan...", "a": "Tetapi", "opts": ["Tetapi", "Dan", "Atau", "Serta"], "r": "Menghubungkan hal bertentangan."},
        {"q": "Makna 'Kambing Hitam'...", "a": "Orang yang disalahkan", "opts": ["Orang yang disalahkan", "Kambing warna hitam", "Penjahat", "Pencuri"], "r": "Dituduh bersalah."},
        {"q": "Huruf kapital digunakan untuk...", "a": "Nama Orang", "opts": ["Nama Orang", "Nama Buah", "Nama Hewan", "Kata Sambung"], "r": "Budi, Ani, dll."}
    ]
}

# --- 3. PROSES DATA & PENGACAKAN AWAL ---
final_data = {}

# Masukkan MTK
final_data["Matematika"] = generate_mtk()

# Masukkan Mapel Lain
for mapel, questions in master_data.items():
    processed_qs = []
    for i, q in enumerate(questions):
        # Format ulang agar sesuai aplikasi
        new_q = {
            "id": i + 1,
            "q": q["q"],
            "options": q["opts"], # Ambil opsi
            "answer": q["a"],     # Kunci jawaban
            "rationale": q["r"]
        }
        # PENTING: Acak opsi di sini agar di JSON sudah teracak
        random.shuffle(new_q["options"]) 
        processed_qs.append(new_q)
    final_data[mapel] = processed_qs

# --- 4. SIMPAN FILE ---
try:
    with open('quiz_data.json', 'w') as f:
        json.dump(final_data, f, indent=4)
    print("✅ SUKSES! Database 'quiz_data.json' diperbarui.")
    print("👉 Total 150 Soal Unik (30 per Mapel).")
    print("👉 Pilihan Ganda SUDAH DIACAK (Jawaban tidak selalu A).")
    print("👉 Silakan restart aplikasi 'app.py' Anda.")
except Exception as e:
    print(f"❌ Error: {e}")