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

## Cloning Repository and Creating Python Virtual Environment
To clone the repository click on the green button on the GitHub repository that says `clone` and select the `SHH` key option. Then run the following command from the command line once you have selected
the desired directory to create the repository in `git clone your_shh_key`.

Following this you need to create the Python Virtual Environment since Python is a interpreted language. If you are trying to reactivate or deactivate the virtual environment there are instructions for 
that as well. 

### Creating a New Virtual Environment
1. Install `virtualenv` (if not already installed). `virtualenv` is a tool to create isolated Python environments which we will use for setting up this repository.
To install run `pip3 install virtualenv`.

2. Run the following command to create a virtual environment in the root directory of the project (`/saga_name_generator`): `python3 -m venv venv`
Note that if you are on a Mac or Linux os the command `python3` must be followed by a three, so that it looks like `python3`. 
This will create a directory called venv in your project folder, which contains the isolated Python environment.

3. Run the following command to activate the virtual environment on your operating system:
- For Mac and Linux: `source venv/bin/activate`
- Windows (cmd): `venv\Scripts\activate`
- Windows (PowerShell): `.\venv\Scripts\Activate`
Once activated, your terminal prompt should change, and you'll see (venv) at the beginning of the command line, indicating that you're working inside the virtual environment.

4. Now we must install all project requirements from the `requirements.txt` file. 
To install run `pip3 install -r requirements.txt`
We can check we installed all our requirements by running `pip3 list` and this will show all packages within the virtual environment. 

### Deactivating Existing Environment
1. To deactivate the virtual environment simply run `deactivate`. This will return you to the global Python environment. 

### Activating Existing Environment
1. To re-activate your virtual environment run the following command to activate the virtual environment on your operating system:
- For Mac and Linux: `source venv/bin/activate`
- Windows (cmd): `venv\Scripts\activate`
- Windows (PowerShell): `.\venv\Scripts\Activate`
You can then follow steps 3-4 for setting up the virtual environment if you need to do additional configuration. 
