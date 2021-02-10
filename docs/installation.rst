============
Installation
============

If you want the latest release::
  
   python -m pip install https://github.com/OfficiumDivinum/OfficiumDivinum/archive/master.zip
    
You can also install the in-development version with::

  python -m pip install git+https://github.com/OfficiumDivinum/OfficiumDivinum

If you want to develop (or just tinker), [fork and] clone the
repository, and then install in ‘development mode’::

  git clone https://github.com/OfficiumDivinum/OfficiumDivinum # or your fork
  cd OfficiumDivinum
  python -m venv venv # create a virtual environment
  source venv/bin/activate # if using bash
  # . venv/bin/activate.fish # if using fish
  python -m pip install -e .

To run the development server, run::

  export FLASK_APP=src/api.py
  export FLASK_ENV=developemnt
  flask run

The flask development server has lots of useful features, including
the ability to open a console directly in the browser right before
whatever line caused an error.
