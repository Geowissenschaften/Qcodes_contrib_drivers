import logging

from .GenericMotorCLI import GenericMotorCLI

log = logging.getLogger(__name__)

class GenericSimpleMotorCLI(GenericMotorCLI):
    """
    Generic simple motor class.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.add_parameter(
            'position',
            get_cmd=lambda: self._get_thorlabs_attribute('Position'),
            set_cmd=self.set_position,
            docstring='Gets the actual position.'
            	'This parameter is motor dependent so its range is variable.'
            	'The position or -1 if the filter is in motion.'
            	'TODO: The operation will use the current value of "movement_timeout" for the move operation.'
        )

    def set_position(self, position: int, timeout_ms=0) -> None:
        """
        Sets the target Position.

        Args:
            position: 
            timeout_ms: If 0 the function will return immediately.
                        If this value is non zero, then the function will wait
                        until the move completes or the timeout elapses,
                        whichever comes first.                        
        """
        if position < 0:
        	raise ValueError("position must be non-negative.")
        self._api_interface.SetPosition(position, timeout_ms)