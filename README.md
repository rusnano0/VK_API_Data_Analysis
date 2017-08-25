# Repository with code for my video tutorial on connecting to VK.com API:
This code is just made for my video tutorial that show's how to work with api's to build your own instruments 
for data retireving, data analysation, and data visualisation. 
If you want to create above this code a User Friendly GUI or Web Interface you will
need to add some feautures to the code, so your users experience will be at a maximum level.

The vk_api3.py:
1. Connects to VK.com API
2. Takes all the data from the wall of a manually requested group
3. Restructures original data that comes in the response and add's some additional data
4. Structures it and send's it to a CSV

The VK_API_v3.ipynb:
1. Uses Python + Pandas and is a Jupyter Notebook, so you can see the rendered code with HTML, Data and Plots
2. Uses the CSV file returned from vk_api3.py to perform Data Analysis and Data Visualisation

[link to last video in the tutorial](https://www.youtube.com/watch?v=jnP1kri-YNM&list=PLPRsICSqu9Fp8v5Os1UU8QcSuRaN5efGf&index=8&t=2472s)

### Usage
To check out how it works you need to just get an api connection token.
So just follow this [Video](https://youtu.be/nbqRFxSw_RI?list=PLPRsICSqu9Fp8v5Os1UU8QcSuRaN5efGf) to get it.

The owner_id variable is allready set to an  existing VK.com group for example.
If you want to change the id to another group or person, you can change it. 
Just start the script, and it will return a CSV file.
And before you use the jupyter notebook. Check, that the script corresponds to the right file name of csv.
And just press run. Now you can check all the data.


