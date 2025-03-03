**Testing app for json files from Jisc AI tools blog**


To get started, check your Python version: 

	python3 --version

Then set up a virtual environment using: 
					
     source venv/bin/activate  # Mac/Linux
     venv\Scripts\activate  # Windows

Then, install Flask inside the virtual environment:
					
     pip install flask


**Then run the Flask script with the matching version:**
                                         
	python3 json_formatter_flask.py



**Run the Flask App in the Correct Directory**

Navigate to the folder where your json_formatter_flask.py is located:
                                          e.g cd /Users/You/Desktop/tools\ testing\ app/ python3 json_formatter_flask.py


**To Run The App**

Navigate to Your Project Folder

**Move into the directory where your json_formatter_flask.py is located:**
                                       	e.g. cd /Users/localadmin/Desktop/AI\ tools\ testing\ app/


**Check If the Virtual Environment Exists**

Run:
       								
	ls venv # Mac/Linux
                                        			
	dir venv # Windows 

**If the venv folder is missing, you need to create a new virtual environment:**
                                        			
	python3 -m venv venv

**Use the Correct Activation Command**

For Mac/Linux, activate with:     
                                        			
	source venv/bin/activate                                

**Running the Flask App**

Start the Flask server by running:
                                        			
	python3 json_formatter_flask.py
                                                    			
	or
							   
	flask run
					
(If using flask run, make sure the FLASK_APP environment variable is set.)


Open the Web Interface

Once the app starts, it will give you a local address, usually:
                                        			http://127.0.0.1:5000/

**Stop the Server**

To stop the Flask app, press:
                                        			CTRL + C

Activate the virtual environment: 
                                         
	source venv/bin/activate




**Troubleshooting**

If you have issues, Uninstall and Reinstall Flask:

	pip uninstall flask
	pip install flask

Check Your PYTHONPATH

Run:    
	
 	echo $PYTHONPATH  # Mac/Linux
                                          			
	echo %PYTHONPATH%  # Windows

Troubleshooting

•	If you get a ModuleNotFoundError, ensure you’re using the correct Python environment.

•	If Flask runs on a different port (e.g., http://127.0.0.1:5001), use the one shown in the terminal.
