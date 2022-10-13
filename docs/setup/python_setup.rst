==============================
Python Setup
==============================

Install Python
------------------------------

* Check the version of python installed from the command line.

.. code-block::

    python --version

* Download and install Python from https://www.python.org/downloads/.

----

Create a python Virtual environment
---------------------------------------

| See: https://www.youtube.com/watch?v=APOPm01BVrk
| Rather than installing the python packages in the system wide installation of python, a virtual environment can be created that only has the modules needed for your project.
| Virtual environments allow easy maintenance of the libraries needed for the project and avoid issues that can happen when multiple dependencies conflict across multiple projects.

| Create a virtual environment for the packages needed.
| By default, these will be created in the users directory: ``C:\Users\username\``.
| In examples below, the virtual environment folder will be called: ``rtd_venv310``, but any suitable name can be used.

| Create a virtual environment, called **rtd_venv310**, with the default system python:

.. code-block::

    python -m venv rtd_venv310
    
| If there are different versions of python installed, use the full path to the version required to create the virtual environment.
| <username> used in the paths below will be different for each user.
| e.g. ``C:\Users\username\AppData\Local\Programs\Python\Python310\python.exe``
| Create a virtual environment using a specific installed version of python:

.. code-block::

    "C:\Users\username\AppData\Local\Programs\Python\Python310\python.exe" -m venv rtd_venv310

Activate a python Virtual environment
---------------------------------------

| Before you can start installing or using packages in your virtual environment you'll need to activate it.
| Activating a virtual environment will put the virtual environment-specific python and pip executables into your shell's PATH.
| Opening a terminal inside Visual Studio Code will automatically activate the selected virtual environment.

| Activate the virtual environment:

.. code-block::
    
    "C:\Users\username\rtd_venv310\Scripts\activate.bat"

----

Using the python Virtual environment in VSCode
---------------------------------------------

| VSCode allows the use of different python environments.
| To use the python python Virtual environment in VSCode:

    #. Choose **View: Command Palette**. 
    #. Into the drop down search field, type: **Python : Select Interpreter**
    #. Choose the one listed that refers to the newly created **rtd_venv310**.

----

Updating python packages 
---------------------------------

| After setting up a project, there may be a need to update the packages required.

.. code-block::

    python.exe -m pip install --upgrade pip


| From the command line change directory, ``cd`` to the folder with the ``requirements.txt`` file and use:

.. code-block::
    
    cd rtd_venv310
    pip install --upgrade -r requirements.txt

* ``-U`` can be used instead of ``--upgrade``

.. code-block::

    pip install -U -r requirements.txt


* To check the installed version numbers and other info about a package, check the output from typing in the VSCode terminal:

.. code-block::

    pip show pillow


* To get all the installed version numbers, check the output from typing in the VSCode terminal:

.. code-block::

    pip list

* To see if there are updates available, check the output from typing in the VSCode terminal:

.. code-block::

    pip list -o

----

Updating python packages
------------------------------

| This is not recommended, but is here for reference purposes. To update all packages in a Windows environment to the latest version available in the Python Package Index (PyPI), use pip in conjunction with Windows PowerShell.
| Open a command shell by typing ``powershell`` in the Search Box of the Windows Task bar.
| Enter:

.. code-block::
    
    pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

----

Uninstalling all python packages
----------------------------------

| This is not recommended, but is here for reference purposes. 
| To remove all installed python packages, leaving just the built in modules, from the command line:

.. code-block::

    pip freeze | xargs pip uninstall -y

