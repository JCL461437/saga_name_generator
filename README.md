# Name Generator API

## Making a Request to the API
To make a request to the API, you must pass the following information in the query parameter request: `gender`, `style`, and `library`.
`Gender` will determine whether the generator returns masculine or feminine names. This value should be one of the two following string values: `male` or `female`.
`Style` will determine which real or fantasy name(s) are returned by the generator. The following styles are available and must be entered as string values as presented below: 
    * 'arab'
    * 'aztec'
    * 'chinese'
    * 'dwarven'
    * 'elven'
    * 'english'
    * 'germanic'
    * 'giant'
    * 'greek'
    * 'halfling'
    * 'human'
    * 'japanese'
    * 'mongolian'
    * 'norsemen'
    * 'orc'
    * 'roman'
    * 'slavic'
    * 'steampunk'
    * 'turkish'
    * 'viking'
`Library` will generate solid names that resemble real names, or names that are more likely to have been present in books, movies, or television shows. 
Leaving the value false will generate more unique names that are a combination of syllables related to the `style` selection. This value should be either `True` or `False`. 

## JSON Response
Upon making a request to the API, your JSON response will follow this format: 

Request: `api/v1/generate_name?gender='male'?style='orc'?library=True`

Response: 
```json
{
  "name": "Snashnag Thrag'ash"
}
```