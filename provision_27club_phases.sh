#!/bin/bash
# ==============================================================================
# SCRIPT MAESTRO DE APROVISIONAMIENTO: THE 27 CLUB CTF
# Universidad de Cundinamarca - Seguridad de Aplicaciones y Hacking Ético
# ==============================================================================

set -e

# Decodificación dinámica de artefactos protegidos del laboratorio (anti-spoiler)
F_JOPLIN=$(echo "RkxBR3tDcnlfQmFieV9IaWRkZW5fRGF0YX0=" | base64 -d)
R_JOPLIN=$(echo "UkFCQklUX0hPTEV7U2lndWVfQnVzY2FuZG9fSmFuaXNfU2VfUmllX0RlX1RpfQ==" | base64 -d)
F_MORRISON=$(echo "RkxBR3tMaWdodF9NeV9GaXJlX1NRTGl9" | base64 -d)
R_MORRISON=$(echo "UkFCQklUX0hPTEV7VGhlX0VuZF9Jc19Ob3RfSGVyZX0=" | base64 -d)
F_AMY=$(echo "RkxBR3tCYWNrX1RvX0JsYWNrX1hTU30=" | base64 -d)
R_AMY=$(echo "UkFCQklUX0hPTEV7UmVoYWJfV2FzX0FfTGllfQ==" | base64 -d)
F_KURT=$(echo "RkxBR3tTbWVsbHNfTGlrZV9Sb290X1NwaXJpdH0=" | base64 -d)

echo "[*] ========================================================"
echo "[*] INICIANDO DESPLIEGUE INSTITUCIONAL 'THE 27 CLUB CTF'"
echo "[*] ========================================================"

# Habilitar cabeceras HTTP temáticas en Apache
a2enmod headers 2>/dev/null || true
cat << 'EOF' > /etc/apache2/conf-available/rock-headers.conf
<IfModule mod_headers.c>
    Header set X-Rock-Memorial "The 27 Club CTF - Live Fast, Die Young, Leave a Clean Codebase"
    Header set X-Artist-Tribute "Jimi Hendrix, Janis Joplin, Jim Morrison, Amy Winehouse, Kurt Cobain"
    Header set X-Security-Auditor "Oscar Robayo - Universidad de Cundinamarca"
    Header set X-Powered-By "Marshall Amps & Fender Stratocaster"
</IfModule>
EOF
a2enconf rock-headers 2>/dev/null || true

# Configurar error 404 personalizado si existe
if [ -f /var/www/html/rock_404.html ]; then
    echo "ErrorDocument 404 /rock_404.html" > /var/www/html/.htaccess
fi

# ------------------------------------------------------------------------------
# FASE 2: JANIS JOPLIN (INYECCIÓN DINÁMICA DE ESTEGANOGRAFÍA EOF)
# ------------------------------------------------------------------------------
if [ -f /var/www/html/cry_baby/janis.jpg ]; then
    echo -n "${F_JOPLIN}" >> /var/www/html/cry_baby/janis.jpg
fi
if [ -f /var/www/html/admin_trampa/backup_keys.jpg ]; then
    echo -n "${R_JOPLIN}" >> /var/www/html/admin_trampa/backup_keys.jpg
fi

# ------------------------------------------------------------------------------
# FASE 3: JIM MORRISON (CWE-89 SQL INJECTION)
# ------------------------------------------------------------------------------
echo "[*] Configurando Fase 3 (Jim Morrison - CWE-89)..."
mkdir -p /var/www/html/doors

# Poblar MySQL con tabla real y tabla señuelo (Rabbit Hole)
mysql -u root -p'password' -e "
CREATE DATABASE IF NOT EXISTS 27club;
USE 27club;

-- Tabla señuelo (Rabbit Hole pedagógico)
DROP TABLE IF EXISTS doors_trap;
CREATE TABLE doors_trap (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cancion VARCHAR(100),
    secreto VARCHAR(255)
);
INSERT INTO doors_trap (cancion, secreto) VALUES
('The End', '${R_MORRISON}'),
('Strange Days', 'Distraccion: Morrison sigue cantando en otra tabla.');

-- Tabla real con la bandera oficial
DROP TABLE IF EXISTS doors_vault;
CREATE TABLE doors_vault (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cancion VARCHAR(100),
    album VARCHAR(100),
    secreto VARCHAR(255)
);
INSERT INTO doors_vault (cancion, album, secreto) VALUES
('Break On Through', 'The Doors (1967)', 'Pista: El fuego se enciende en el siguiente registro.'),
('Light My Fire', 'The Doors (1967)', '${F_MORRISON}'),
('Riders on the Storm', 'L.A. Woman (1971)', 'Archivo historico de sesion.'),
('Touch Me', 'The Soft Parade (1969)', 'Registro completado.');

GRANT ALL PRIVILEGES ON 27club.* TO 'app'@'localhost' IDENTIFIED BY 'vulnerables';
GRANT ALL PRIVILEGES ON 27club.* TO 'dvwa'@'localhost';
FLUSH PRIVILEGES;
" 2>/dev/null || {
    echo "[!] Advertencia: Creando tablas en base de datos dvwa por compatibilidad..."
    mysql -u dvwa -ppassword -D dvwa -e "
    CREATE TABLE IF NOT EXISTS doors_trap (id INT AUTO_INCREMENT PRIMARY KEY, cancion VARCHAR(100), secreto VARCHAR(255));
    INSERT INTO doors_trap (cancion, secreto) VALUES ('The End', '${R_MORRISON}');

    CREATE TABLE IF NOT EXISTS doors_vault (id INT AUTO_INCREMENT PRIMARY KEY, cancion VARCHAR(100), album VARCHAR(100), secreto VARCHAR(255));
    INSERT INTO doors_vault (cancion, album, secreto) VALUES 
    ('Light My Fire', 'The Doors', '${F_MORRISON}');
    "
}

# Crear portal vulnerable de Jim Morrison en PHP
cat << 'EOF' > /var/www/html/doors/index.php
<?php
$conn = @new mysqli('127.0.0.1', 'app', 'vulnerables', '27club');
if ($conn->connect_error) {
    $conn = @new mysqli('127.0.0.1', 'root', 'password', '27club');
    if ($conn->connect_error) {
        $conn = new mysqli('127.0.0.1', 'dvwa', 'password', 'dvwa');
    }
}
$id = isset($_GET['id']) ? $_GET['id'] : '1';
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>The Doors Archives - Jim Morrison</title>
    <style>
        body { background: #0c0a14; color: #e6dfd3; font-family: 'Courier New', monospace; padding: 30px; }
        .card { max-width: 720px; margin: 0 auto; background: #151221; border: 2px solid #ffaa00; border-radius: 8px; padding: 25px; box-shadow: 0 0 25px rgba(255, 170, 0, 0.2); }
        h1 { color: #ffaa00; text-align: center; }
        .quote { font-style: italic; color: #9c95ab; text-align: center; margin-bottom: 20px; }
        input[type="text"] { width: 75%; padding: 10px; background: #07060d; border: 1px solid #ffaa00; color: #00ffcc; font-family: monospace; font-size: 1rem; }
        button { padding: 10px 18px; background: #ffaa00; border: none; font-weight: bold; cursor: pointer; color: #000; }
        .box-result { margin-top: 25px; background: #07060d; padding: 15px; border-left: 4px solid #ffaa00; }
        .hint { margin-top: 15px; font-size: 0.8rem; color: #6e6b7b; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🎸 The Doors • Jim Morrison Vault</h1>
        <p class="quote">"There are things known and things unknown, and in between are the doors."</p>
        
        <form method="GET" action="">
            <label><strong>Consultar Catálogo por ID:</strong></label><br><br>
            <input type="text" name="id" value="<?php echo htmlspecialchars($id); ?>">
            <button type="submit">Ejecutar</button>
        </form>

        <div class="box-result">
            <h4>Registros en memoria:</h4>
            <?php
            $query = "SELECT cancion, album, secreto FROM doors_vault WHERE id = " . $id;
            $res = $conn->query($query);

            if ($res && $res->num_rows > 0) {
                while($row = $res->fetch_assoc()) {
                    echo "<p><strong>Canción:</strong> " . htmlspecialchars($row["cancion"]) . "<br>";
                    echo "<strong>Álbum:</strong> " . htmlspecialchars($row["album"]) . "<br>";
                    echo "<strong>Secreto / Archivo:</strong> <code>" . htmlspecialchars($row["secreto"]) . "</code></p><hr>";
                }
            } else {
                echo "<p style='color: #ff3366;'>No se encontraron registros o error de sintaxis en la consulta.</p>";
                if ($conn->error) {
                    echo "<p style='color: #ffaa00;'><small>Debug MySQL: " . htmlspecialchars($conn->error) . "</small></p>";
                }
            }
            ?>
        </div>
        <p class="hint">Fase 3: Auditoría CWE-89 (SQL Injection) • Universidad de Cundinamarca</p>
    </div>
</body>
</html>
EOF

# ------------------------------------------------------------------------------
# FASE 4: AMY WINEHOUSE (CWE-79 STORED XSS & COOKIE EXTRACTION)
# ------------------------------------------------------------------------------
echo "[*] Configurando Fase 4 (Amy Winehouse - CWE-79)..."
mkdir -p /var/www/html/winehouse

mysql -u root -p'password' -e "
USE 27club;
CREATE TABLE IF NOT EXISTS amy_guestbook (
    id INT AUTO_INCREMENT PRIMARY KEY,
    autor VARCHAR(100),
    mensaje TEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
" 2>/dev/null || true

cat << EOF > /var/www/html/winehouse/index.php
<?php
setcookie("admintoken", "${F_AMY}", time() + 3600, "/");
setcookie("test_decoy", "${R_AMY}", time() + 3600, "/");

\$conn = @new mysqli('127.0.0.1', 'app', 'vulnerables', '27club');
if (\$conn->connect_error) {
    \$conn = new mysqli('127.0.0.1', 'root', 'password', '27club');
}

if (\$_SERVER['REQUEST_METHOD'] === 'POST' && !empty(\$_POST['mensaje'])) {
    \$autor = !empty(\$_POST['autor']) ? \$_POST['autor'] : 'Anónimo';
    \$mensaje = \$_POST['mensaje'];
    \$stmt = \$conn->prepare("INSERT INTO amy_guestbook (autor, mensaje) VALUES (?, ?)");
    if (\$stmt) {
        \$stmt->bind_param("ss", \$autor, \$mensaje);
        \$stmt->execute();
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Amy Winehouse - Back To Black Lounge</title>
    <style>
        body { background: #0e0712; color: #e9d5ff; font-family: 'Georgia', serif; padding: 30px; }
        .card { max-width: 750px; margin: 0 auto; background: #1c1024; border: 2px solid #ff007f; border-radius: 8px; padding: 25px; box-shadow: 0 0 25px rgba(255, 0, 127, 0.2); }
        h1 { color: #ff007f; text-align: center; font-family: sans-serif; }
        .quote { font-style: italic; color: #a894b8; text-align: center; }
        input[type="text"], textarea { width: 95%; padding: 10px; background: #0a040d; border: 1px solid #ff007f; color: #00f0ff; font-family: sans-serif; margin-bottom: 12px; }
        button { padding: 10px 22px; background: #ff007f; border: none; font-weight: bold; color: #fff; cursor: pointer; border-radius: 4px; }
        .entry { background: #0a040d; padding: 12px; border-left: 4px solid #ff007f; margin-bottom: 12px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🎤 Amy Winehouse • Back to Black Lounge</h1>
        <p class="quote">"Love is a losing game, but XSS steals the crown."</p>

        <form method="POST" action="">
            <label>Nombre del remitente:</label><br>
            <input type="text" name="autor" placeholder="Ej: Fan de Camden"><br>
            <label>Mensaje dedicatoria (Soporta formato):</label><br>
            <textarea name="mensaje" rows="3" placeholder="Deja tus últimas palabras..."></textarea><br>
            <button type="submit">Publicar en el Muro</button>
        </form>

        <hr style="border: 0.5px solid #3b1d4c; margin: 25px 0;">
        <h3>Dedicatorias Almacenadas:</h3>
        <div id="posts">
            <?php
            \$res = \$conn->query("SELECT autor, mensaje, fecha FROM amy_guestbook ORDER BY id DESC LIMIT 10");
            if (\$res) {
                while(\$row = \$res->fetch_assoc()) {
                    echo "<div class='entry'>";
                    echo "<strong>" . htmlspecialchars(\$row['autor']) . "</strong> <em>(" . \$row['fecha'] . ")</em><br>";
                    echo "<div class='content'>" . \$row['mensaje'] . "</div>";
                    echo "</div>";
                }
            }
            ?>
        </div>
        <p style="font-size:0.8rem; color:#786588; text-align:center; margin-top:20px;">
            Fase 4: Auditoría CWE-79 (Stored Cross-Site Scripting) • Universidad de Cundinamarca
        </p>
    </div>
</body>
</html>
EOF

# ------------------------------------------------------------------------------
# FASE 5: KURT COBAIN (CWE-250 / CWE-307 AUDITORÍA Y ESCALADA ROOT)
# ------------------------------------------------------------------------------
echo "[*] Configurando Fase 5 (Kurt Cobain - CWE-250 / SUID)..."

id -u kurt &>/dev/null || useradd -m -s /bin/bash kurt
echo "kurt:nirvana" | chpasswd

mkdir -p /home/kurt
cat << 'EOF' > /home/kurt/nota_cobain.txt
"Come as you are, as you were, as I want you to be..."
Para romper la última cadena del Club de los 27 y reclamar el trono de root:
Audita los permisos especiales (SUID). Hay una herramienta que corre con el poder de UID 0.
EOF
chown -R kurt:kurt /home/kurt

cat << EOF > /root/flag.txt
========================================================================
   ⚡ THE 27 CLUB CTF - UNIVERSIDAD DE CUNDINAMARCA ⚡
   COMPROMISO TOTAL DEL SISTEMA (ROOT UID 0 ALCANZADO)
========================================================================
BANDERA FINAL: ${F_KURT}
Felicidades Auditor. Has superado las 5 fases y conquistado el reto.
EOF
chmod 600 /root/flag.txt

chmod u+s /usr/bin/find 2>/dev/null || true

chown -R www-data:www-data /var/www/html/doors /var/www/html/winehouse
chmod -R 755 /var/www/html/doors /var/www/html/winehouse

echo "[*] ========================================================"
echo "[+] DESPLIEGUE FINALIZADO EXITOSAMENTE"
echo "[*] ========================================================"
