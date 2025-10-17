# 🧠 Optimalex Practical Exercise - Flask API

## 📄 Description du projet

Ce projet a été réalisé dans le cadre du **test technique pour le poste de Software Engineer Intern chez Optimalex**.
L’objectif est de développer une **API REST** utilisant **Flask (Python)**, qui associe des combinaisons de filtres à des *system prompts* prédéfinis selon les critères reçus dans une requête JSON.

L’application respecte l’architecture **MVC simplifiée** :

* **View (app.py)** : reçoit les requêtes HTTP et renvoie les réponses.
* **Service (prompt_service.py)** : contient la logique de correspondance entre les filtres et les prompts.
* **Model** : non requis pour cet exercice.

L’API vérifie les données d’entrée, gère les erreurs de manière robuste, et renvoie un message clair selon le cas.

---

## ⚙️ Fonctionnalités principales

✅ Reçoit une requête **POST** contenant les champs :

* `situation`
* `level`
* `file_type`
* `data`

✅ Retourne le **prompt correspondant** si la combinaison est valide.
⚠️ Retourne une erreur descriptive sinon :

* `Missing Data` → un champ est absent.
* `Invalid Prompt` → la combinaison n’existe pas.

---

## 🧩 Table de correspondance des prompts

| Prompt   | Situation            | Level     | File Type       |
| :------- | :------------------- | :-------- | :-------------- |
| Prompt 1 | Commercial Auto      | Structure | Summary Report  |
| Prompt 2 | General Liability    | Summarize | Deposition      |
| Prompt 3 | Commercial Auto      | Summarize | Summons         |
| Prompt 4 | Workers Compensation | Structure | Medical Records |
| Prompt 5 | Workers Compensation | Summarize | Summons         |

---

## 🛠️ Installation et exécution

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/bilelhichem/optimalex.git
cd optimalex_flask_api
```

### 2️⃣ Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4️⃣ Lancer le serveur Flask

```bash
python app.py
```

➡️ Le serveur démarre sur : `http://127.0.0.1:5000`

---

## 📡 Exemple d’utilisation

### ✅ Cas valide

**Requête :**

\\ Ouvrir un nouveau terminal et exécuter ça

```bash
curl -X POST http://127.0.0.1:5000/match_prompt \
-H "Content-Type: application/json" \
-d '{"situation": "Commercial Auto", "level": "Structure", "file_type": "Summary Report", "data": ""}'
```

**Réponse :**

```json
{
  "prompt": "Prompt 1"
}
```

### ⚠️ Champ manquant

```json
{
  "error": "Missing Data"
}
```

### ⚠️ Combinaison non valide

```json
{
  "error": "Invalid Prompt"
}
```

---


## 🧪 Tests rapides



* Vous pouvez trouver des photos de test depuis Insomnia dans le dossier nommé photo_from_insomnia

---

## 🧰 Technologies utilisées

* **Python 3.10+**
* **Flask 3.0.3** (framework web léger)
* **Postman / cURL** pour tester l’API

---


## ✨ Auteur

👤 **Lakhmi Hichem Billal**
🎓 Étudiant en informatique, passionné par le développement web & mobile, l’IA et les systèmes distribués.
📧 Email : [lakhmihichembillal@gmail.com](mailto:lakhmihichembillal@gmail.com)
🌐 GitHub : [https://github.com/<your_username>](https://github.com/bilelhichem)

---

## 📤 Soumission

Projet soumis dans le cadre du test technique **Optimalex - Software Engineer Intern**.
Date limite : **19 octobre 2025 à 23h59 EST**.

---

**💼 Merci à Optimalex pour cette opportunité !** 🚀
