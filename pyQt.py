import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton
class SimpleExample1(BaseWidget):
    def __init__(self):
        super(SimpleExample1,self).__init__('Simple Example 1')
        self._firstname =ControlText('First Name','Default value')
        self._middlename =ControlText('Middle name')
        self._lastname =ControlText('Last name')
        self._fullname =ControlText('Full name')
        self._button =ControlButton("press this button")
        self._button.value =self._buttonAction


    def _buttonAction(self):
        self._fullname.value=self._firstname.value+" "+self._middlename.value+" "+self._lastname.value

if _name_=="main": pyforms.start_app(SimpleExample1)
