import sqlite3

def create_connection():
    """Create a database connection to a SQLite database"""
    conn = sqlite3.connect('university.db')
    return conn

def create_tables(conn):
    """Create the required tables"""
    cursor = conn.cursor()
    
    # Create Mahasiswa table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Mahasiswa (
            NIM TEXT PRIMARY KEY,
            Nama TEXT NOT NULL,
            Alamat TEXT,
            Jurusan TEXT,
            Umur INTEGER
        )
    ''')
    
    # Create Mata_Kuliah table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Mata_Kuliah (
            ID INTEGER PRIMARY KEY,
            Mata_Kuliah TEXT NOT NULL,
            NIM TEXT,
            Nilai INTEGER,
            Dosen_Pengajar TEXT,
            FOREIGN KEY (NIM) REFERENCES Mahasiswa (NIM)
        )
    ''')
    
    conn.commit()

def insert_sample_data(conn):
    """Insert sample data into the tables"""
    cursor = conn.cursor()
    
    # Insert Mahasiswa data
    mahasiswa_data = [
        ('123456', 'John', 'Jl. Merdeka No. 1', 'Teknik Informatika', 21),
        ('234567', 'Alice', 'Jl. Gatot Subroto', 'Sistem Informasi', 23),
        ('345678', 'Bob', 'Jl. Sudirman No. 5', 'Teknik Informatika', 20),
        ('456789', 'Cindy', 'Jl. Pahlawan No. 2', 'Manajemen', 22),
        ('567890', 'David', 'Jl. Diponegoro No. 3', 'Teknik Elektro', 25),
        ('678901', 'Emily', 'Jl. Cendrawasih No. 4', 'Manajemen', 24),
        ('789012', 'Frank', 'Jl. Ahmad Yani No. 6', 'Teknik Informatika', 19)
    ]
    
    cursor.executemany('INSERT OR REPLACE INTO Mahasiswa VALUES (?,?,?,?,?)', mahasiswa_data)
    
    # Insert Mata_Kuliah data
    mata_kuliah_data = [
        (1, 'Pemrograman Web', '123456', 85, 'Pak Budi'),
        (2, 'Basis Data', '234567', 70, 'Ibu Ani'),
        (3, 'Jaringan Komputer', '345678', 75, 'Pak Dodi'),
        (4, 'Sistem Operasi', '123456', 90, 'Pak Budi'),
        (5, 'Manajemen Proyek', '456789', 80, 'Ibu Desi'),
        (6, 'Bahasa Inggris', '567890', 85, 'Ibu Eka'),
        (7, 'Statistika', '678901', 75, 'Pak Farhan'),
        (8, 'Algoritma', '789012', 65, 'Pak Galih'),
        (9, 'Pemrograman Java', '123456', 95, 'Pak Budi')
    ]
    
    cursor.executemany('INSERT OR REPLACE INTO Mata_Kuliah VALUES (?,?,?,?,?)', mata_kuliah_data)
    
    conn.commit()

def execute_queries(conn):
    """Execute the required queries"""
    cursor = conn.cursor()
    
    print("\n1. Update alamat mahasiswa dengan NIM '123456'")
    cursor.execute("""
        UPDATE Mahasiswa 
        SET Alamat = 'Jl. Raya No.5' 
        WHERE NIM = '123456'
    """)
    conn.commit()
    
    print("\n2. Data mahasiswa Teknik Informatika dan dosen pembimbing:")
    cursor.execute("""
        SELECT DISTINCT 
            m.NIM,
            m.Nama,
            m.Jurusan,
            mk.Dosen_Pengajar as Dosen_Pembimbing
        FROM Mahasiswa m
        JOIN Mata_Kuliah mk ON m.NIM = mk.NIM
        WHERE m.Jurusan = 'Teknik Informatika'
        GROUP BY m.NIM, m.Nama, m.Jurusan, mk.Dosen_Pengajar
    """)
    for row in cursor.fetchall():
        print(row)
    
    print("\n3. 5 mahasiswa tertua:")
    cursor.execute("""
        SELECT Nama, Umur
        FROM Mahasiswa
        ORDER BY Umur DESC
        LIMIT 5
    """)
    for row in cursor.fetchall():
        print(row)
    
    print("\n4. Data mahasiswa dengan nilai > 70:")
    cursor.execute("""
        SELECT 
            m.Nama,
            mk.Mata_Kuliah,
            mk.Nilai
        FROM Mahasiswa m
        JOIN Mata_Kuliah mk ON m.NIM = mk.NIM
        WHERE mk.Nilai > 70
        ORDER BY m.Nama, mk.Mata_Kuliah
    """)
    for row in cursor.fetchall():
        print(row)

def main():
    # Create connection
    conn = create_connection()
    
    try:
        # Create tables
        create_tables(conn)
        
        # Insert sample data
        insert_sample_data(conn)
        
        # Execute queries
        execute_queries(conn)
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()