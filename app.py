from flask import Flask, render_template, request, session, redirect, url_for, json
import os
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'rahasia_negara_api_cerah'

# --- FUNGSI BACA DATABASE SOAL ---
def load_questions():
    filename = os.path.join(app.root_path, 'quiz_data.json')
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# --- FUNGSI BARU: SIMPAN REKAP NILAI SISWA ---
def simpan_rekap(data_siswa):
    filename = os.path.join(app.root_path, 'rekap_nilai.json')
    data_lama = []
    
    # Coba baca data lama kalau ada
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                data_lama = json.load(f)
        except:
            data_lama = []

    # Tambah data baru
    data_lama.append(data_siswa)
    
    # Simpan kembali
    with open(filename, 'w') as f:
        json.dump(data_lama, f, indent=4)

# --- ROUTE HALAMAN ---

@app.route('/', methods=['GET', 'POST'])
def index():
    # Halaman Login
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('menu'))
    return render_template('login.html')

@app.route('/menu')
def menu():
    # Halaman Pilih Mapel
    if 'username' not in session:
        return redirect(url_for('index'))
    
    data = load_questions()
    subjects = list(data.keys())
    return render_template('menu.html', nama=session['username'], mapel=subjects)

# --- ROUTE BARU: HALAMAN KHUSUS GURU ---
@app.route('/rekap-nilai-mr-heru')
def rekap_guru():
    # Baca file rekap
    filename = os.path.join(app.root_path, 'rekap_nilai.json')
    data_rekap = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                data_rekap = json.load(f)
        except:
            data_rekap = []
            
    # Balik urutan biar yang terbaru di atas
    data_rekap.reverse()
    return render_template('rekap.html', data=data_rekap)

@app.route('/start_quiz/<mapel>')
def start_quiz(mapel):
    # Persiapan Mulai Kuis
    data = load_questions()
    if mapel in data:
        all_questions = data[mapel]
        # Ambil 30 soal
        jumlah_soal = min(len(all_questions), 30)
        selected_questions = random.sample(all_questions, jumlah_soal)
        
        # Simpan data kuis ke Session
        session['quiz_data'] = selected_questions
        session['current_mapel'] = mapel
        session['score'] = 0
        session['total'] = len(selected_questions)
        session['current_index'] = 0
        session['log_jawaban'] = []
        
        return redirect(url_for('question'))
    return redirect(url_for('menu'))

@app.route('/question')
def question():
    # Tampilkan Soal
    if 'quiz_data' not in session:
        return redirect(url_for('menu'))

    idx = session['current_index']
    questions = session['quiz_data']
    
    if idx < len(questions):
        current_q = questions[idx]
        return render_template('quiz.html', 
                             q=current_q, 
                             index=idx+1, 
                             total=session['total'],
                             mapel=session['current_mapel'])
    else:
        return redirect(url_for('result'))

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    # Cek Jawaban (AJAX)
    user_answer = request.form.get('answer')
    idx = session['current_index']
    questions = session['quiz_data']
    
    correct_answer = questions[idx]['answer']
    rationale = questions[idx]['rationale']
    
    is_correct = (user_answer == correct_answer)
    
    if is_correct:
        session['score'] += 1
        
    session['log_jawaban'].append({
        'no': idx + 1,
        'q': questions[idx]['q'],
        'user_ans': user_answer,
        'correct_ans': correct_answer,
        'is_correct': is_correct
    })
    
    session['current_index'] += 1
    session.modified = True
    
    return json.dumps({
        'is_correct': is_correct,
        'correct_answer': correct_answer,
        'rationale': rationale,
        'finished': session['current_index'] >= len(questions)
    })

@app.route('/result')
def result():
    # Halaman Rapor Akhir & PENYIMPANAN DATA
    if 'score' not in session:
        return redirect(url_for('menu'))

    score = session['score']
    total = session['total']
    percent = int((score / total) * 100) if total > 0 else 0
    nama = session['username']
    mapel = session['current_mapel']
    
    # Logic Pangkat
    badge = ""
    pesan = ""
    if percent == 100:
        badge = "👑 THE GOAT"
        pesan = "Sempurna! Masa depan cerah di tanganmu!"
    elif percent >= 85:
        badge = "🌟 STAR PIONEER"
        pesan = "Luar biasa! Kamu siap memimpin masa depan."
    elif percent >= 70:
        badge = "🚀 FUTURE LEADER"
        pesan = "Hebat! Terus tingkatkan potensimu."
    elif percent >= 50:
        badge = "✨ RISING STAR"
        pesan = "Bagus, teruslah bersinar dan belajar."
    else:
        badge = "🌱 FUTURE SEED"
        pesan = "Jangan menyerah, pupuk terus ilmumu!"

    # --- BAGIAN BARU: SIMPAN DATA UNTUK GURU ---
    # Kita hanya simpan jika ini pertama kali buka halaman result untuk sesi ini
    if not session.get('data_saved'):
        waktu_skrg = datetime.now().strftime("%d/%m/%Y %H:%M")
        data_untuk_guru = {
            "waktu": waktu_skrg,
            "nama": nama,
            "mapel": mapel,
            "skor": f"{score} / {total}",
            "persen": f"{percent}%",
            "badge": badge
        }
        simpan_rekap(data_untuk_guru)
        session['data_saved'] = True # Tandai sudah disimpan

    return render_template('result.html', 
                           score=score, 
                           total=total, 
                           percent=percent, 
                           badge=badge, 
                           pesan=pesan,
                           log=session['log_jawaban'],
                           nama=nama)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)