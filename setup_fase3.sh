#!/bin/bash
# ==============================================================================
# SCRIPT DE CONFIGURACIÓN - FASE 3: JIM MORRISON (THE DOORS - SQL INJECTION)
# Universidad de Cundinamarca - Proyecto CTF "The 27 Club"
# ==============================================================================

echo "[*] Configurando el entorno de la Fase 3 (Jim Morrison)..."

# 1. Crear directorio web temático en el contenedor
mkdir -p /var/www/html/doors
chmod 755 /var/www/html/doors

# 2. Poblar la base de datos MySQL con el baúl de Jim Morrison
mysql -u root -p'password' -e "
CREATE DATABASE IFD NOT EXISTS 27club;
USE 27club;

DROP TABLE IF EXISTS doors_vault;
CREATE TABLE doors_vault (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cancion VARCHAR(100),
    album VARCHAR(100),
    secreto VARCHAR(255),
    es_flag BOOLEAN DEFAULT FALSE
);

INSERT INTO doors_vault (cancion, album, secreto, es_flag) VALUES
('Break On Through', 'The Doors (1967)', 'FLAG{Break_On_Through_The_Doors_SQLi}', TRUE),
('Riders On The Storm', 'L.A. Woman (1971)', 'RABBIT_HOLE{Riders_On_The_Storm_Lost_In_Query}', FALSE),
('Light My Fire', 'The Doors (1967)', 'Nota: El fuego consume a quienes no sanitizan inputs.', FALSE),
('The End', 'The Doors (1967)', 'Pista: Kurt Cobain te espera en el puerto de comandos.', FALSE);
" 2>/dev/null || {
    # Fallback utilizando la base de datos de DVWA si no permite crear base de datos aparte
    mysql -u dvwa -ppassword -D dvwa -e "
    CREATE TABLE IF NOT EXISTS doors_vault (
        id INT AUTO_INCREMENT PRIMARY KEY,
        cancion VARCHAR(100),
        album VARCHAR(100),
        secreto VARCHAR(255)
    );
    INSERT INTO doors_vault (cancion, album, secreto) VALUES
    ('Break On Through', 'The Doors (1967)', 'FLAG{Break_On_Through_The_Doors_SQLi}'),
    ('Riders On The Storm', 'L.A. Woman (1971)', 'RABBIT_HOLE{Riders_On_The_Storm_Lost_In_Query}'),
    ('Light My Fire', 'The Doors (1967)', 'Nota: El fuego consume a quienes no sanitizan inputs.');
    "
}

# 3. Crear el portal vulnerable en PHP
cat << 'EOF' > /var/www/html/doors/index.php
<?php
// Templo de Jim Morrison - The Doors Archives
$db_host = '127.0.0.1';
$db_user = 'root';
$db_pass = 'password';
$db_name = '27club';

$conn = @new mysqli($db_host, $db_user, $db_pass, $db_name);
if ($conn->connect_error) {
    // Intento con usuario dvwa por compatibilidad
    $conn = new mysqli($db_host, 'dvwa', 'password', 'dvwa');
}

$id = isset($_GET['id']) ? $_GET['id'] : '1';
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>The Doors - Archivo de Jim Morrison</title>
    <style>
        body { background: #0f0c1b; color: #f0e6d2; font-family: 'Courier New', monospace; padding: 30px; }
        .box { max-width: 700px; margin: 0 auto; background: #1a162b; border: 2px solid #ffaa00; border-radius: 8px; padding: 25px; box-shadow: 0 0 20px rgba(255, 170, 0, 0.2); }
        h1 { color: #ffaa00; text-align: center; }
        p.quote { font-style: italic; color: #a09cb0; text-align: center; }
        input[type="text"] { width: 70%; padding: 10px; background: #08070d; border: 1px solid #ffaa00; color: #00ffcc; font-family: monospace; }
        button { padding: 10px 18px; background: #ffaa00; border: none; font-weight: bold; cursor: pointer; }
        .result { margin-top: 20px; background: #08070d; padding: 15px; border-left: 4px solid #ffaa00; }
        .hint { margin-top: 15px; font-size: 0.8rem; color: #6e6b7b; }
    </style>
</head>
<body>
    <div class="box">
        <h1>🚪 The Doors: Jim Morrison Archives</h1>
        <p class="quote">"There are things known and things unknown, and in between are the doors."</p>
        <hr style="border: 0.5px solid #332d4a; margin: 20px 0;">
        
        <form method="GET" action="">
            <label>Buscar Pista Musical por ID: </label><br><br>
            <input type="text" name="id" value="<?php echo htmlspecialchars($id); ?>" placeholder="Ej: 1">
            <button type="submit">Consultar</button>
        </form>

        <div class="result">
            <h3>Resultado de la consulta:</h3>
            <?php
            // Vulnerabilidad intencional: Parámetro concatenado directamente a la consulta SQL
            $query = "SELECT cancion, album, secreto FROM doors_vault WHERE id = " . $id;
            $result = $conn->query($query);

            if ($result && $result->num_rows > 0) {
                while($row = $result->fetch_assoc()) {
                    echo "<p><strong>Canción:</strong> " . htmlspecialchars($row['cancion']) . "</p>";
                    echo "<p><strong>Álbum:</strong> " . htmlspecialchars($row['album']) . "</p>";
                    echo "<p><strong>Archivo Secreto:</strong> " . htmlspecialchars($row['secreto']) . "</p>";
                    echo "<hr style='border: 0.5px dashed #443c61; margin: 10px 0;'>";
                }
            } else {
                echo "<p style='color: #ff5555;'>No se encontraron registros o error en la consulta.</p>";
                if ($conn->error) {
                    echo "<pre style='color: #ff3333;'>Error SQL: " . htmlspecialchars($conn->error) . "</pre>";
                }
            }
            ?>
        </div>
        <div class="hint">
            <strong>Fase 3:</strong> Explora la estructura de la base de datos con inyección SQL para extraer el secreto de Morrison.
        </div>
    </div>
</body>
</html>
EOF

# 4. Asignar permisos
chown -R www-data:www-data /var/www/html/doors

echo "[+] ¡Fase 3 configurada exitosamente! Accesible en: http://192.168.56.1/doors/?id=1"

