
CREATE TABLE 'avantage' (
    'entreprise_identifiant' VARCHAR(255),
    'denomination_sociale' VARCHAR(255),
    'ligne_identifiant' VARCHAR(255),
    'ligne_rectification' VARCHAR(255),
    'benef_categorie_code' VARCHAR(255),
    'categorie' VARCHAR(255),
    'benef_nom' VARCHAR(255),
    'benef_prenom' VARCHAR(255),
    'benef_qualite_code' VARCHAR(255),
    'qualite' VARCHAR(255),
    'benef_adresse1' VARCHAR(255),
    'benef_adresse2' VARCHAR(255),
    'benef_adresse3' VARCHAR(255),
    'benef_adresse4' VARCHAR(255),
    'benef_codepostal' VARCHAR(255),
    'benef_ville' VARCHAR(255),
    'benef_pays_code' VARCHAR(255),
    'pays' VARCHAR(255),
    'benef_titre_code' VARCHAR(255),
    'benef_titre_libelle' VARCHAR(255),
    'benef_specialite_code' VARCHAR(255),
    'benef_speicalite_libelle' VARCHAR(255),
    'benef_identifiant_type_code' VARCHAR(255),
    'identifiant_type' VARCHAR(255),
    'benef_identifiant_valeur' VARCHAR(255),
    'benef_etablissement' VARCHAR(255),
    'benef_etablissement_codepostal' VARCHAR(255),
    'benef_etablissement_ville' VARCHAR(255),
    'benef_denomination_sociale' VARCHAR(255),
    'benef_objet_social' VARCHAR(255),
    'ligne_type' VARCHAR(255),
    'avant_date_signature' VARCHAR(255),
    'avant_montant_ttc' VARCHAR(255),
    'avant_nature' VARCHAR(255),
    'avant_convention_lie' VARCHAR(255),
    'semestre' VARCHAR(255)
);

LOAD DATA LOCAL INFILE "C:/Users/Utilisateur/Desktop/Data_Viz-/data/declaration_avantage_2020_02_19_04_00.csv"
INTO TABLE avantage
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n' IGNORE 1 LINES;


CREATE TABLE 'convention' (
    'entreprise_identifiant' VARCHAR(255),
    'denomination_sociale' VARCHAR(255),
    'ligne_identifiant' VARCHAR(255),
    'ligne_rectification' VARCHAR(255),
    'benef_categorie_code' VARCHAR(255),
    'categorie' VARCHAR(255),
    'benef_nom' VARCHAR(255),
    'benef_prenom' VARCHAR(255),
    'benef_qualite_code' VARCHAR(255),
    'qualite' VARCHAR(255),
    'benef_adresse1' VARCHAR(255),
    'benef_adresse2' VARCHAR(255),
    'benef_adresse3' VARCHAR(255),
    'benef_adresse4' VARCHAR(255),
    'benef_codepostal' VARCHAR(255),
    'benef_ville' VARCHAR(255),
    'benef_pays_code' VARCHAR(255),
    'pays' VARCHAR(255),
    'benef_titre_code' VARCHAR(255),
    'benef_titre_libelle' VARCHAR(255),
    'benef_specialite_code' VARCHAR(255),
    'benef_speicalite_libelle' VARCHAR(255),
    'benef_identifiant_type_code' VARCHAR(255),
    'identifiant_type' VARCHAR(255),
    'benef_identifiant_valeur' VARCHAR(255),
    'benef_etablissement' VARCHAR(255),
    'benef_etablissement_codepostal' VARCHAR(255),
    'benef_etablissement_ville' VARCHAR(255),
    'benef_denomination_sociale' VARCHAR(255),
    'benef_objet_social' VARCHAR(255),
    'ligne_type' VARCHAR(255),
    'conv_date_signature' VARCHAR(255),
    'conv_objet' VARCHAR(255),
    'conv_objet_autre' VARCHAR(255),
    'conv_date_debut' VARCHAR(255),
    'conv_date_fin' VARCHAR(255),
    'conv_montant_ttc' VARCHAR(255),
    'conv_manifestation_date' VARCHAR(255),
    'conv_manifestation_nom' VARCHAR(255),
    'conv_manifestation_lieu' VARCHAR(255),
    'conv_manifestation_organisateur' VARCHAR(255)
);

LOAD DATA LOCAL INFILE "C:/Users/Utilisateur/Desktop/Data_Viz-/data/declaration_convention_2020_02_19_04_00.csv"
INTO TABLE convention
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n' IGNORE 1 LINES;


CREATE TABLE 'remuneration' (
    'entreprise_identifiant' VARCHAR(255),
    'denomination_sociale' VARCHAR(255),
    'ligne_identifiant' VARCHAR(255),
    'ligne_rectification' VARCHAR(255),
    'benef_categorie_code' VARCHAR(255),
    'categorie' VARCHAR(255),
    'benef_nom' VARCHAR(255),
    'benef_prenom' VARCHAR(255),
    'benef_qualite_code' VARCHAR(255),
    'qualite' VARCHAR(255),
    'benef_adresse1' VARCHAR(255),
    'benef_adresse2' VARCHAR(255),
    'benef_adresse3' VARCHAR(255),
    'benef_adresse4' VARCHAR(255),
    'benef_codepostal' VARCHAR(255),
    'benef_ville' VARCHAR(255),
    'benef_pays_code' VARCHAR(255),
    'pays' VARCHAR(255),
    'benef_titre_code' VARCHAR(255),
    'benef_titre_libelle' VARCHAR(255),
    'benef_specialite_code' VARCHAR(255),
    'benef_speicalite_libelle' VARCHAR(255),
    'benef_identifiant_type_code' VARCHAR(255),
    'identifiant_type' VARCHAR(255),
    'benef_identifiant_valeur' VARCHAR(255),
    'benef_etablissement' VARCHAR(255),
    'benef_etablissement_codepostal' VARCHAR(255),
    'benef_etablissement_ville' VARCHAR(255),
    'benef_denomination_sociale' VARCHAR(255),
    'benef_objet_social' VARCHAR(255),
    'ligne_type' VARCHAR(255),
    'remu_date' VARCHAR(255),
    'remu_montant_ttc' VARCHAR(255),
    'remu_convention_liee' VARCHAR(255)
);

LOAD DATA LOCAL INFILE "C:/Users/Utilisateur/Desktop/Data_Viz-/data/declaration_remuneration_2020_02_19_04_00.csv"
INTO TABLE remuneration
FIELDS TERMINATED BY ';' ENCLOSED BY '"'
LINES TERMINATED BY '\n' IGNORE 1 LINES;


CREATE TABLE 'entreprise' (
    'identifiant' VARCHAR(255),
    'pays_code' VARCHAR(255),
    'pays' VARCHAR(255),
    'secteur_activite_code' VARCHAR(255),
    'secteur' VARCHAR(255),
    'denomination_sociale' VARCHAR(255),
    'adresse_1' VARCHAR(255),
    'adresse_2' VARCHAR(255),
    'adresse_3' VARCHAR(255),
    'adresse_4' VARCHAR(255),
    'code_postal' VARCHAR(255),
    'ville' VARCHAR(255)
);

LOAD DATA LOCAL INFILE "C:/Users/Utilisateur/Desktop/Data_Viz-/data/entreprise_2020_02_19_04_00.csv"
INTO TABLE entreprise
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n' IGNORE 1 LINES;
