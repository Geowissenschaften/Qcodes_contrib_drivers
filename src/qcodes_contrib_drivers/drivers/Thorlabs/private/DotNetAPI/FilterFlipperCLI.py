import logging

from .GenericMotorCLI_SimpleMotor import GenericSimpleMotorCLI

log = logging.getLogger(__name__)


class FilterFlipper(GenericSimpleMotorCLI):
    """
    Main entry class for the FilterFlipper.
    
    This class encapsulates the functionality provided by the Thorlabs .NET API for
    FilterFlipper, integrating with the QCoDeS framework.
    
    Args:
        polling_rate_ms: The polling rate in milliseconds for the stage status updates.
        api_interface: The API interface object for the stage. Optional
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
