import subprocess

# Reemplaza el número de disco según corresponda.
# VERIFICA con 'list disk' en diskpart o desde la Administración de discos
# que este es el disco correcto.
disk_number = 2

# Comandos de DiskPart para:
# 1. Seleccionar el disco.
# 2. "clean" para eliminar todas las particiones.
# 3. Crear partición primaria.
# 4. Formatear en NTFS rápido.
# 5. Asignar una letra de unidad.
# 6. Salir.
diskpart_script = f"""
select disk {disk_number}
clean
create partition primary
format fs=ntfs quick
assign letter=Z
exit
"""

# Guardamos el script en un archivo temporal
with open("diskpart_script.txt", "w") as f:
    f.write(diskpart_script)

# Ejecutamos diskpart con el script
# Importante: Python debe correr como Administrador
subprocess.run(["diskpart", "/s", "diskpart_script.txt"], check=True)

print("Proceso completado. Verifica en la Administración de discos.")
