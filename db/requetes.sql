select identifiant, remu_montant_ttc, conv_montant_ttc from entreprise 
INNER JOIN remuneration on entreprise.identifiant = remuneration.entreprise_identifiant
INNER JOIN convention on entreprise.identifiant = convention.entreprise_identifiant
where entreprise.identifiant = "MQKQLNIC";

select identifiant, remu_montant_ttc, conv_montant_ttc, avant_montant_ttc from entreprise 
INNER JOIN remuneration on entreprise.identifiant = remuneration.entreprise_identifiant
INNER JOIN convention on entreprise.identifiant = convention.entreprise_identifiant
INNER JOIN avantage on entreprise.identifiant = avantage.entreprise_identifiant
where entreprise.identifiant = "MQKQLNIC";

"liste des entreprises ayant payées une conventioniste "
select denomination_sociale, sum(conv_montant_ttc) as total from convention
group by 1
order by 2 desc;

"liste des entreprises ayant payées une remuneration"
select denomination_sociale, sum(remu_montant_ttc) as total from remuneration
group by 1
order by 2 desc;

"liste des entreprises ayant payées des anvantages"
select denomination_sociale, sum(remu_montant_ttc) as total from avantage
group by 1
order by 2 desc;

"liste des professions et total dans convention"
SELECT qualite, COUNT(qualite) FROM convention group by 1 order by 2 desc;

"liste des professions et total dans remuneration"
SELECT qualite, COUNT(qualite) FROM remuneration group by 1 order by 2 desc;

"liste des professions et total dans avantage"
SELECT qualite, COUNT(qualite) FROM avantage group by 1 order by 2 desc;

"liste entreprise par pays ds remuneration"
select denomination_sociale , pays from remuneration 
group by 1, 2;

"liste entreprise par pays ds convention"
select denomination_sociale , pays from convention 
group by 1, 2;

"liste entreprise par pays ds avantage"
select denomination_sociale , pays from avantage 
group by 1, 2;

"nb d'entreprise par pays ds remu"
select  pays, count(pays) as total  from remuneration 
group by 1
order by 2 desc;

"nb d'entreprise par pays ds conv"
select  pays, count(pays) as total  from convention 
group by 1
order by 2 desc;

"nb d'entreprise par pays ds avant"
select  pays, count(pays) as total  from avantage 
group by 1
order by 2 desc;

