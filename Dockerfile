FROM vulnerables/web-dvwa:latest

# Metadatos del reto académico
LABEL maintainer="Universidad de Cundinamarca - Línea de Profundización I"
LABEL description="Contenedor oficial del reto CTF 'The 27 Club' (Hendrix, Joplin, Morrison, Winehouse, Cobain)"

# Instalar OpenSSH para la Fase 5 (Kurt Cobain)
RUN apt-get update && apt-get install -y --allow-unauthenticated openssh-server && \
    mkdir -p /var/run/sshd && \
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Copiar activos del reto (Joplin, robots.txt, 404 personalizado, tráfico Hendrix PCAP)
COPY docker_assets/robots.txt /var/www/html/robots.txt
COPY docker_assets/rock_404.html /var/www/html/rock_404.html
COPY docker_assets/jimi_hendrix.pcap /var/www/html/jimi_hendrix.pcap
RUN mkdir -p /var/www/html/cry_baby /var/www/html/admin_trampa
COPY docker_assets/janis.jpg /var/www/html/cry_baby/janis.jpg
COPY docker_assets/backup_keys.jpg /var/www/html/admin_trampa/backup_keys.jpg

# Copiar script de aprovisionamiento de las fases
COPY provision_27club_phases.sh /tmp/provision_27club_phases.sh
RUN chmod +x /tmp/provision_27club_phases.sh

# Exponer los puertos del servidor web, auditoría SSH y señuelo Troll
EXPOSE 80 22 2222 1337

# Comando de arranque que inicializa todos los servicios
CMD ["/bin/bash", "-c", "service mysql start && service apache2 start && service ssh start && /tmp/provision_27club_phases.sh && tail -f /var/log/apache2/access.log"]
