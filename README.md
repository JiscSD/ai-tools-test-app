**testing app for json files from Jisc AI tools blog**


**To get started check your python version: **
								_python3 --version_

**Then set up a virtual environment using: **
								_source venv/bin/activate_  # Mac/Linux
                                          			_venv\Scripts\activate_  # Windows

**Then, install Flask inside the virtual environment:**
								_pip install flask_


**Then run the Flask script with the matching version:**
                                         			 _python3 json_formatter_flask.py_



**Run the Flask App in the Correct Directory**

Navigate to the folder where your json_formatter_flask.py is located:
                                         			 e.g cd /Users/You/Desktop/tools\ testing\ app/ python3 json_formatter_flask.py


**To Run The App**

Navigate to Your Project Folder

**Move into the directory where your json_formatter_flask.py is located:**
                                       				 e.g. cd /Users/localadmin/Desktop/AI\ tools\ testing\ app/


**Check If the Virtual Environment Exists**
							Run: 
       								_ls venv_  # Mac/Linux
                                        			_dir venv_  # Windows 

**If the venv folder is missing, you need to create a new virtual environment:**
                                        			_python3 -m venv venv_

**Use the Correct Activation Command**

For Mac/Linux, activate with:      
                                        			_source venv/bin/activate_                                 

**Running the Flask App**

Start the Flask server by running:
                                        			
					   			_python3 json_formatter_flask.py_
                                                    			
									     **or**
							   
                                       					   _flask run_
					
     				(If using flask run, make sure the FLASK_APP environment variable is set.)


Open the Web Interface

_Once the app starts, it will give you a local address, usually:_
                                        			http://127.0.0.1:5000/

**Stop the Server**

To stop the Flask app, press:
                                        			CTRL + C

Activate the virtual environment: 
                                         			_source venv/bin/activate_




**Troubleshooting**

If you have issues, Uninstall and Reinstall Flask:
                                          			_pip uninstall flask_
                                         			_pip install flask_

Check Your PYTHONPATH
                                  				Run:    _echo $PYTHONPATH_  # Mac/Linux
                                          			
						     			_echo %PYTHONPATH%_  # Windows

Troubleshooting
							•	If you get a ModuleNotFoundError, ensure you’re using the correct Python environment.
							•	If Flask runs on a different port (e.g., http://127.0.0.1:5001), use the one shown in the terminal.
