# Tutorial y Resumen de Configuración del Servidor DayZ (Proyecto Gravity)

Este documento guarda un resumen de todos los ajustes y configuraciones que hemos realizado en el servidor para tenerlo de referencia en el futuro. Todo ha sido ajustado a través del DayZ Expansion Mod.

---

## 1. Reglas de Raideo (PvE / PvP Limitado)
- **Horario de Raideo:** Activado exclusivamente los Sábados y Domingos desde las 16:00 hasta las 20:00 horas (`BaseBuildingRaidMode: 1`). Fuera de ese horario, las bases son invulnerables.
- **Explosivos:** Se ha configurado una lista blanca (`ExplosiveDamageWhitelist`) para permitir que objetos como el C4 (`Expansion_C4_Explosion`) y las cargas de brecha causen daño a las bases.
- **Multiplicadores:** El daño base de explosivos está en su valor por defecto (1.0).

---

## 2. Inteligencia Artificial (IA) y Patrullas Militares
- **Persistencia de la IA:** La IA no se desactiva aunque haya mucha gente. El límite se subió artificialmente a 100 jugadores (`PlayerCountLimit: 100` en `AISettings.json`) para que siempre haya bots.
- **Visión:** La distancia a la que la IA te percibe como amenaza se bajó a 100 metros (`ThreatDistanceLimit: 100.0`) para que no te disparen desde la otra punta del mapa.
- **Zonas Militares:** 
  - Se han configurado **11 zonas militares** clave (Tisy, NWAF, Myshkino, etc.) usando el sistema de patrullas estáticas (`ObjectPatrols`).
  - Tienen un **100% de probabilidad** de aparecer.
  - El grupo es siempre de entre **3 y 5 bots militares** por cada zona, armados y peligrosos.

---

## 3. Construcción de Bases
- **Construcción Libre:** Se ha habilitado `CanBuildAnywhere`. Los jugadores ahora pueden construir bases atravesando árboles, arbustos y rocas.
- **Banderas:** Sigue siendo obligatorio tener un territorio y colocar una bandera antes de poder construir muros u otras estructuras. El tamaño del territorio se mantiene en 50 metros de radio (100 metros de diámetro).
- **Candados:** El código de seguridad de los candados (`CodeLockLength`) se bajó del nivel casi imposible al nivel estándar de **4 dígitos**, para que sea más justo y realista de probar en un raideo.

---

## 4. Limpieza del Servidor y Zonas Seguras
- **Basura:** Se activó la limpieza automática de objetos tirados al suelo en las zonas de los Traders. Los objetos desaparecen tras 15 minutos (900 segundos).
- **Coches Abandonados:** Se activó la limpieza estricta de vehículos. Cualquier vehículo dejado abandonado dentro de un Trader desaparecerá automáticamente tras **3 horas** (10800 segundos).

---

## 5. Airdrops (Cajas de Suministros)
- **Marcadores:** Los Airdrops muestran un marcador en el mapa 2D del GPS/M (para orientarte), pero no ensucian la pantalla flotando en 3D (`Server3DMarkerOnDropLocation: 0`).
- **Dificultad:** Cuando la caja toca el suelo, aparecen **15 zombis** protegiéndola.
- **Loot Normal:** Cada caja suelta **10 objetos**. Se inyectaron **58 armas de Tactical Flava** (filtradas para quitar basura de Tier 4, cargadores y miras sueltas). Cada arma top tiene un **25% de probabilidad** de estar en la caja.
- **Loot Médico:** Existe una caja médica (`ExpansionAirdropContainer_Medical`) que también suelta 10 objetos con 15 zombis guardianes. En esta se inyectaron 15 tipos de suministros de alto nivel (Adrenalina, botiquines, férulas de aluminio, etc.) al 25% de probabilidad.

---

## 6. Vehículos (Coches, Barcos y Helicópteros)
- **Inmortalidad por Choques:** El ajuste global `DisableVehicleDamage: 1` está activo. **Ningún vehículo recibe daño por estrellarse**. Son inmortales frente a accidentes a 150 km/h, choques contra muros o aterrizajes forzosos de helicópteros.
- **Llaves y Candados:** 
  - Se integraron con éxito **59 coches de RagVehiculos** y **34 helicópteros de RedFalcon**. 
  - A todos se les puso una dificultad de cerradura estándar (`LockComplexity: 2.0`). Esto permite que los jugadores puedan comprar llaves y usarlas para proteger sus coches recién comprados en el Trader.
- **Trader:** Verificamos y todos estos vehículos moddeados ya se encuentran integrados en la base de datos de precios del mercado (`Cars.json` y `Cars_Parts.json`).

---

**Nota:** Si alguna vez decides que los coches sufran daños o cambiar los horarios de raideo, solo tienes que consultarme y te diré las líneas exactas a modificar. ¡Buena suerte administrando Gravity!
