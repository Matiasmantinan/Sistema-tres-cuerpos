from visual import *
from visual.graph import *


listaCuerpos = []
# Estado describe (masa, velocidad, aceleracion)
listaEstados = []

#listaVelocidades = []
#listaAceleracions = []
#listaFuerzas[]

constanteGravedad = 67

t = 0.0
dt = 0.1



ventanaGrafico1 = gdisplay(xtitle="Tiempo", ytitle="Energia Cinetica",x=500 , y=0, height=300, width = 500)
curvaPlaneta1 = gcurve(gdisplay=ventanaGrafico1, color = color.blue) 
curvaSatelite1 = gcurve(gdisplay=ventanaGrafico1, color = color.white)
curvaEstrella1 = gcurve(gdisplay=ventanaGrafico1, color = color.yellow)
curvaTotal1 = gcurve(gdisplay=ventanaGrafico1, color = color.red)

ventanaGrafico2 = gdisplay(xtitle="Tiempo", ytitle="Energia Potencial", x = 500, y=400, height=300, width = 500)
curvaEstrella2 = gcurve(gdisplay=ventanaGrafico2, color = color.yellow) 
curvaPlaneta2 = gcurve(gdisplay=ventanaGrafico2, color = color.blue) 
curvaSatelite2 = gcurve(gdisplay=ventanaGrafico2, color = color.white)
curvaTotal2 = gcurve(gdisplay=ventanaGrafico2, color = color.red)


ventanaGrafico3 =gdisplay(xtitle="Tiempo", ytitle = "Energia Mecanica", x = 0, y = 600 , height =300, width = 500)
curvaMecanica = gcurve(gdisplay=ventanaGrafico3 , color = color.cyan)


ventana =  display(title='Gravedad',x=0, y=0, width=500, height=400,center=(0,0,0), background=color.black)


# Los tamanos son incoherentes para mejorar la apreciasion, pero trato de hacer que las masas tengan sentido
#	Creo la estrella 
listaCuerpos.append(sphere(pos=(0,0,0), radius=5 , color=color.yellow))

#	Creo planeta
listaCuerpos.append(sphere( pos=(100,0,0), radius=2, make_trail=True, color=color.blue))
listaCuerpos[1].trial = curve(color=color.blue)
listaCuerpos[1].trial.append(listaCuerpos[1].pos)

#	Creo satelite
listaCuerpos.append(sphere(pos=(90,0,0), radius = 0.5, color=color.white))
listaCuerpos[2].trial = curve(color=color.white)
listaCuerpos[2].trial.append(listaCuerpos[2].pos)


masaEstrella = 150
masaPlaneta = 10
masaSatelite = 1

velocidadEstrella = vector(0,0,0)
velocidadPlaneta = vector(0,9.5,0)
velocidadSatelite = vector(2,2,0)

aceleracionEstrella = vector(0,0,0)
aceleracionPlaneta = vector(0,0,0)
aceleracionSatelite = vector(0,0,0)


listaEstados.append({'cuerpo':'estrella', 'masa':masaEstrella, 'velocidad':velocidadEstrella, 'aceleracion':aceleracionEstrella})
listaEstados.append({'cuerpo':'planeta', 'masa':masaPlaneta, 'velocidad':velocidadPlaneta, 'aceleracion':aceleracionPlaneta})
listaEstados.append({'cuerpo':'satelite', 'masa':masaSatelite, 'velocidad':velocidadSatelite, 'aceleracion':aceleracionSatelite})





fuerza_ep = vector(0,0,0)
fuerza_es = vector(0,0,0)
fuerza_ps = vector(0,0,0)


peEstrella = 0
pePlaneta = 0
peSatelite = 0



distancia_ep = 0
distancia_es = 0
distancia_ps = 0

keEstrella = 0
kePlaneta = 0
keSatelite = 0


'''
while true:
	
	rate(100)
	t =  t + dt

	for c in range(len(listaCuerpos)):
		b = c+1
		while b < len(listaCuerpos):
			# Calculo las nuevas aceleraciones
			vectorUnitario = (listaCuerpos[c].pos - listaCuerpos[b].pos)/mag(listaCuerpos[c].pos - listaCuerpos[b].pos)
			print vectorUnitario
			distancia_vec = listaCuerpos[c].pos - listaCuerpos[b].pos
			distanciaCuadrado = distancia_vec.x ** 2 + distancia_vec.y ** 2

			
			

			listaEstados[c]['aceleracion'] = -fuerza_c/ listaEstados[c]['masa']
			listaEstados[b]['aceleracion'] = fuerza_c / listaEstados[b]['masa']


			print 'Fuerza entre cuerpos ',listaEstados[b]['cuerpo'],' y ',listaEstados[c]['cuerpo'],': ',fuerza_c

			b += 1

		# Calculo las nuevas velocidades
		listaEstados[c]['velocidad'] = listaEstados[c]['velocidad'] + listaEstados[c]['aceleracion'] * dt

#		print 'Nueva velocidad: ',  listaEstados[c]['velocidad']

		# Calculo las nuevas posiciones
		listaCuerpos[c].pos = listaCuerpos[c].pos + listaEstados[c]['velocidad'] * dt 
'''

## Vuelvo a enpezar 
	
while true:
	
	rate(20)
	t =  t + dt


	# Las distancias estan al cuadrado

	# distancia estrella planeta
	vectorUnitario_ep = (listaCuerpos[0].pos - listaCuerpos[1].pos)/mag(listaCuerpos[0].pos - listaCuerpos[1].pos)
	distancia_vec = listaCuerpos[0].pos - listaCuerpos[1].pos
	#distancia_ep = distancia_vec.x ** 2 + distancia_vec.y ** 2
	# pruebo la funcion mag
	distancia_ep = mag(distancia_vec)

	# distancia estrella satelite
	vectorUnitario_es = (listaCuerpos[0].pos - listaCuerpos[2].pos)/mag(listaCuerpos[0].pos - listaCuerpos[2].pos)
	distancia_vec = listaCuerpos[0].pos - listaCuerpos[2].pos
	distancia_es = mag(distancia_vec)

	# distancia planeta estrella
	vectorUnitario_ps = (listaCuerpos[1].pos - listaCuerpos[2].pos)/mag(listaCuerpos[1].pos - listaCuerpos[2].pos)
	distancia_vec = listaCuerpos[1].pos - listaCuerpos[2].pos
	distancia_ps = mag(distancia_vec)



	fuerza_ep = vectorUnitario_ep * constanteGravedad * listaEstados[0]['masa'] * listaEstados[1]['masa']/distancia_ep**2

	fuerza_es = vectorUnitario_es * constanteGravedad * listaEstados[0]['masa'] * listaEstados[2]['masa']/distancia_es**2

	fuerza_ps = vectorUnitario_ps * constanteGravedad * listaEstados[1]['masa'] * listaEstados[2]['masa']/distancia_ps**2

	listaEstados[0]['aceleracion'] = - (fuerza_ep + fuerza_es)/ listaEstados[0]['masa']
	listaEstados[1]['aceleracion'] = (fuerza_ep - fuerza_ps) / listaEstados[1]['masa']
	listaEstados[2]['aceleracion'] = (fuerza_ps + fuerza_es) / listaEstados[2]['masa']

#	print 'aceleracion estrella = ', listaEstados[0]['aceleracion']
#	print 'aceleracion planeta = ', listaEstados[1]['aceleracion']
#	print 'aceleracion satelite = ', listaEstados[2]['aceleracion']


	
	
	print peEstrella

	for c in range(len(listaCuerpos)):
		# Calculo las nuevas velocidades
		listaEstados[c]['velocidad'] = listaEstados[c]['velocidad'] + listaEstados[c]['aceleracion'] * dt

		#print 'Nueva velocidad: ',  listaEstados[c]['velocidad']

		# Calculo las nuevas posiciones
		listaCuerpos[c].pos = listaCuerpos[c].pos + listaEstados[c]['velocidad'] * dt 

		


	peEstrella = mag(fuerza_ep) * distancia_ep  + mag(fuerza_es) * distancia_es
	pePlaneta =  mag(fuerza_ep) * distancia_ep  + mag(fuerza_ps) * distancia_ps
	peSatelite = mag(fuerza_ps) * distancia_ps + mag(fuerza_es) * distancia_es



	keEstrella = (listaEstados[0]['masa'] * mag(listaEstados[0]['velocidad']) ** 2) / 2
	kePlaneta = (listaEstados[1]['masa'] * mag(listaEstados[1]['velocidad']) ** 2) / 2
	keSatelite = (listaEstados[2]['masa'] * mag(listaEstados[2]['velocidad']) ** 2) /  2


	print 'Energia estrella: ', keEstrella ," , ", peEstrella 
	print 'Energia planeta: ', kePlaneta ," , ", pePlaneta 
	print 'Energia satelite: ', keSatelite ," , ", peSatelite 
	

	keSistema = keEstrella + kePlaneta + keSatelite
	peSistema = peEstrella + pePlaneta + peSatelite

	energiaMecanica = keSistema + peSistema


	curvaPlaneta1.plot(pos = (t, kePlaneta))
	curvaEstrella1.plot(pos = (t, keEstrella))
	curvaSatelite1.plot(pos = (t, keSatelite))
	curvaTotal1.plot(pos = (t, keSistema))

	curvaEstrella2.plot(pos=(t, peEstrella))
	curvaPlaneta2.plot(pos=(t, pePlaneta))
	curvaEstrella2.plot(pos=(t, peSatelite))
	curvaTotal2.plot(pos=(t, peSistema))

	curvaMecanica.plot(pos=(t, energiaMecanica))


	listaCuerpos[1].trial.append(listaCuerpos[1].pos)
	listaCuerpos[2].trial.append(listaCuerpos[2].pos)

