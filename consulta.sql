CREATE TABLE "Herramientas" (
	"idHerramienta"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL,
	"cantidad"	INTEGER NOT NULL,
	PRIMARY KEY("idHerramienta" AUTOINCREMENT)
);

CREATE TABLE "Personas" (
	"idPersona"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL,
	"apellido"	TEXT NOT NULL,
	PRIMARY KEY("idPersona" AUTOINCREMENT)
);

CREATE TABLE "Prestamos" (
	"idPrestamo"	INTEGER NOT NULL UNIQUE,
	"idPersona"	INTEGER NOT NULL,
	"devuelto"	INTEGER NOT NULL,
	"Fecha"	TEXT NOT NULL,
	PRIMARY KEY("idPrestamo" AUTOINCREMENT),
	FOREIGN KEY("idPersona") REFERENCES "Personas"("idPersona")
);

CREATE TABLE "HerramientasPrestadas" (
	"idHerramientaPrestada"	INTEGER NOT NULL UNIQUE,
	"idPrestamo"	INTEGER NOT NULL,
	"idHerramienta"	INTEGER NOT NULL,
	"cantidad"	INTEGER NOT NULL,	
	FOREIGN KEY("idHerramienta") REFERENCES "Herramientas"("idHerramienta"),
	FOREIGN KEY("idPrestamo") REFERENCES "Prestamos"("idPrestamo"),
	PRIMARY KEY("idHerramientaPrestada" AUTOINCREMENT)
);

CREATE TABLE "HerramientasDevueltas" (
	"idHerramientaDevuelta"	INTEGER NOT NULL UNIQUE,
	"idHerramienta"	INTEGER NOT NULL,
	"idPrestamo"	INTEGER NOT NULL,
	"cantidad"	INTEGER NOT NULL,
	PRIMARY KEY("idHerramientaDevuelta" AUTOINCREMENT),
	FOREIGN KEY("idHerramienta") REFERENCES "Herramientas" ("idHerramienta"),
	FOREIGN KEY("idPrestamo") REFERENCES "Prestamos" ("idPrestamo")
);