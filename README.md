
# Rasp_Pi-Temp

Pi-Temp (côté raspberry)

## Procédure utilisateur
En tant qu'utilisateur de la plateforme plusieurs étapes sont à respecter pour pouvoir faire fonctionner votre Raspberry Pi et le site web :

1/ Se créer un compte sur le site. 

2/ Récupérer le jeton Token affiché sur votre compte.

3/ Cloner le dépôt sur votre Raspberry pi 3 à l'emplacement suivant : /home/pi

4/ Insérer le chemin de votre fichier contenant vos températures générer automatiquement au moment de la connection de votre son de température.
 exemple : /sys/bus/w1/devices/le_numero_unique_de_la_sonde/w1_slave
 A insérer dans la méthode read_file et préciser le paramètre location avec votre chemin comme vu dans l'exemple.

3/ Insérer le Token à l'emplacement suivant : /home/pi/Rasp_Pi-Temp/api_request.py
	Une fois le fichier ouvert insérer votre Token à cet emplacement:  { headers = {'Authorization': 		    votre_clef_token} }

4/Mettre en place les tache Cron de la façon suivante :
	***crontab -e
	*/5 * * * *  /home/pi/Rasp_Pi-Temp/task_cron.sh
	1 * * * *  /home/pi/Rasp_Pi-Temp/task_cron_1.sh*****
	
De cette manière vos températures seront envoyées une fois par heure.

