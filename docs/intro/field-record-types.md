# Record and Field Types

Fieldmark offers a range of data formats and metadata, organised into different record types within a single notebook, to suit different data collection needs.  

## Understanding the parts of a Notebook

A Fieldmark notebook is comprised of Forms which can be divided into Sections. Fields or Components are placed on each Section, in the order determined by the Notebook Creator.

### Forms
Forms are highest level of organisation with a Notebook and are best understood as an Entity in traditional data modelling. They should describe the subject (or one of the subjects) of your recording project and, on export, a .csv or spreadsheet will be created for each Form.

Within Fieldmark you will be able to add a Record for each Form you create in the App. In the Demo Notebook, Thing 1 and Thing 2 are Forms:       

{% include figure image_path="//images/demonotebook_forms.jpg" alt="Forms in the Demo Notebook"%}

### Sections
Sections are defined parts of a Form. They do not affect the output of data for that Form but allow the Notebook Creator to break up the different Fields and Components onto discreet views that allow researchers to capture data in the most efficient way.

In the Demo Notebook, there are six Sections within the Form for Thing 1 that appears as tabs across the top of the screen:

{% include figure image_path="//images/demonotebook_sections.jpg" alt="Sections in the Demo Notebook"%}

### Records
Records are the primary organising unit for observations made in Fieldmark. A record is created for each Form and together they will be exported into a single table or .csv. A record will include one or more Fields.

## Supported data types and fields

Each Fieldmark data type is described below, followed by options for metadata,  helper text and other configuration settings available for all or most data types.

### Text fields

There are two primary input fields for text strings, numbers and email addresses:

1. The **Input Field** allows for a single line of free text with options to configure for text strings, numbers or email addresses:
- *string* allows for any and all text, including special characters and emojis (tapping a string input field on your mobile device will call up the standard keyboard),
- *number* will only accept numerals (tapping a number input field on your mobile device will call up the number pad), and
- *email* will accept email addresses (tapping an email input field on your mobile device will call up a keyboard with the @ key near the spacebar).  

2. The **Input Box** allows for multiples lines of free text, including special characters and emojis.

### Date and Time fields

There are three types of Date and Time fields in Fieldmark:

1. **Date Picker**: with a calendar prompt to select a date.
2. **Date and Time Picker**: with a calendar prompt with a timestamp to select a date and time.
3. **Month Picker**: with a calendar prompt to select just the month if that is all you need.

See below for the Special component that will give you the current date and time with a single tap.  

### Structured Data

There are five primary field types in Fieldmark that allow selection from a predetermined list:

1. The **Select Dropdown** field allows you to select one item from a list by tapping or clicking on the desired option from the dropdown menu 	
2. The **Multi Select Picker** allows you to select more than one option from the pick list by tapping or clicking the desired option from the picklist (tapping a second time will deselect unwanted selections)		
3. The **Hierarchical Picker** allows you to choose and option from an organised list. You can choose to store the full path, where that's useful, or just the end value if that is all you need.
4. The **Checkbox** is a simple toggle and is useful if you have just one option (eg Yes/No, Left/Right)
5. The **Radio Button** allows you to choose from a list of options without a dropdown (this is useful if you only have a few choices)

### Metadata
Fieldmark offers input options for annotation and certainty when the options are structured, but the data are fuzzy. These include a certainty flag and an option for annotated or marginal notes about the selected option.

#### Certainty Flags
All **Input** and **Structured Data** fields can be configured to include a checkbox for certainty. This allows the user to select a term from a picklist or enter a number and 'flag' the value as questionable or uncertain in some way. This is the digital equivalent of adding a question mark to a value on a paper form. The label for the flag can be customised, so the Notebook Designer could include a general flag for 'Not Sure', something more specialised like 'Label obscured' or a call to action such as 'Please Review'. Regardless of the label, the checkbox value will be stored as part of the metadata for that field, giving users the choice about how to present this uncertainty on export and during analysis.      

#### Annotations
All **Input** and **Structured Data** fields can be configured to include an annotation or marginal note. This is the digital equivalent of 'scribbling in the margin' on a paper form. It is useful when you need to make additional notes about a controlled vocabulary or number. The label for Annotation can be customised to allow for 'General Notes' or something more targeted like 'Recording Conditions'. Regardless of the label, the checkbox value will be stored as part of the metadata for that field, giving users the choice about how to present these marginal notes on export and during analysis.      

### Geospatial data
Fieldmark can capture geospatial data in two ways:

1. A single point
2. A bounding box drawn on a map

For more information, see [Mapping](mapping).

### Attachments and Multimedia

Fieldmark supports two multimedia field types:

1. **Photos** which allow to capture images directly from your device's camera while using the App
2. **Attachments**: which allow you to add any file type to your record, eg a digital sketch captured on another app on (or shared with) the same device.

Pictures and attachments inherit the record's identifier upon export.

### Special Fields

#### Identifiers

Fieldmark allocates a Universally Unique Identifier (UUID) to all records. These are long strings that are essential for the computational management of data, but can be confusing for humans. Fieldmark supports two kinds of Human Readable Identifiers (HRID) that can be used together:

1. Basic Autoincrementer: this is a simple counter for all records in a single Form on a single device
2. Unique ID: this is Human Readable Identifier that can be compiled from other values in the Record, eg 'Feature 1'.

For more information about Identifiers and Incrementors see [Identifiers](identifiers).

#### QR codes

## Relationships
Fieldmark supports two kinds of Relationships between forms:

1. Parent–Child Relationships
2. Linked

For more information see [Relationships](/Relationships/md).

## Field settings

### Validation

In addition to the required of set field types (eg a *number* **Input field** must contain a number), all fields can be configured to enforce validation rules, as determined by the Notebook Creator:

1. Required or compulsory fields: the record cannot be saved if a value is not entered
2. Custom validation: such as a number must be between a certain range   

### Default data

**Input fields** can be configured to include prepopulated text or other values.

### Persistent Values

**Input fields** can be configured to include to be 'persistent'.

### Inherited Values

**Input fields** can be configured to display values in the Parent record to avoid duplicate entries in the child record. (See Relationships.)
