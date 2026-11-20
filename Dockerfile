FROM vulnerables/web-dvwa:latest

# Metadatos del reto académico
LABEL maintainer="Universidad de Cundinamarca - Línea de Profundización I (Óscar Robayo)"
LABEL description="Contenedor oficial del reto CTF 'The 27 Club' (Johnson, Hendrix, Joplin, Morrison, Winehouse, Cobain)"

# Configurar repositorios Debian Archive (Stretch EOL) e instalar OpenSSH y Python para los servicios del reto
RUN sed -i 's|deb.debian.org/debian|archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i 's|security.debian.org/debian-security|archive.debian.org/debian-security|g' /etc/apt/sources.list && \
    sed -i '/stretch-updates/d' /etc/apt/sources.list && \
    echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until && \
    apt-get update && apt-get install -y --allow-unauthenticated openssh-server python3 && \
    mkdir -p /var/run/sshd && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Copiar activos del reto (Joplin, robots.txt, 404 personalizado, tráfico Hendrix PCAP)
COPY docker_assets/robots.txt /var/www/html/robots.txt
COPY docker_assets/rock_404.html /var/www/html/rock_404.html
COPY docker_assets/jimi_hendrix.pcap /var/www/html/jimi_hendrix.pcap
RUN mkdir -p /var/www/html/cry_baby /var/www/html/admin_trampa
COPY docker_assets/janis.jpg /var/www/html/cry_baby/janis.jpg
COPY docker_assets/backup_keys.jpg /var/www/html/admin_trampa/backup_keys.jpg

# Copiar scripts de aprovisionamiento y remediación (sanitizando CRLF -> LF para compatibilidad Windows/Linux)
COPY provision_27club_phases.sh /tmp/provision_27club_phases.sh
COPY hardening_remediacion.sh /tmp/hardening_remediacion.sh
RUN sed -i 's/\r$//' /tmp/provision_27club_phases.sh /tmp/hardening_remediacion.sh && \
    chmod +x /tmp/provision_27club_phases.sh /tmp/hardening_remediacion.sh

# Exponer los puertos del servidor web (80), auditoría SSH (22/2222) y señuelo Troll (1337)
EXPOSE 80 22 2222 1337

# Comando de arranque que inicializa todos los servicios y aprovisiona las 6 fases
CMD ["/bin/bash", "-c", "service mysql start && service apache2 start && service ssh start && /tmp/provision_27club_phases.sh && tail -f /var/log/apache2/access.log"]
