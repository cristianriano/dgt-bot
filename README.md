# DGT Bot

Python script to attempt to get an appointment at the [DGT (Dirección General de Trafico)](https://sedeapl.dgt.gob.es:7443/WEB_NCIT_CONSULTA/solicitarCita.faces).

## Setup

- Python 3.9
- Chrome Driver available in PATH. Download from [here](https://chromedriver.chromium.org/downloads)
- Activate the venv with
```bash
python -m venv .ven
source .venv/bin/activate
```
- Install dependencies\
`pip install -r requirements.tx`

## TODO
- Figure out ReCaptcha (try anticaptchaofficial)
- Fill the form (fields have no id or name)
- Receive a list of oficinas

## Configuration

In the constants file set the `OFICINA` variable to the desired office
```
Albacete
Alicante/Alacant
Alicante/Alacant-Elche
Almería
Araba/Álava
Asturias-Gijón
Asturias-Oviedo
Ávila
Badajoz
Barcelona
Barcelona-Sabadell
Bizkaia
Burgos
Cáceres
Cádiz
Cádiz-La Línea
Cantabria
Castellón/Castellò
Ceuta
Ciudad Real
Córdoba
Coruña (A)
Coruña (A)-Santiago
Cuenca
Gipuzkoa
Girona
Granada
Guadalajara
Huelva
Huesca
Illes Balears-Ibiza
Illes Balears-Mallorca
Illes Balears-Menorca
Jaén
Las Palmas-Fuerteventura
Las Palmas-Gran Canaria
Las Palmas-Lanzarote
León
Lleida
Lugo
Madrid
Madrid-Alcalá de Henares
Madrid-Alcorcón
Málaga
Melilla
Murcia
Murcia-Cartagena
Navarra
Ourense
Palencia
Pontevedra
Pontevedra-Vigo
Rioja (La)
S.C. de Tenerife
S.C. de Tenerife-La Palma
Salamanca
Segovia
Sevilla
Soria
Tarragona
Teruel
Toledo
Toledo-Talavera
Valencia/València
Valencia/València-Alzira
Valladolid
Zamora
Zaragoza
```