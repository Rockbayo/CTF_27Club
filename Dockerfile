FROM vulnerables/web-dvwa:latest

# Metadatos del reto académico
LABEL maintainer="Universidad de Cundinamarca - Línea de Profundización I"
LABEL description="Contenedor oficial del reto CTF 'The 27 Club' (Hendrix, Joplin, Morrison, Winehouse, Cobain)"

# Copiar scripts y aprovisionamiento de las 5 fases
COPY provision_27club_phases.sh /tmp/provision_27club_phases.sh

# Script de inicialización automatizada
RUN chmod +x /tmp/provision_27club_phases.sh

# Exponer el puerto del servidor web
EXPOSE 80

# Comando de arranque que inicializa servicios y despliega las 5 fases del reto
CMD ["/bin/bash", "-c", "service mysql start && service apache2 start && /tmp/provision_27club_phases.sh && tail -f /var/log/apache2/access.log"]

