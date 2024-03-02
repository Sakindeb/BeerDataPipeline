import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
   
    # Convert the list to a DataFrame for analysis
    df = pd.DataFrame(data).astype(str)
    beer_dim = df[['name', 'tagline','description']].reset_index(drop=True)
    beer_dim['beer_id']=beer_dim.index
    beer_dim = beer_dim[['beer_id','name', 'tagline','description']]

    date_brewed_dim = df[['first_brewed']].reset_index(drop=True)
    date_brewed_dim['date_id'] = date_brewed_dim.index
    date_brewed_dim=date_brewed_dim[['date_id','first_brewed']]

    image_dim = df[['image_url']].reset_index(drop=True)
    image_dim['image_id']=image_dim.index
    image_dim=image_dim[['image_id','image_url']]


    ingredients_dim = df[['ingredients']].reset_index(drop=True)
    ingredients_dim['ingredients_id'] = ingredients_dim.index
    ingredients_dim= ingredients_dim[['ingredients_id','ingredients']]
    

    food_pairing_dim = df[['food_pairing']].reset_index(drop=True)
    food_pairing_dim['food_pairing_id'] = food_pairing_dim.index
    food_pairing_dim = food_pairing_dim[['food_pairing_id','food_pairing']]
    

    brewer_tips_dim = df[['brewers_tips']]
    brewer_tips_dim['brewer_tips_id']=brewer_tips_dim.index
    brewer_tips_dim = brewer_tips_dim[['brewer_tips_id', 'brewers_tips']]
    

    fact_table = df.merge(beer_dim, on=['name', 'tagline','description']) \
                .merge(date_brewed_dim, on='first_brewed') \
                .merge(image_dim, on='image_url') \
                .merge(ingredients_dim, on='ingredients') \
                .merge(food_pairing_dim, on='food_pairing') \
                .merge(brewer_tips_dim, on='brewers_tips') \
                [['id', 'beer_id','abv','ibu','target_fg','target_og','ebc','srm','ph','attenuation_level', 'date_id', 'image_id', 'ingredients_id','food_pairing_id', 'brewer_tips_id']]
    # Convert specific columns in the fact table to floats
    fact_table[['abv', 'ibu', 'target_fg', 'target_og', 'ebc', 'srm', 'ph', 'attenuation_level']] = fact_table[['abv', 'ibu', 'target_fg', 'target_og', 'ebc', 'srm', 'ph', 'attenuation_level']].astype(float)

    fact_table[['id']] = fact_table[['id']].astype(int)
    
   
    return {"beer_dim":beer_dim.to_dict(orient="dict"),
            "date_brewed_dim":date_brewed_dim.to_dict(orient="dict"),
            "image_dim":image_dim.to_dict(orient="dict"),
            "ingredients_dim":ingredients_dim.to_dict(orient="dict"),
            "food_pairing_dim":food_pairing_dim.to_dict(orient="dict"),
            "brewer_tips_dim": brewer_tips_dim.to_dict(orient="dict"),
            "fact_table":fact_table.to_dict(orient="dict")
    }



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
