# UMLreader
This project is a simple means to read a UMLetino diagram file by parsing and retrieving the various sections

The project is designed to be run either by Main.py or by withClasses.py.
You should provide the name of the .uxf file you wish to parse as the first CLA.

e.g. withClasses.py "Playschool example 1.uxf"

The UML Diagram that the Playschool example generates is:
![Playschool example image](https://user-images.githubusercontent.com/23443826/227777238-a58cc869-d12c-4c1f-9034-654a388d57b1.png)

## Example outputs:
- Main.py "Playschool Example 1 (1).uxf" 
```
Classes:
{'title': 'Persons', 'attributes': 'personName;yearStarted;yearLeft', 'X': '370', 'Y': '280', 'H': '100', 'W': '100'}
{'title': 'Producers', 'attributes': '', 'X': '420', 'Y': '460', 'H': '70', 'W': '90'}
{'title': 'Presenters', 'attributes': '', 'X': '310', 'Y': '460', 'H': '70', 'W': '90'}
{'title': 'Themes', 'attributes': 'themeName', 'X': '620', 'Y': '140', 'H': '70', 'W': '110'}
{'title': 'Episodes', 'attributes': 'episodeAirDate', 'X': '610', 'Y': '300', 'H': '70', 'W': '120'}
{'title': 'Toys', 'attributes': 'toyName;toyType;firstAppeared', 'X': '890', 'Y': '290', 'H': '90', 'W': '120'}
{'title': 'EpisodeToys', 'attributes': '', 'X': '760', 'Y': '440', 'H': '40', 'W': '110'}

Relations:
{'linetype': '-', 'multiplicity1': '1..*', 'multiplicity2': '1..*', 'text': '< appeared in', 'additional_attributes': ['10,20', '170,20'], 'X': '720', 'Y': '320', 'H': '50', 'W': '190'}
{'linetype': '.', 'multiplicity1': None, 'multiplicity2': None, 'text': None, 'additional_attributes': ['10,10', '10,110'], 'X': '800', 'Y': '330', 'H': '130', 'W': '30'}
{'linetype': '-', 'multiplicity1': '1..*', 'multiplicity2': '1..1', 'text': 'episode theme ^', 'additional_attributes': ['10,100', '10,10'], 'X': '650', 'Y': '200', 'H': '120', 'W': '130'}
{'linetype': '<<-', 'multiplicity1': None, 'multiplicity2': None, 'text': None, 'additional_attributes': ['10,10', '10,60', '50,60', '50,90'], 'X': '400', 'Y': '370', 'H': '110', 'W': '70'}
{'linetype': '<<-', 'multiplicity1': None, 'multiplicity2': None, 'text': None, 'additional_attributes': ['70,10', '70,60', '10,60', '10,90'], 'X': '340', 'Y': '370', 'H': '110', 'W': '90'}
{'linetype': '-', 'multiplicity1': '1..*', 'multiplicity2': '1..*', 'text': '< starred', 'additional_attributes': ['10,170', '10,270', '370,270', '370,10'], 'X': '340', 'Y': '360', 'H': '290', 'W': '410'}
{'linetype': '-', 'multiplicity1': '1..*', 'multiplicity2': '1..*', 'text': 'produced ^', 'additional_attributes': ['10,140', '120,140', '120,10'], 'X': '500', 'Y': '360', 'H': '170', 'W': '210'}

Relations mapped to Classes:
{'linetype': '-', 'multiplicity1': '1..*', 'multiplicity2': '1..*', 'text': '< appeared in', 'additional_attributes': ['10,20', '170,20'], 'X': '720', 'Y': '320', 'H': '50', 'W': '190'}
{'title': 'Episodes', 'attributes': 'episodeAirDate', 'X': '610', 'Y': '300', 'H': '70', 'W': '120'}
{'title': 'Toys', 'attributes': 'toyName;toyType;firstAppeared', 'X': '890', 'Y': '290', 'H': '90', 'W': '120'}

{'linetype': '.', 'multiplicity1': None, 'multiplicity2': None, 'text': None, 'additional_attributes': ['10,10', '10,110'], 'X': '800', 'Y': '330', 'H': '130', 'W': '30'}
{'title': 'EpisodeToys', 'attributes': '', 'X': '760', 'Y': '440', 'H': '40', 'W': '110'}
{'linetype': '-', 'multiplicity1': '1..*', 'multiplicity2': '1..*', 'text': '< appeared in', 'additional_attributes': ['10,20', '170,20'], 'X': '720', 'Y': '320', 'H': '50', 'W': '190'}

{'linetype': '-', 'multiplicity1': '1..*', 'multiplicity2': '1..1', 'text': 'episode theme ^', 'additional_attributes': ['10,100', '10,10'], 'X': '650', 'Y': '200', 'H': '120', 'W': '130'}
{'title': 'Episodes', 'attributes': 'episodeAirDate', 'X': '610', 'Y': '300', 'H': '70', 'W': '120'}
{'title': 'Themes', 'attributes': 'themeName', 'X': '620', 'Y': '140', 'H': '70', 'W': '110'}

{'linetype': '<<-', 'multiplicity1': None, 'multiplicity2': None, 'text': None, 'additional_attributes': ['10,10', '10,60', '50,60', '50,90'], 'X': '400', 'Y': '370', 'H': '110', 'W': '70'}
{'title': 'Persons', 'attributes': 'personName;yearStarted;yearLeft', 'X': '370', 'Y': '280', 'H': '100', 'W': '100'}
{'title': 'Producers', 'attributes': '', 'X': '420', 'Y': '460', 'H': '70', 'W': '90'}

{'linetype': '<<-', 'multiplicity1': None, 'multiplicity2': None, 'text': None, 'additional_attributes': ['70,10', '70,60', '10,60', '10,90'], 'X': '340', 'Y': '370', 'H': '110', 'W': '90'}
{'title': 'Persons', 'attributes': 'personName;yearStarted;yearLeft', 'X': '370', 'Y': '280', 'H': '100', 'W': '100'}
{'title': 'Presenters', 'attributes': '', 'X': '310', 'Y': '460', 'H': '70', 'W': '90'}

{'linetype': '-', 'multiplicity1': '1..*', 'multiplicity2': '1..*', 'text': '< starred', 'additional_attributes': ['10,170', '10,270', '370,270', '370,10'], 'X': '340', 'Y': '360', 'H': '290', 'W': '410'}
{'title': 'Presenters', 'attributes': '', 'X': '310', 'Y': '460', 'H': '70', 'W': '90'}
{'title': 'Episodes', 'attributes': 'episodeAirDate', 'X': '610', 'Y': '300', 'H': '70', 'W': '120'}

{'linetype': '-', 'multiplicity1': '1..*', 'multiplicity2': '1..*', 'text': 'produced ^', 'additional_attributes': ['10,140', '120,140', '120,10'], 'X': '500', 'Y': '360', 'H': '170', 'W': '210'}
{'title': 'Producers', 'attributes': '', 'X': '420', 'Y': '460', 'H': '70', 'W': '90'}
{'title': 'Episodes', 'attributes': 'episodeAirDate', 'X': '610', 'Y': '300', 'H': '70', 'W': '120'}
```




- withClasses.py "Playschool Example 1 (1).uxf" 
```
Classes:
Title: Persons, Attributes: personName;yearStarted;yearLeft, X: 370, Y: 280, H: 100, W: 100, Degree: 2, Neighbours: ['Producers', 'Presenters']
Title: Producers, Attributes: , X: 420, Y: 460, H: 70, W: 90, Degree: 2, Neighbours: ['Episodes', 'Persons']
Title: Presenters, Attributes: , X: 310, Y: 460, H: 70, W: 90, Degree: 2, Neighbours: ['Episodes', 'Persons']
Title: Themes, Attributes: themeName, X: 620, Y: 140, H: 70, W: 110, Degree: 1, Neighbours: ['Episodes']
Title: Episodes, Attributes: episodeAirDate, X: 610, Y: 300, H: 70, W: 120, Degree: 5, Neighbours: ['Toys', 'Themes', 'Presenters', 'Producers', 'EpisodeToys']
Title: Toys, Attributes: toyName;toyType;firstAppeared, X: 890, Y: 290, H: 90, W: 120, Degree: 2, Neighbours: ['Episodes', 'EpisodeToys']
Title: EpisodeToys, Attributes: , X: 760, Y: 440, H: 40, W: 110, Degree: 2, Neighbours: ['Episodes', 'Toys']

Relations:
Linetype: -, M1: 1..*, M2: 1..*, Text: < appeared in, AA: ['10,20', '170,20'], X: 720, Y: 320, H: 50, W: 190, EndA: Episodes, EndB: Toys
Linetype: -, M1: 1..*, M2: 1..1, Text: episode theme ^, AA: ['10,100', '10,10'], X: 650, Y: 200, H: 120, W: 130, EndA: Episodes, EndB: Themes
Linetype: -, M1: 1..*, M2: 1..*, Text: < starred, AA: ['10,170', '10,270', '370,270', '370,10'], X: 340, Y: 360, H: 290, W: 410, EndA: Presenters, EndB: Episodes
Linetype: -, M1: 1..*, M2: 1..*, Text: produced ^, AA: ['10,140', '120,140', '120,10'], X: 500, Y: 360, H: 170, W: 210, EndA: Producers, EndB: Episodes
Linetype: ., M1: None, M2: None, Text: None, AA: ['10,10', '10,110'], X: 800, Y: 330, H: 130, W: 30, EndA: EpisodeToys, EndB: < appeared in
Linetype: <<-, M1: None, M2: None, Text: None, AA: ['10,10', '10,60', '50,60', '50,90'], X: 400, Y: 370, H: 110, W: 70, EndA: Persons, EndB: Producers
Linetype: <<-, M1: None, M2: None, Text: None, AA: ['70,10', '70,60', '10,60', '10,90'], X: 340, Y: 370, H: 110, W: 90, EndA: Persons, EndB: Presenters
```
