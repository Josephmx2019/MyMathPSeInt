Funcion aux <- csc ( x )
	aux = senn(x)
Fin Funcion

Funcion aux <- sec ( x )
	aux = 1/coss(x)
Fin Funcion

Funcion aux <- cot ( x )
	aux = 1/tann(x)
Fin Funcion

Funcion aux <- tann ( x )
	aux = senn(x)/coss(x)
Fin Funcion

Funcion aux <- senn ( x )
	Para i<-0 Hasta 21 Con Paso 1 Hacer
		aux = aux + ((((-1)^i)*(x^(2*i+1)))/fact(2*i+1))
	Fin Para
Fin Funcion

Funcion aux <- coss ( x )
	Para i<-0 Hasta 21 Con Paso 1 Hacer
		aux = (((-1)^i)*(x^(2*i))/(fact(2*i)))
	Fin Para
Fin Funcion

Funcion aux <- radToDeg ( n )
	aux = n * (PI()/180)
Fin Funcion

Funcion aux <- degToRad ( n )
	aux = n * (180/PI())
Fin Funcion

Funcion aux <- comb ( n, k )
	aux = fact(n)/(fact(k)*fact(n - k))
Fin Funcion

Funcion aux <- perm ( n, k )
	aux = fact(n)/fact(n - k)
Fin Funcion

Funcion res <- abss ( n )
	Si n > 1 Entonces
		res = n
	SiNo
		res = -n
	Fin Si
Fin Funcion

Funcion aux <- PHI ( Argumentos )
	aux = (1 + (5^0.5))/2
Fin Funcion

Funcion aux <- fact ( n )
	Si n == 0 Entonces
		aux = 1
	SiNo
		aux = n * fact(n - 1)
	Fin Si
Fin Funcion

Funcion aux <- E ( Argumentos )
	Para i<-0 Hasta 21 Con Paso 1 Hacer
		aux = aux + (1 / fact(i))
	Fin Para
Fin Funcion

Funcion aux <- PII ( Argumentossecuencia_de_acciones )
	aux = 0
	Para i<-0 Hasta 21 Con Paso 1 Hacer
		aux = (-1)^(i/2+i) + i
	Fin Para
	aux = 4 + aux
Fin Funcion

Algoritmo MyMath
	x = 0
	exit = Verdadero
	opc = 's'
	Mientras exit Hacer
		Escribir "Escriba la operación a realizar en minusculas usando abreviaciones de nombres comunes ex. exp: "
		Leer  opc
		Segun opc Hacer
			'fact':
				Escribir "Ingresa un número: "
				Leer  x
				Escribir "El resultado es: ", fact(x)
			'abs':
				Escribir "Ingresa un número: "
				Leer  x
				Escribir "El resultado es: ", abss(x)
			'perm':
				n = 0
				k = 0
				Escribir "Ingresa n: "
				Leer n
				Escribir "Ingresa k: "
				Leer k
				Escribir "El resultado es: ", perm(n, k)
			'comb':
				n = 0
				k = 0
				Escribir "Ingresa n: "
				Leer n
				Escribir "Ingresa k: "
				Leer k
				Escribir "El resultado es: ", comb(n, k)
			'deg':
				Escribir "Ingresa un número: "
				Leer  x
				Escribir "El resultado es: ", degToRad(x)
			'rad':
				Escribir "Ingresa un número: "
				Leer  x
				Escribir "El resultado es: ", radToDeg(x)
			'exit':
				Escribir "Saliendo..."
				exit = Falso
			De Otro Modo:
				Escribir "La opción ", opc, " no existe"
		Fin Segun
	Fin Mientras
FinAlgoritmo
