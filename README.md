# autojob

Automatically sends you cv and personal letter to up to 2100 job adds' email on [https://arbetsformedlingen.se/platsbanken/](https://arbetsformedlingen.se/platsbanken/) that fit you querry
## Installation

install python 3.10.
install the requests module:
```powershell
pip install requests
```

## Usage
Copy your cv and personal letter into the same folder as main.py. <br>
Then edit the variables:
```python
#Change these to you personal information
server = 'mailout.telia.com' #your email server
port = 465 #propably doesn't need to be changed but check on your email providers website
user = 'erik.cassel@telia.com'
introFile = "personligtbrevVildmark.txt" #The text you want in the email
personligtBrev = "personalLetter.pdf"
CurriculumVitae = "cv.pdf"
quarry = "it" #search term for the job application quarry
```
Open the directory with main.py in a terminal and run:
```powershell
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
