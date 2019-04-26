# Projecte ASIX2 - Mohamed Amine Boulaayoun

**Introducció:**

Les dades com ja sabem és l'element més valuós d’una empresa, però el problema que hi ha amb les dades es a l’hora de la seva visualització. Si hem de mostrar un CSV o Excel de 1000 files a una persona el més normal és que no interpreta correctament les dades i li sembli massa treball per això està el dit ‘una foto val més que mil paraules’. Sense anar més lluny en el camp de la ciència molts dels experiments, resultats es mostren en forma de imatges, diagrames i gràfics.

Els darrers anys s’ha popularitzat molt el terme Data Science, és una ciència que estudia les dades, involucrant mètodes científics, processos i sistemes per extreure ‘suc’ de les dades. Ja sigui coneixements o d’alguna manera explicar de forma fàcil i gràfica totes aquestes dades. El Data Science és una evolució d’alguns camps d’anàlisis de dades com ara la estadística, mineria de dades, Machine Learning.

**Objectius:**

L'objectiu del meu projecte es apartat de facilitar la visualització de la informació, perquè per l’usuari final és més còmode llegir/interpretar un gràfic.. Una altre raó es que gràcies a aquests gràfics ens poden ajudar a triar la tarifa horària.

Ens ajuda també a mirar i controlar el correcte funcionament de les plaques solars, que cobreixen realment totes les hores de sol i amb aquests gràfics podem detectar les hores on ‘fallen’ o deixen de rebre energia solar.

**Fases del meu projecte:**

La primera fase es la mes important perquè és la manera amb la qual agafo els fitxers i els tracto per després emmagatzemar-los en una base de dades i començar a treballar amb aquests.

Es una de les parts més importants ja que d'aquesta fase primera es la manera la qual inicialitza la meva base de dades.

![](https://lh4.googleusercontent.com/2pFMBg-FhZpMAgzoXNKoQZksPtGNQZ-GfqPQa9uMhzH9AiAItuPQ-IwASxPJVcgfFkDL1mnJjACngfpcQ7bgwyB0_JJhXqT9CqRI66f884MLi_NS54ZVDWB2Au8WsdqPSq-Iyuxi)
La segona fase és començar a treballar amb el Framework en qüestió Dash Plotly, l'objectiu d'aquesta fase es agafar les dades emmagatzemades en la fase anterior i utilitzar-les per crear els Dashboards.

![](https://lh5.googleusercontent.com/Hlio-Ktj91GJck9tk019abxIX_wDyHn9cI2WS1PI2x9Mh8TqHW6_tnfqLEi_ZxkHL9y-d7G0sg413tUM1Ln6XT8Sv_IuYhAWQRB5DD2_f2M9zSeLoOhEw_3Cxfgc8T39fKywyApE)
**Què és Dash Plotly ?**

És un Framework de Python per crear aplicacions web, està escrito en Flask, Plotly.js i React.js, una de les opcions de Dash és la creació d'aplicacions de visualització de dades amb interfícies d'usuari altament personalitzades en Python.

El que fa molt bé aquest software és adjuntar totes le tecnològies i protocols necessaris per construir una aplicació web en un mateix Framework. És 100% multiplataforma perquè les aplicacions es poden visualitzar des de qualsevol navegador, també una

característica molt important es que els Dashboards són de forma 'automatica' responsive i s'adapten a qualsevol dispositiu no ens hem de preocupar d'aquesta part.

Dash és una llibreria open source, lliberada sota la llicència MIT permisiva.

| | |
|----------|:-------------:|------:|
| Compatible amb DFSG |  Sí |
| Aprovada per la FSF |    Sí   |
| Aprovada per la OSI | Sí |
| Compatible amb la GPL | Sí |

**Dash Deployment Server**

Aquesta gent també ofereixen una mena de 'cloud' anomenat Dash Deployment Server, una manera de despegar i gestionar les nostres aplicacions i poder accedir a aquestes de forma fàcil i ràpida.

Característiques:

-   Sincronització entre el client i el Servidor: Permet treballar com una mena de GIT, el client pot anar fent canvis i periòdicament anar fent pushs.
    
-   Ens dóna la possibilitat de pujar i treballar amb moltes aplicacions i compartir-les entre els membres d'un departament.
    
-   Dash Deployment Server instal·la i actualitza el Python i les seves dependències per només centrar-nos en l'aplicació.
    
-   La nostra aplicació s'executa en un entorn segur i aïllat, no ens hem de preocupar de le seguretat.

Hi ha una versió gratuïta anomenada Community:

Coses que podem fer:

-   Publicar fins a un màxim de 25 Charts (Gràfics).
    
-   Ens donen 500 KB en datasets.
    

Limitacions:

Una de les principals limitacions que té aquesta versió Community es que no podem emmagatzemar els nostres charts i dashboards de forma privada, això si estem fent proves no és molt rellevant, però per exemple per una empresa que està treballant amb dades reals es un problema/delicte contra la llei RGPD. Imaginem que per un moment estem realitzant un Chart per mostrar de forma gràfica els beneficis anuals d'una empresa i estigues públic, i a lo millor aquesta informació ens interessa que no ho sàpiga la nostra competència. Per això les empreses opten per les versions de pagament.

Versions:

-   Professional: aquesta és la versió completa amb un preu de $840/any.
    
-   Personal: $420/any.
    
-   Student: $99/any.
    

Grans empreses que utilitzen aquests serveis:

Google: la veritat no entenc com Google utilitza aquest software tinguent el seu propi servei Google Chart.

P&G

Smpl Bio

Shell (benzinera).

  

El principal avantatge d’aquest servei que ofereixen és la simplicitat la qual ofereix, en pocs segons podem tenir un Dash creat, permet una àmplia configuració en quan a personalització es refereix. Podem importar tot tipus de dades i de diferents maneres ja sigui amb un simple fitxer, URL, SQL etc..

![](https://lh6.googleusercontent.com/jXsNx9cLJ4uvoxj1gu_OKqu7LiWktQLgYHNFMBX046ycZnsDG703RUIm-TYrsyXNPcvtS0_KtMr9WGCIn-iwG9YROHcaF3w0X4KpNNrhYoltW_sWHnlOW9bLN9mCAhVGkkIU-yOj)
![](https://lh5.googleusercontent.com/2S8u8Xt-kQqNXfF_TuRFT3dtDmJQC0hB8KQZCBbVaWsrj4thljDiMAo0fJqI61HP3wmCQ12eFMeDO-7PdtMAf7eSQnGUq--egbFp0iO29h-CwW1OG2BJkPkQXLuCpWwF7C-B3t3R)
També ens dóna la possibilitat de crear Dashboards, aquest Dashboard és com una mena de pàgina Web en la qual podem tenir molts Charts, texts etc l'aplicació web es configura per blocs.

  

-   Plot: són bàsicament gràfics (Charts) que hem anat creant.
    
-   Text: és un bloc on podem escriure paràgrafs amb diferents títols i subtítols.
    
-   Webpage: podem incrustar pàgines webs o components com ara video, maps, etc..

![](https://lh6.googleusercontent.com/kcbmcqhqpliHIhwUf_nS6qh1e1QJ8U-dhSQW_iE0y_XUd2Ky-hufkPpKN9uZ0gCrE8T_8q61Ac1fDAHjfUTFpHQkvfJVefhXm7SdlstNJqH0MVIWrUAi3UQJw9Ccmq_qU7Opm_EB)

Una vegada tenim fet el nostre gràfic el podem exportar en HTML i incrustar-ho en la nostra web corporativa.

**Software utilitzat:**
Perquè MongoDB i no MySQL ?
![](https://lh6.googleusercontent.com/dC52sZef2Xgc1F9yRDS0U6_gfyi1a0f4vwhRUp7fb5S28HxJF32NYlLUKJV2z0FLfsZCZuem90y6WaEh9Kh4wwIvK2efLuQFCE7MfXm3pC8Zq7RbRnOiRFLvsChYgjhBH3Ga8FSU)
Comparativa:

Principals diferències entre els dos SGBD.

SQL (MySQL):

-   Les bases de dades d’aquest son relacionals.
    
-   Les taules estan esquematitzades (camps).
    

NoSQL (MongoDB):

-   Son bases de dades que no requereixen relacions entre les taules.
    
-   Estan orientades a col·leccions i documents.
-   Tenen un millor rendiment en quant a velocitat ens referim.    
-   Son BD Schema Less.

Conclusió:

He decidit treballar amb MongoDB perquè és un SGBD molt versàtil i per les dades que he de consumir que son bàsicament CSV/XLS, és la millor opció. Una altra opció per la qual he triat aquest sistema gestor és perquè el meu framework normalment genera els gràfics a través d’un JSON.

Python 3.7

El meu projecte està orientat a la programació orientada a tractament de fitxers. He triat un projecte orientat a la programació perquè és una branca de la informàtica que m’agrada però no domini, llavors ha sigut com una mena de repte que m’he proposat.

Perquè Python ?

És un dels llenguatges que menys hem treballat al cicle, per això l’he triat per aprofundir una mica i realment he vist de primera mà la POTÈNCIA que té, és increïble la quantitat de llibreries que hi ha per solucionar qualsevol repte. El “problema” que he tingut es que moltes coses ni les coneixia i no sabia com funcionaven i gràcies en part al Robert per donar-me un cop de mà.

Avantatges:

-   És un llenguatge ràpid si el dediquem a Scripting.
    
-   El codi està net, ja que ens obliga a indentar el codi.
    
-   És un llenguatge multiplataforma (Windows, Linux, Mac).
    
-   Molta comunitat i llibreria a darrere.
    

Desavantatges:

-   Al principi la curva d'aprenentatge és molt senzilla, però com tot si comencem a entrar en detall és complica una mica la cosa..
    
-   Que hi hagi moltes llibreries externes això vol dir que d’alguna manera el llenguatge base està “buit”, amb això vull dir que si volem fer alguna cosa per exemple amb fitxers el més probable és anar a buscar una llibreria que ho compleixi.
    

**Llibrerias usadas.
PIP INSTALLS FOTO**




