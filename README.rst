|block| PyeRail : eRail python wrapper
=============================================

.. |block| image:: http://api.erail.in/images/eRail196x196.png
  :width: 20px
  :height: 20px

**What is it?**
****************

PyeRail is a Python wrapper for the eRail web API.

It allows quick and easy comsumption of eRail API from your Python applicatuon.

PyeRail reqires Python 3.


**Install**
***********

You can install pyerail using:

.. code ::

	$ pip3 install pyerail

Build from source

.. code ::
	
	$ git clone https://github.com/aksbuzz/PyeRail.git

	$ cd PyeRail

	$ make


**Usage**
*********

*API Key*
^^^^^^^^^
For access to the eRail API you would need a API Key.

You can get the API Key from here http://api.erail.in/

*Using the module*
^^^^^^^^^^^^^^^^^^

Creating an instance object of class

.. code :: python
	
	>>> from pyerail import Erail
	>>> eRail = Erail(api_key)

Getting details of given PNR number

.. code :: python
	
	>>> eRail.pnr(your_pnr_number)


In any case the object returns
	
	"status" and "result"


**Examples**
************

You can find example usage in the examples folder.

**Contribution**
****************

Contributions are welcome!.

**Documentation**
*****************

Documentation at http://api.erail.in/

**Todo**
********

- Add Python 2 support
- Add detailed documentation