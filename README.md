# DeleterScript

This script was originally created to delete multiple files in a directory where backup files would be collected.  It is, by default, designed to keep the 3 most recent files and delete ALL OTHER FILES in the directory.  (You've been warned)

You can change the amount of files it keeps (values 1+) by making the correct modifications in the file at the top in the first class declaration. You will absolultely need to change the path string to the path of the directory you want it to work in.  Both settings are located at the top of the file.

Be careful not to place the script in the path that you want to make it work in.  It will eventually delete it's self if you do this.
