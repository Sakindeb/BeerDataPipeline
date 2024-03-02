SELECT DISTINCT
fact.id,
beer.name,
beer.tagline,
fact.abv,
fact.attenuation_level,
fact.ebc,
fact.ibu,
fact.ph,
fact.srm,
fact.target_fg,
fact.target_og,
tips.brewers_tips,
food.food_pairing,
image.image_url,
ingred.ingredients

FROM
`bionic-plate-410118.BeerAnalysis.fact_table` fact
JOIN `bionic-plate-410118.BeerAnalysis.beer_dim` beer ON fact.beer_id = beer.beer_id
JOIN `bionic-plate-410118.BeerAnalysis.brewer_tips_dim` tips ON fact.brewer_tips_id = tips.brewer_tips_id
JOIN `bionic-plate-410118.BeerAnalysis.date_brewed_dim` brewed ON fact.date_id = brewed.date_id
JOIN `bionic-plate-410118.BeerAnalysis.food_pairing_dim` food ON fact.food_pairing_id = food.food_pairing_id
JOIN `bionic-plate-410118.BeerAnalysis.image_dim` image ON fact.image_id = image.image_id
JOIN `bionic-plate-410118.BeerAnalysis.ingredients_dim` ingred ON fact.ingredients_id = ingred.ingredients_id
