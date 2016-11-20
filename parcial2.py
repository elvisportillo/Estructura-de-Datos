 #!/usr/bin/python
 # -*- coding: utf-8 -*-
import sqlite3
conn = sqlite3.connect('datos_empleados.db')


sql1='''
SELECT empleado.id, nombre, departamento.nombredepto,salario FROM empleado, departamento WHERE departamento.id_depto=empleado.id_depto
 
 '''

cursor1 = conn.execute(sql1)


lista = []
for row in cursor1:

	if row[3] > 0 and row[3] <= 462.00:
		if row[0] not in lista:
			lista.append(row[0])
			if row[0] in lista:
				id_empleado = row[0]
				afp = row[3] * 0.0625
				isss = row[3] * 0.03
				salario_neto = row[3] - afp -isss
				renta = 0
				conn.execute("INSERT INTO pago_empleados (id_empleado,descuento_afp,descuento_iss,renta,salario_neto) VALUES (?,?,?,?,?)" , (row[0],round(afp,2),round(isss,2),round(renta,2),round(salario_neto,2)))
				conn.commit()


	elif row[3] > 462.01 and row[3] <= 895.24:
		afp = row[3] * 0.0625
		isss = row[3] * 0.03
		renta = (row[3] - 472) * .10
		salario_neto = row[3] -afp - isss - renta - 17.67
		conn.execute("INSERT INTO pago_empleados (id_empleado,descuento_afp,descuento_iss,renta,salario_neto) VALUES (?,?,?,?,?)" , (row[0],round(afp,2),round(isss,2),round(renta,2),round(salario_neto,2)))
		conn.commit()


	elif row[3] > 895.24 and row[3] <= 2038.10:
		afp = row[3] * 0.0625
		isss = row[3] * 0.03
		renta = (row[3] - 895.24) * .20
		salario_neto = row[3] -afp - isss - renta - 60.00
		conn.execute("INSERT INTO pago_empleados (id_empleado,descuento_afp,descuento_iss,renta,salario_neto) VALUES (?,?,?,?,?)" , (row[0],round(afp,2),round(isss,2),round(renta,2),round(salario_neto,2)))
		conn.commit()

	
	elif row[3] > 2038.11:
		if row[0] not in lista:
			lista.append(row[0])
			if row[0] in lista:
				afp = row[3] * 0.0625
				isss = row[3] * 0.03
				renta = (row[3] - 2038.10) * .30
				salario_neto = row[3] -afp - isss - renta - 288.57
				conn.execute("INSERT INTO pago_empleados (id_empleado,descuento_afp,descuento_iss,renta,salario_neto) VALUES (?,?,?,?,?)" , (row[0],round(afp,2),round(isss,2),round(renta,2),round(salario_neto,2)))
				conn.commit()

print lista
