###
### Makefile for nsl-classes
###

ENV_PYTHON	=python3
ENV_ACTIVE	=(env | grep VIRTUAL_ENV) || . env/bin/activate
REQUIREMENTS	=requirements.txt


help:  # List targets and help messages
	@echo
	@echo "Targets supported:"
	@echo
	@cat Makefile | grep -E '^[a-zA-Z].*: ' | sed -e 's/:.*  # / - /' | sed -e 's/^/  /'
	@echo


todo:  # Display TODO items (including this one)
	@grep -nHR --color=auto 'TODO: ' .


env:  # Create Python Virtual Environment
	virtualenv -p $(ENV_PYTHON) env


requirements:  # Install required python packages into Python Virtual Environment
	$(ENV_ACTIVE) && pip install -r $(REQUIREMENTS)


init: env requirements  # Initialize the environment and install requirements
	@echo Completed initialization


jupyter-start:  # Start the jupyter server with JUPYTER_PATH
	$(ENV_ACTIVE) && jupyter notebook --no-browser --notebook-dir=$(JUPYTER_PATH)/


jupyter-publish:  # Publish a jupyter notebook to html with JUPYTER_PATH
	$(ENV_ACTIVE) && jupyter nbconvert "$(JUPYTER_PATH)" --to html


clean:  # Clean published and temporary files
	find . -type f -name '*~' -delete
	find . -type f -name '*.html' -delete
