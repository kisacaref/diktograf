# Türkçe-Fransızca Sözlük
import streamlit as st

diktotraf = {"abajur": "(a)(fr) chose qui diminue la lumière d'une lampe, abat-jour(m)",
             "abaküs": "(a)(fr) dispositif utilisé pour les calculs partiqulièrement par les enfants, abaque(m)",
             "abanmak": "(e) appliquer la force avec une partie ou le total d'un corps, s'appuyer sur qch",
             "abartmak": "(e) donner une importance inutile, exagérer qch ",
             "abes": "(s) contre la raison ou la réalité, insensée",
             "abide": "(a) ouvrage qui se situe pour rappeler une mémoire de l'humanité, monument(m)",
             "abla": "(a) sœur ainée, une femme respectée",
             "ablak": "(s) visage rond",
             "abluka": "(a) coupage des relations d'une personne ou d'un pays par la force, siège(m); ablukaya almak: assiéger",
             "abone": "(a) (fr) participation à un service payant, abonné(f); abone olmak: s'abonner à; abonman: abonnement",
             "abstre": "(s) (fr) difficile à comprendre par les cinq sens, abstrait",
             "abuk sabuk": "(z) dire des betises sans reflechir",
             "abur cubur": "(a) nourriture habituellement consommée en faisant autre chose",
             "absürt": "(s) (fr) contraire à la raison, absurde",
             "acayip": "(s) chose, evenement surprenant, bizarre",
             "acele etmek": "faire quelque chose vite, se depecher, se hâter, se précipiter, se presser",
             "aceleci": "(s) personne qui fait tout sans calme",
             "acemi": "(s) personne inexpériencée, débutant",
             }
def sozluk(key):
    if key.lower() in diktotraf.keys():
        return(diktotraf[key.lower()])
    else:
        return("Sözlüğümüzde henüz böyle bir kelime yok :)")

sozluk("ala")
