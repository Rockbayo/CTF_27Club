FROM vulnerables/web-dvwa:latest

# Metadatos del reto académico
LABEL maintainer="Universidad de Cundinamarca - Línea de Profundización I"
LABEL description="Contenedor oficial del reto CTF 'The 27 Club' (Hendrix, Joplin, Morrison, Winehouse, Cobain)"

# Copiar activos del reto (Joplin, robots.txt, 404 personalizado)
COPY docker_assets/robots.txt /var/www/html/robots.txt
COPY docker_assets/rock_404.html /var/www/html/rock_404.html
RUN mkdir -p /var/www/html/cry_baby /var/www/html/admin_trampa
COPY docker_assets/janis.jpg /var/www/html/cry_baby/janis.jpg
COPY docker_assets/backup_keys.jpg /var/www/html/admin_trampa/backup_keys.jpg

# Copiar scripts y aprovisionamiento de las 5 fases
COPY provision_27club_phases.sh /tmp/provision_27club_phases.sh
RUN chmod +x /tmp/provision_27club_phases.sh

# Exponer el puerto del servidor web
EXPOSE 80

# Comando de arranque que inicializa servicios y despliega las 5 fases del reto
CMD ["/bin/bash", "-c", "service mysql start && service apache2 start && /tmp/provision_27club_phases.sh && tail -f /var/log/apache2/access.log"]
