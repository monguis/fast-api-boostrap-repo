import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('./logs/app.log')  
    ]
)

def generateLoger(name):
   return logging.getLogger(name)