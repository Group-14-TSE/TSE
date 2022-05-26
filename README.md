# PACTA
The application does not need to be trained as all the data is stored within the tfmodel folder.

You may train the network again if you wish :)

**NOTE**
You must have Python 3.10 and the tensorflow and sklearn libraries installed for the application to function

# How to use
1 - When launching the program, you will be greeted with a menu asking whether you want to train the application, test the network or exit. You need to decide what you want to do.

2 A - If you selected to train the network, the training cycle will be run for 1000 epochs using the passwords.txt file provided. Once complete you will then be taken back to the main menu.

2 B - If you selected to test network, you will be asked to select from one of three files. The PACTA will then output the ports / devices listed within the selected file to the "network security posture.txt" file (the file will be automatically created if not already there) along with their password strengths and their likelyhoods of being attacked. After the text file has been created / updated, PACTA will return back to its main menu.

**NOTE** If you would like to analyse your own network, simply replace the contents of one of the test network text files with your own ports / devices and passwords using the same format.

2 C - If you select to quit PACTA then the application will close.

# Issues

If you encounter any issues then please report them on the issues page here: https://github.com/Group-14-TSE/TSE/issues
