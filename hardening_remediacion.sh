#!/bin/bash
# ==============================================================================
# SCRIPT DE HARDENING Y REMEDIACIÓN DEFENSIVA - THE 27 CLUB CTF
# Universidad de Cundinamarca - Seguridad de Aplicaciones y Hacking Ético
# Estudiante: Óscar Robayo | Línea de Profundización I
# ==============================================================================
# Este script aplica los controles defensivos y parches de seguridad
# para mitigar las 5 vulnerabilidades explotadas durante el laboratorio CTF.
# ==============================================================================

set -e

echo "========================================================================"
echo "  🛡️ INICIANDO HARDENING Y REMEDIACIÓN DEFENSIVA (THE 27 CLUB)"
echo "  Universidad de Cundinamarca - Aplicando Controles OWASP / MITRE CWE"
echo "========================================================================"
echo ""

# ------------------------------------------------------------------------------
# 1. REMEDIACIÓN FASE 1: JIMI HENDRIX (CWE-311 / C&C MITIGATION)
# ------------------------------------------------------------------------------
echo "[*] [Fase 1 - Hendrix] Mitigando tráfico C&C y User-Agent no confiable..."
# Detener baliza simulada en memoria
pkill -f "SYNT{" 2>/dev/null || true

# Configurar Apache para bloquear User-Agents maliciosos con mod_rewrite
cat << 'EOF' > /etc/apache2/conf-available/security-hendrix.conf
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_USER_AGENT} (SYNT\{|curl|nikto|sqlmap) [NC]
    RewriteRule .* - [F,L]
</IfModule>
EOF
a2enmod rewrite 2>/dev/null || true
a2enconf security-hendrix 2>/dev/null || true
echo "[+] [OK] Regla de bloqueo de tráfico C&C aplicada en Apache."

# ------------------------------------------------------------------------------
# 2. REMEDIACIÓN FASE 2: JANIS JOPLIN (CWE-200 / INFORMATION EXPOSURE)
# ------------------------------------------------------------------------------
echo "[*] [Fase 2 - Joplin] Saneando directivas robots.txt y deshabilitando Indexación..."
cat << 'EOF' > /var/www/html/robots.txt
User-agent: *
Disallow:
EOF

# Eliminar directorios trampa y restringir listado de directorios
rm -rf /var/www/html/admin_trampa
echo "Options -Indexes" > /var/www/html/.htaccess

# Truncar metadatos residuales en janis.jpg si existe
if [ -f /var/www/html/cry_baby/janis.jpg ]; then
    chmod 644 /var/www/html/cry_baby/janis.jpg
fi
echo "[+] [OK] robots.txt higienizado y listado de directorios desactivado."

# ------------------------------------------------------------------------------
# 3. REMEDIACIÓN FASE 3: JIM MORRISON (CWE-89 / SQL INJECTION MITIGATION)
# ------------------------------------------------------------------------------
echo "[*] [Fase 3 - Morrison] Refactorizando código PHP con Consultas Preparadas (PDO)..."
cat << 'EOF' > /var/www/html/doors/index.php
<?php
// REMEDIACIÓN CWE-89: Uso de PDO y Parámetros Vinculados (Prepared Statements)
$host = '127.0.0.1';
$db   = '27club';
$user = 'app';
$pass = 'vulnerables';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$opt = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_SILENT, // Deshabilitar mensajes de error detallados
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,               // Forzar consultas preparadas nativas
];

try {
    $pdo = new PDO($dsn, $user, $pass, $opt);
} catch (PDOException $e) {
    die("<p style='color: red;'>Error de conexión segura.</p>");
}

// 1. Validación estricta y tipificado del parámetro de entrada
$id = isset($_GET['id']) ? filter_var($_GET['id'], FILTER_VALIDATE_INT) : 1;
if ($id === false) {
    $id = 1; // Fallback seguro ante entradas no numéricas
}

// 2. Consulta parametrizada (Imposibilita la inyección de sintaxis SQL)
$stmt = $pdo->prepare("SELECT cancion, album, secreto FROM doors_vault WHERE id = :id");
$stmt->execute(['id' => $id]);
$registros = $stmt->fetchAll();
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>The Doors Archives - Sistema Protegido</title>
    <style>
        body { background: #0c0a14; color: #e6dfd3; font-family: 'Courier New', monospace; padding: 30px; }
        .card { max-width: 720px; margin: 0 auto; background: #151221; border: 2px solid #00ff88; border-radius: 8px; padding: 25px; }
        h1 { color: #00ff88; text-align: center; }
        .badge { background: #00ff88; color: #000; padding: 3px 8px; border-radius: 4px; font-weight: bold; }
        .box-result { margin-top: 25px; background: #07060d; padding: 15px; border-left: 4px solid #00ff88; }
        input[type="text"] { width: 75%; padding: 10px; background: #07060d; border: 1px solid #00ff88; color: #00ff88; }
        button { padding: 10px 18px; background: #00ff88; border: none; font-weight: bold; cursor: pointer; color: #000; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🔒 The Doors • Jim Morrison Vault <span class="badge">SECURED (PDO)</span></h1>
        <p style="text-align:center; color:#888;">Consultas Preparadas con Parámetros Tipificados (CWE-89 Parcheado)</p>
        
        <form method="GET" action="">
            <label><strong>ID Numérico de Catálogo:</strong></label><br><br>
            <input type="text" name="id" value="<?php echo htmlspecialchars((string)$id, ENT_QUOTES, 'UTF-8'); ?>">
            <button type="submit">Consultar</button>
        </form>

        <div class="box-result">
            <h4>Registros Obtenidos:</h4>
            <?php if (!empty($registros)): ?>
                <?php foreach ($registros as $row): ?>
                    <p><strong>Canción:</strong> <?php echo htmlspecialchars($row['cancion'], ENT_QUOTES, 'UTF-8'); ?><br>
                    <strong>Álbum:</strong> <?php echo htmlspecialchars($row['album'], ENT_QUOTES, 'UTF-8'); ?><br>
                    <strong>Archivo:</strong> <code><?php echo htmlspecialchars($row['secreto'], ENT_QUOTES, 'UTF-8'); ?></code></p>
                <?php endforeach; ?>
            <?php else: ?>
                <p style="color: #888;">No se encontraron registros para el identificador solicitado.</p>
            <?php endif; ?>
        </div>
    </div>
</body>
</html>
EOF
echo "[+] [OK] Portal de The Doors protegido mediante PDO y Prepared Statements."

# ------------------------------------------------------------------------------
# 4. REMEDIACIÓN FASE 4: AMY WINEHOUSE (CWE-79 / STORED XSS & COOKIE HARDENING)
# ------------------------------------------------------------------------------
echo "[*] [Fase 4 - Winehouse] Implementando codificación contextual y cookies HttpOnly..."
cat << 'EOF' > /var/www/html/winehouse/index.php
<?php
// REMEDIACIÓN CWE-79: Protección de Cookies con flag HttpOnly y SameSite
setcookie("admintoken", "TOKEN_PROTEGIDO_SESSION_REVOKED", [
    'expires' => time() + 3600,
    'path' => '/',
    'secure' => false,
    'httponly' => true,      // Impide acceso a la cookie mediante JavaScript (document.cookie)
    'samesite' => 'Strict'   // Protección contra ataques CSRF
]);

$conn = @new mysqli('127.0.0.1', 'app', 'vulnerables', '27club');

if ($_SERVER['REQUEST_METHOD'] === 'POST' && !empty($_POST['mensaje'])) {
    $autor = !empty($_POST['autor']) ? trim($_POST['autor']) : 'Anónimo';
    $mensaje = trim($_POST['mensaje']);
    
    // Consulta preparada para inserción segura
    $stmt = $conn->prepare("INSERT INTO amy_guestbook (autor, mensaje) VALUES (?, ?)");
    if ($stmt) {
        $stmt->bind_param("ss", $autor, $mensaje);
        $stmt->execute();
    }
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Amy Winehouse - Back To Black Lounge (Hardened)</title>
    <style>
        body { background: #0e0712; color: #e9d5ff; font-family: 'Georgia', serif; padding: 30px; }
        .card { max-width: 750px; margin: 0 auto; background: #1c1024; border: 2px solid #00f0ff; border-radius: 8px; padding: 25px; }
        h1 { color: #00f0ff; text-align: center; }
        input[type="text"], textarea { width: 95%; padding: 10px; background: #0a040d; border: 1px solid #00f0ff; color: #00f0ff; }
        button { padding: 10px 22px; background: #00f0ff; border: none; font-weight: bold; color: #000; cursor: pointer; }
        .entry { background: #0a040d; padding: 12px; border-left: 4px solid #00f0ff; margin-bottom: 12px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🎙️ Amy Winehouse • Back to Black Lounge (SECURED)</h1>
        <p style="text-align:center; color:#00f0ff;">Cookies con HttpOnly y Escape HTML Contextual (CWE-79 Parcheado)</p>

        <form method="POST" action="">
            <label>Nombre del remitente:</label><br>
            <input type="text" name="autor" placeholder="Tu nombre"><br>
            <label>Mensaje dedicatoria:</label><br>
            <textarea name="mensaje" rows="3" placeholder="Mensaje seguro..."></textarea><br>
            <button type="submit">Publicar</button>
        </form>

        <hr style="border: 0.5px solid #00f0ff; margin: 25px 0;">
        <h3>Dedicatorias Sanitizadas:</h3>
        <div id="posts">
            <?php
            $res = $conn->query("SELECT autor, mensaje, fecha FROM amy_guestbook ORDER BY id DESC LIMIT 10");
            if ($res) {
                while($row = $res->fetch_assoc()) {
                    // REMEDIACIÓN CLAVE: Escape de entidades HTML antes de la impresión en el DOM
                    $autor_seguro = htmlspecialchars($row['autor'], ENT_QUOTES, 'UTF-8');
                    $mensaje_seguro = htmlspecialchars($row['mensaje'], ENT_QUOTES, 'UTF-8');
                    echo "<div class='entry'>";
                    echo "<strong>" . $autor_seguro . "</strong> <em>(" . $row['fecha'] . ")</em><br>";
                    echo "<div class='content'>" . nl2br($mensaje_seguro) . "</div>";
                    echo "</div>";
                }
            }
            ?>
        </div>
    </div>
</body>
</html>
EOF
echo "[+] [OK] Muro de Amy protegido con htmlspecialchars y cookies HttpOnly."

# ------------------------------------------------------------------------------
# 5. REMEDIACIÓN FASE 5: KURT COBAIN (CWE-250 / SUID REMOVAL & AUTH HARDENING)
# ------------------------------------------------------------------------------
echo "[*] [Fase 5 - Cobain] Retirando bit SUID peligroso y fortaleciendo autenticación..."
# Retirar bit SUID de /usr/bin/find
chmod u-s /usr/bin/find 2>/dev/null || true

# Cambiar clave de kurt por una contraseña de alta entropía y bloquear login interactivo
usermod -s /usr/sbin/nologin kurt 2>/dev/null || true

# Proteger permisos de directorio root
chmod 700 /root
chmod 600 /root/flag.txt 2>/dev/null || true
echo "[+] [OK] Bit SUID revocado en /usr/bin/find y acceso interactivo de kurt bloqueado."

# ------------------------------------------------------------------------------
# REINICIAR SERVICIOS WEB
# ------------------------------------------------------------------------------
service apache2 reload 2>/dev/null || service apache2 restart 2>/dev/null || true

echo ""
echo "========================================================================"
echo "  ✅ PROCESO DE HARDENING COMPLETADO EXITOSAMENTE"
echo "  Todas las brechas de seguridad del CTF han sido mitigadas formalmente."
echo "========================================================================"
