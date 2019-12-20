from pyDatalog import pyDatalog

pyDatalog.clear()

msg = "Entrez vos donnez personnelles"
title = "données"
fields = ("nom, lieu, nombre de victime, etat, obstacle")
mes_choix = multenterbox(msg,title,fields)



pyDatalog.create_terms('X,Y,proteger, examiner, alerter')
pyDatalog.create_terms('dangerMeca, dangerElec, dangerThermique, dangerToxique')
pyDatalog.create_terms('supprimerSansAggraver, supprimerDanger, soustraire')
pyDatalog.create_terms('reponsePos, reponseNeg')
pyDatalog.create_terms('secourir1, secourir2, secourir3, secourir4, secourir5, secourir6, secourir7, secourir8')
pyDatalog.create_terms('arreterSaignement, respirer')

proteger(X) <= dangerMeca(X)
proteger(X) <= dangerElec(X)
proteger(X) <= dangerThermique(X)
proteger(X) <= dangerToxique(X)

dangerMeca(X) <= supprimerSansAggraver(X)
dangerMeca(X) <= supprimerDanger(X)
dangerMeca(X) <= soustraire(X)

dangerElec(X) <= supprimerSansAggraver(X)
dangerElec(X) <= supprimerDanger(X)
dangerElec(X) <= soustraire(X)

dangerThermique(X) <= supprimerSansAggraver(X)
dangerThermique(X) <= supprimerDanger(X)
dangerThermique(X) <= soustraire(X)

dangerToxique(X) <= supprimerSansAggraver(X)
dangerToxique(X) <= supprimerDanger(X)
dangerToxique(X) <= soustraire(X)

proteger(X) <= examiner(X)

examiner(X) <= secourir1(X)
examiner(X) <= secourir2(X)
examiner(X) <= reponsePOs(X)
examiner(X) <= reponseNeg(X)
examiner(X) <= alerter(X)

reponsePos(X) <= secourir3(X)
reponsePos(X) <= secourir4(X)
reponsePos(X) <= secourir5(X)




secourir1(X) <= arreterSaignement(X)
secourir2(X) <= respirer(X)