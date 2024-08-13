import logging

# Create a logger for 'metrics'
logger = logging.getLogger('metrics')

# Create a console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter to the console handler
ch.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(ch)

# Propagate logs to the root logger
logger.propagate = True
