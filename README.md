This is the repository for the IPython notebooks for CSC-432.

You can read more about the Notebooks in the [IPython documentation](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html).

Usage Instructions
------------------

At the command prompt or Git Bash in windows, go the directory in which you want to keep this repository and type

    git clone git://github.com/jseabold/csc432-notebooks

This will create a directory called csc432-notebooks in that folder. If you want to name it something else, you can by appending the folder name to that command.

    git clone git://github.com/jseabold/csc432-notebooks other-name

To keep up to date with the changes in this repository, you're going to want to *fetch* the changes that I make and put up on github. You do this from the folder you just created. This is your new repository.

    git fetch origin

Then merge these changes into your local copy.

    get merge origin/master

**Note:** I do not recommend making any changes to these files. They are saved with the output cleared. So, for instance, if you run the notebooks from this directory or make changes and save them, you can run into problems when trying to merge from github. There could be a *conflict* between the remote changes and your local changes.

You will, however, want to be able to play with these. The easiest way to do this is to put these notebooks into another directory and add that directory to you IPython Notebook profile for this class. See below for an easy solution on how to automate this.

Creating a Notebook Profile
---------------------------

First you have to create a profile if you want to be able to edit it to point to the directory that contains your notebooks. To do this, run the command

    ipython profile create your-profile-name

This will create a folder in the IPython directory called `profile_your-profile-name`. It will contain a file called `ipython_notebook_config.py`. This file is self-documented, but I've included my configuration file in the repository if you want to look at it for hints. To find out for sure where your IPython directory is, run this code in Python.

    from IPython.utils.path import get_ipython_dir
    get_ipython_dir()

Or at the command prompt type

    ipython locate

Copy the provided file over the one that was automatically created. Now when you want to start the Notebook server with this profile, just type

    ipython notebook --profile=your-profile-name


Staying Up to Date
------------------

Tired of copying over the notebooks after updating them with git? This is good. A good programmer is a lazy programmer. You should write a script to automate this.

### OS X and Linux Shell Script

    #!/bin/sh
    
    cur_dir=`pwd`
    repo_dir='/home/skipper/school/csc432/csc432-notebooks/' # read only
    dest_dir='/home/skipper/school/csc432/my-notebooks/' # can make changes
    
    cd $repo_dir
    git fetch origin
    git merge origin/master --ff-only
    cp -r $repo_dir* $dest_dir
    cd $cur_dir

Save this to a file called `update_notebooks.sh`. You need to make this file `executable`, so you need to do at the command prompt

    chmod +x update_notebooks.sh

Whenever you want to update the notebooks, you just go to the directory that contains this script and type

    ./update_notebooks.sh

That's it.

### Windows Batch File

    @echo off
    
    set cur_dir=%cd%
    set repo_dir=C:\Users\skipper\school\csc432\notebooks
    set dest_dir=C:\Users\skipper\school\csc432\my-notebooks
    
    chdir /D %repo_dir%
    
    call git fetch origin master
    call git merge origin/master --ff-only
    
    chdir /D %cur_dir%
    
    xcopy /s /v %repo_dir% %dest_dir%

On Windows, scripts that you want to run at the command prompt are called batch files. Copy the above to a text file called `update_notebooks.bat`. Whenever you want to update the notebooks, just double-click on it or type the name of the batch file at the command prompt in the directory where it is.
