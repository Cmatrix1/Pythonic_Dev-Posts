import logging

FORMAT = '%(asctime)s %(exception)s: %(error_message)s status_code=%(status_code)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('Exceptions')

class WidgetException(Exception):
    error_message = ""
    user_message = ""
    status_code = 500
    
    def to_json(self):
        return {"error_message": self.error_message,
                "user_message": self.user_message,
                "status_code": self.status_code,
                "exception": self.__class__.__name__}
        
    def log(self):
        logger.error(self.error_message, extra=self.to_json())
        

class SupplierException(WidgetException):
    error_message = "Supplier exceptions"
    user_message = "Supplier exceptions"
    status_code = 500
    
class NotManufacturedAnymore(WidgetException):
    error_message = "Not manufactured anymore"
    user_message = "Not manufactured anymore"

class ProductionDelayed(WidgetException):
    error_message = "Production delayed"
    user_message = "Production delayed"

class ShippingDelayed(WidgetException):
    error_message = "Shipping delayed"
    user_message = "Shipping delayed"
    
    
class CheckoutException(WidgetException):
    ...


ex = WidgetException()
ex.log()