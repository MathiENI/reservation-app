# Rapport de tests – Application de réservation

## 1. Objectif

Ce document décrit les tests réalisés sur l’application de réservation de ressources.
L’objectif est de vérifier le bon fonctionnement des fonctionnalités principales, notamment la gestion des réservations, des conflits, et des permissions utilisateurs.

---

## 2. Environnement de test

- OS : Windows
- Python : 3.14
- Framework : Django 6
- Base de données : SQL Server
- Navigateur : Chrome

---

## 3. Tests
### Test 1 – Création d’une réservation valide

- Action : création d’une réservation avec une date de début inférieure à la date de fin
- Résultat attendu : la réservation est enregistrée
- Résultat obtenu : OK

### Test 2 – Conflit de réservation

- Action : Réservation d'une ressource déjà réservée sur le même créneau
- Résultat attendu : refus de la réservation - message d'erreur "Ce créneau est déjà réservé."
- Résultat obtenu : OK - 

### Test 3 – Dates invalides

- Action : date de début supérieure à la date de fin
- Résultat attendu : message d’erreur - "La date de fin doit être après le début."
- Résultat obtenu : OK

### Test 4 – Accès administrateur

- Action : un administrateur accède à la gestion globale
- Résultat attendu : accès autorisé
- Résultat obtenu : OK

### Test 5 – Dates antérieures

- Action : choix d'une date antérieure à la date du jour
- Résultat attendu : message d’erreur - "Impossible de réserver dans le passé."
- Résultat obtenu : OK

### Test 6 – Annulation d’une réservation

- Action : annulation d’une réservation
- Résultat attendu : statut de la réservation = "annulée"
- Résultat obtenu : OK

## Améliorations possibles / TODO

- Ajout de tests automatisés (pytest / Django TestCase)
- Notifications email
- Vue calendrier avancée
